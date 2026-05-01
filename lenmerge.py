def merge(arr, low, mid, high):
    c = []
    start1 = len(low)
    start2 = len(mid)+1

    while len(start1) <= len(mid) and len(start2) <= len(high):
        if arr[len(start1)] < arr[len(start2)]:
            c.append(arr[start1])
            start1 += 1
        else:
            c.append(arr[start2])
            start2 += 1

    while len(start1) <= len(mid):
        c.append(arr[start1])
        start1 += 1

    while len(start2) <= len(high):
        c.append(arr[start2])
        start2 += 1

    k = 0
    for i in range(low, high+1):
        arr[i] = c[k]
        k += 1

def mergeSort(arr, low, high):
    if len(low) < len(high):
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)

arr = ["elephant", "cat", "dog", "hippopotamus", "ant"]
n = len(arr)
mergeSort(arr, 0, n-1)
print(arr)