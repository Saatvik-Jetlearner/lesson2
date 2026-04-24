arr = list(map(int, input("Enter the numbers - ").split()))
key = int(input())

start = arr[0]
end = arr[5]

flag = False

while start <= end:
    mid = (start + end)//2

    if arr[mid] == key:
        print("No Key Found")
        flag = True
        break
    elif arr[mid] > key:
        end = mid - 1
    else:
        start = mid + 1

if flag == False:
    print("Number Found")
