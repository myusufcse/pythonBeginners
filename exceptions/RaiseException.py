try:
    raise TypeError("I raised Type Error exception")
except TypeError as te:
    print(te)
    raise ValueError("I raised Value Error exception")
finally:
    print("I will execute. No Matter What")