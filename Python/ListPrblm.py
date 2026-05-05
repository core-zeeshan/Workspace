# coding problem2: Problem: Return the count of even integers in a given list.

# a = [5,67,7,25,6,5,23,5,7,8,9,4,12,78]


def even_int(a):
    count = 0
    for i in a:
        if i % 2==0:
            count=count+1
    return count

print(even_int(a))

# comding problem1: Problem: Given a list of integers (can have duplicates), find the second largest distinct element. 
# If it doesn't exist (e.g., list has less than 2 unique values), return None.


lst = [2,3,5,2]
def second_largest(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return None
    unique_sorted = sorted(unique,reverse=True)
    return unique_sorted[1]

print(second_largest(lst))



#some square of n no.

n = int(input("Enter a No:"))
sum = 0
for i in range(1,n+1):
    sum = sum + i**2
    print(f"Square of {i}:{sum}")
    print(f"Square of {i} + Square of {i+1}:{sum}")

print(sum)

