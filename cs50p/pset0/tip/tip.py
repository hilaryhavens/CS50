def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    # Convert input to float and strip dollar sign
    d = float(d.replace("$", ""))
    return d


def percent_to_float(p):
    # TODO
    # Convert percent to float decimal and strip percent sign
    p = float(p.replace("%", ""))
    p = p / 100
    return p


main()