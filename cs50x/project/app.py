import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import xml.etree.ElementTree as ET

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///speeches.db")


@app.route("/")
def index():
    """Show list of speeches"""
    # Run database query to join tables
    speeches = db.execute(
        "SELECT characters.name, speeches.text FROM (speeches INNER JOIN characters ON speeches.charID = characters.id)")

    # Iterate over each speech to get values for table
    for speech in speeches:
        # Access values in dictionary
        name = speech["name"]
        text = speech["text"]

    # Return values to HTML
    return render_template("index.html", speeches=speeches)