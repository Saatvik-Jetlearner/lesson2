arr = list(map(int,input("Enter the numbers - ").split()))
key = int(input())
if key in arr:
    print("Key Exist")

for i in range(0, len(arr)):
    if arr[i] == key:
        print("Key Exist")

for num in arr:
    if num == key:
        print("Key Exist")