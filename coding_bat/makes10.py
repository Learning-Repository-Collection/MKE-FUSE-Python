
def makes10(a, b):
    if a + b == 10:
        return True
    elif a == 10 or b == 10:
        return True
    else:
        return False

print(makes10(10,10))