a=[3,5,7,2,4]
length = len(a)
for i in range(length-1):
    swap=False
    print(f"Pass:{i}")
    for j in range(length-1-i):
        print(f"Pass{j}")
        
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            print(f"Swapped Value this:{a[j+1]} to this {a[j]}")
            swap = True
        
    if swap == False:
        break
    print(a)

