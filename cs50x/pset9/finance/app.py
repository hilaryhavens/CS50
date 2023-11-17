import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Run database queries
    # Query with all of companies and stock symbols per user
    stocks = db.execute(
        "SELECT companyName, companySymbol, SUM(stockShares) FROM stocks WHERE userID = ? GROUP BY companySymbol", session['user_id'])

    # Query of current cash balance
    cashVal = db.execute("SELECT cash FROM users WHERE id = ?", session['user_id'])
    cashRaw = str(cashVal[0].get('cash'))
    cash = float(cashRaw.replace(",", "").replace("$", ""))
    print(cash)

    if not stocks and not cash:
        return apology("No cash and stocks to display")

    # Set total_value to 0
    total_value = 0

    # Iterate over each stock to get values for table
    for stock in stocks:
        # Access values in dictionary
        name = stock["companyName"]
        symbol = stock["companySymbol"]
        shares = stock["SUM(stockShares)"]
        stock['shares'] = shares
        priceDict = lookup(symbol)
        price = float(priceDict.get('price'))
        stock['price'] = price
        value = float(price) * float(shares)
        stock['value'] = value
        total_value = value + total_value

    # Calculate grand total and format cash
    total = total_value + cash
    cash = usd(cash)
    total = usd(total)

    # Return values to HTML
    return render_template("index.html", stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # POST - insert stock symbol and number of shares
    if request.method == "POST":
        symbol = request.form.get("symbol")
        d_symbol = lookup(symbol)
        # if unsuccessful, return apology and "None"
        if d_symbol == None:
            return apology("Stock symbol not found.")
        shares = request.form.get("shares")
        if not shares.isnumeric():
            return apology("Shares input is not a positive integer.")
        if float(shares) <= 0:
            return apology("Shares input is not a positive integer.")
        shares = int(shares)

        # when successful, returns a dictionary with name, price, symbol
        sym_list = list(d_symbol.values())
        # Convert dictionary to list so that name, price, and symbol can be extracted
        name = sym_list[0]
        price = float(sym_list[1])
        symval = sym_list[2]

        # Confirm that funds are sufficient to make purchase and make it
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session['user_id'])
        cashVal = str(cash[0]['cash'])
        cashVal = float(cashVal.replace(",", "").replace("$", ""))
        purchase = shares * price
        if purchase > cashVal:
            return apology("Funds insufficient for transaction.")
        cashVal = usd(cashVal - (shares * price))

        # Set timestamp
        dt = datetime.now()

        # Update database following transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cashVal, session['user_id'])
        db.execute("INSERT INTO stocks (companyName, companySymbol, stockPrice, stockShares, userId, date) VALUES (?, ?, ?, ?, ?, ?)",
                   name, symval, price, shares, session['user_id'], dt)
        # Return to homepage
        return redirect("/")

    # GET - display form to purchase stock shares
    return render_template("buy.html")


@app.route("/skrilla", methods=["GET", "POST"])
@login_required
def skrilla():
    """Add more money to account"""

    # POST - add $1000 to account on submission
    if request.method == "POST":
        # Find cash balance for user
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session['user_id'])
        cashVal = float(cash[0]['cash'])
        db.execute("UPDATE users SET cash = ? WHERE id = ?", (cashVal + 1000), session['user_id'])
        # Return to homepage
        return redirect("/")

    # GET - display form to request $$
    return render_template("skrilla.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Run database queries
    # Query with all of companies and stock symbols per user
    stocks = db.execute(
        "SELECT companyName, companySymbol, stockPrice, stockShares, date FROM stocks WHERE userID = ? ORDER BY date", session['user_id'])

    if not stocks:
        return apology("No transaction history")

    # Iterate over each stock to get values for table
    for stock in stocks:
        # Access values in dictionary
        shares = int(stock['stockShares'])
        if shares > 0:
            stock['type'] = "Bought"
        elif shares < 0:
            stock['type'] = "Sold"
        stock['shares'] = abs(shares)

    # Return values to HTML
    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # POST - lookup the stock symbol by calling the lookup function, and display results
    if request.method == "POST":
        symbol = request.form.get("symbol")
        d_symbol = lookup(symbol)

        # if unsuccessful, return apology and "None"
        if d_symbol == None:
            return apology("Stock symbol not found.")

        # when successful, returns a dictionary with name, price, symbol
        sym_list = list(d_symbol.values())

        # Convert dictionary to list so that name, price, and symbol can be displayed in table
        name = sym_list[0]
        price = sym_list[1]
        symval = sym_list[2]
        return render_template("quoted.html", symbolval=d_symbol, name=name, price=price, symbol=symval)

    # GET - display form to request stock quote
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Validate submission

    # POST
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check for form errors
        # Return if any field is blank
        if not username or not password or not confirmation:
            return apology("Username and/or Password left blank.")
        # Return if pass and confirmation don't match
        if password != confirmation:
            return apology("Password and confirmation don't match.")
        # Return if username is already taken
        repeat = db.execute("SELECT username FROM users")
        revalues = [d['username'] for d in repeat]
        if username in revalues:
            return apology("Username is already taken.")

        # Insert new user into SQL users table with generate_password_hash
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
        return redirect("/")

    # GET: display registration form so that they can create new account
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # POST - insert stock symbol and number of shares to be sold
    if request.method == "POST":
        symbol = request.form.get("symbol")
        d_symbol = lookup(symbol)
        # if unsuccessful, return apology and "None"
        if d_symbol == None:
            return apology("Stock symbol not found.")
        shares = request.form.get("shares")
        # apology if a non-positive integer is inputed to shares
        if not shares.isnumeric():
            return apology("Shares input is not a positive integer.")
        if float(shares) <= 0:
            return apology("Shares input is not a positive integer.")
        # apology if the user does not have enough shares
        user = db.execute("SELECT SUM(stockShares) FROM stocks WHERE companySymbol = ? AND userId = ?",
                          d_symbol['symbol'], session['user_id'])
        #stocks = db.execute("SELECT companyName, companySymbol, SUM(stockShares) FROM stocks WHERE userID = ? GROUP BY companySymbol", session['user_id'])
        user_shares = float(user[0]['SUM(stockShares)'])
        shares = float(shares)
        if shares > user_shares:
            return apology("User does not own enough shares to complete transaction.")
        new_shares = -abs(shares)

        # Get price for shares and sale
        price = float(d_symbol.get('price'))
        sale = float(price * shares)

        # when successful, returns a dictionary with name, price, symbol
        sym_list = list(d_symbol.values())
        # Convert dictionary to list so that name, price, and symbol can be extracted
        name = sym_list[0]
        symval = sym_list[2]

        # Add money to cash after sale
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session['user_id'])
        cashVal = str(cash[0]['cash'])
        cashVal = cashVal.replace(",", "").replace("$", "")
        cashVal = float(cashVal)
        cashVal = cashVal + float(sale)
        print(cashVal)

        # Set timestamp
        dt = datetime.now()

        # Update database following transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cashVal, session['user_id'])
        db.execute("INSERT INTO stocks (companyName, companySymbol, stockPrice, stockShares, userId, date) VALUES (?, ?, ?, ?, ?, ?)",
                   name, symval, price, new_shares, session['user_id'], dt)
        # Return to homepage
        return redirect("/")

    # GET - display form to purchase stock shares
    stocks = db.execute("SELECT DISTINCT companySymbol FROM stocks WHERE userID = ?", session['user_id'])
    # query database for stock symbols over for loop
    symbols = []
    for stock in stocks:
        # Access values in dictionary
        symbols.append(stock["companySymbol"])
    print(symbols)
    return render_template("sell.html", symbols=symbols)
