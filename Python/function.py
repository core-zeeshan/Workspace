a = float(input("Enter a value of A"))
b = float(input("Enter a value of B:"))
print(f"Before Swap A is {a}")
print(f"Before Swap B is {b}")
def math(a,b):
    add = a+b
    sub = a-b
    mlt = a*b
    dvd = a/b
    return add, sub,mlt,dvd


add,sub,mlt,dvd = math(a,b)
print(f"Addition:{add}")
print(f"Substraction:{sub}")
print(mlt)
print(dvd)
