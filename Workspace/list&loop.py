# coding prblem1: Check if an array contains any duplicate elements.

# Input: [1,2,3,1]
# Output: True

arr = [1,2,3,1]
duplicate = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            duplicate = True

print(duplicate)

# coding prkblem2: Merge two sorted arrays into a single sorted array.

# Input: [1,3,5], [2,4,6]
# Output: [1,2,3,4,5,6]

arr1 = [1,3,5]
arr2=[2,4,6]
merged_arr = []
for i in arr1:
    merged_arr.append(i)
for j in arr2:
    merged_arr.append(j)

print(merged_arr)


for i in range(len(merged_arr)):
    for j in range(i+1,len(merged_arr)):
        if merged_arr[i]>merged_arr[j]:
            temp = merged_arr[i]
            merged_arr[i] = merged_arr[j]
            merged_arr[j] = temp
       
print(f"Sorted Array:{merged_arr}")

# using sorted method 

print(f"Unsorted array:{merged_arr}")
sorted_arr = sorted(merged_arr)
print(f"Sorted array:{sorted_arr}")
