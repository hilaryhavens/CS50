class Jar:
    def __init__(self, capacity=12):
        # If capacity is not a non-negative int __init__ should instead raise a ValueError.
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        #if int(capacity) != int:
            #raise ValueError("Capacity must be an integer")
        # __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar.
        self._capacity = capacity
        # Initialize another variable for number of cookies
        self.cookies = 0

    def __str__(self):
        # __str__ should return a str with 🍪, where is the number of cookies in the cookie jar.
        return self.cookies * "🍪"

    def deposit(self, n):
        # If adding n cookies would exceed the cookie jar’s capacity, deposit should instead raise a ValueError.
        if (self.cookies + n) > self.capacity:
            raise ValueError("Number of cookies must not exceed capacity")
        # Add n cookies to the cookie jar.
        self.cookies = self.cookies + n
        return self.cookies

    def withdraw(self, n):
        # If there aren’t enough cookies in the cookie jar, raise a ValueError.
        if (self.cookies - n) < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        # Remove n cookies from the cookie jar.
        self.cookies = self.cookies - n
        return self.cookies

    @property
    def capacity(self):
        return self._capacity
        # capacity should return the cookie jar’s capacity.

    @property
    def size(self):
        # size should return the number of cookies actually in the cookie jar, initially 0.
        return self.cookies

