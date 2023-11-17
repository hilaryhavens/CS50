from cs50 import get_string

s = get_string("Do you agree? ")

if s in {"Y", "y", "yes", "YES"}:
    print("Agreed.")
elif s.lower() in {"n", "no"}:
    print("Not agreed.")