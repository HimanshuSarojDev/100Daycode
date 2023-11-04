arr = []
row, cols = 3, 3

for i in range(row):
    col = []
    for j in range(cols):
        col.append(int(input("Enter the values: ")))

    arr.append(col)

print(arr)

def search(arr, target):
    print(arr)
    found = False  # Initialize a flag to track if the target is found
    for i in range(3):
        for j in range(3):
            print(arr[i][j])
            if arr[i][j] == target:
                found = True 
                print("Value is present",i,j) # Set the flag to True when the target is found

    if found:
        print("Value is present")
    else:
        print("Value is not present")

search(arr, 3)
