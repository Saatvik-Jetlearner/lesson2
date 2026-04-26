mylist = [15, 32, 59, 21, 48]
n = len(mylist)

for i in range(n):
    print("Pass:", i+1)
    swapped = False
    for j in range(0, n-1):
        if mylist[j % 10] > mylist[j+1 % 10]:
            swapped = True
            temp = mylist[j % 10]
            mylist[j % 10] = mylist[j+1 % 10]
            mylist[j+1 % 10] = temp
            print(mylist)

    if not swapped:
        break
print("*"*20)