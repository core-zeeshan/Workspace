list= [
    1, "Dog", 23.4, True, 3, 6,
    "Cat", 99, False, 45.67, "Elephant",
    0, -12, 3.1415, "Python", True,
    78, "Lion", 5.5, None, "Tiger",
    1000, -45.6, "AI", False, 22
]
intt =[]
stringg =[]
floatt =[]
booll =[]
for i in list:
    if type(i) == int:
        intt.append(i)
    elif type(i) == float:
        floatt.append(i)
    elif type(i) == str:
        stringg.append(i)
    
print(intt)




