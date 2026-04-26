# arr = [12, 34, 2, 5, 7, 2]

# n = len(arr)
# for i in range(1, n):
#         key = arr[i]
#         print("Key", key)
#         j = i-1
#         while j>= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#             print(arr)

#         arr[j+1] = key
#         print(arr)
#         print("-"*20)

fruits = ["apple", "kiwi", "banana", "watermelon", "date"]

n = len(fruits)
for i in range(1, n):
                    
    key = fruits[i]
    print("Key", key)
    j = i-1
    while j >= 0 and len(key) < len(fruits[j]):
        fruits[j+1] == fruits[j]
        j -= 1
        print(fruits)
    fruits[j+1] = key
    print(fruits)
    print("-" * 20)
