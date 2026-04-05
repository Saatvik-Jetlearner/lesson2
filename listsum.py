def list_sum(numbers):
    if (len(numbers) == 0):
        return numbers
    else:
        return numbers[0] + list_sum(numbers[1:])
    
print(list_sum("10,20,30"))
print(list_sum("50, 30, 45"))