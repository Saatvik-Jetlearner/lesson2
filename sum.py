def sum(num):
    if num == 1 or num == 0:
        return num
    else:
        return num + (num-1)
    
print(sum(5))
print(sum(10))