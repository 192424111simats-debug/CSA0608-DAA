# Linear Search

arr = [10, 25, 30, 45, 50]
key = 30

index = -1

for i in range(len(arr)):
    if arr[i] == key:
        index = i
        break

if index != -1:
    print("Key found at index", index)
else:
    print("Key not found")
