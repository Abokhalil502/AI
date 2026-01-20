def complex(z, y, x):
    return z * (y + x)**x - (x-y)
def simple(a, b):
    return a + b
def age(c):
    if c < 0:
        return "Invalid age"
    elif c == 0:
        return "Newborn"
    else:
        return f"Age is {c}"