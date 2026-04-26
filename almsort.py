mylist = [3, 2, 1, 4, 5]
n = len(mylist)

for i in range(n):
    print("Pass:", i+1)
    swapped = False
    for j in range(0, n-1):
        if mylist[j] > mylist[j+1]:
            swapped = True
            temp = mylist[j]
            mylist[j] = mylist[j+1]
            mylist[j+1] = temp
            print(mylist)
        if swapped == False:
            print("Stopped Early!")
            break

    if not swapped:
        break
print("*"*20)
