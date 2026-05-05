a = int(input("Enter a value of A: "))
b = int(input("Enter a value of B: "))
def swap(a,b):
    c=a
    a=b
    b=c 

    return a,b

a,b = swap(a,b)
print(f"After Swap A is {a}")
print(f"After Swap B is {b}")



a = int(input("Enter a value of A: "))
b = int(input("Enter a value of B: "))
def swap(a,b):
    a,b = b,a

    return a,b

a,b = swap(a,b)
print(f"After Swap A is {a}")
print(f"After Swap B is {b}")