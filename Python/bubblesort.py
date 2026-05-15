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




import matplotlib.pyplot as plt

# Example data
x = [1,2,3,4,5]
y = [2,4,5,4,5]

# Predicted values
y_pred = [2.2,3.1,4.0,4.8,5.7]

# Plot actual points
plt.scatter(x, y, label="Actual Y")

# Plot prediction line
plt.plot(x, y_pred, label="Predicted Line")

# Labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Actual vs Predicted")

# Show legend
plt.legend()

# Show graph
plt.show()
