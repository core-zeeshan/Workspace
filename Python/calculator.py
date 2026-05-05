math_function = input("Enter maths function(Add,Sub,Multi,Divs):")
a = int(input("Enter 1st No:"))
b = int(input("Enter 2nd NO:"))
def math(a,b,math_function):
    if math_function == "Add":
        result = a+b
        return result
    elif math_function == "Sub":
        result= a+b
        return result
    elif math_function == "Multi":
        result = a*b
        return result
    else:
        result = a/b
        return result
print(math(a,b,math_function))
