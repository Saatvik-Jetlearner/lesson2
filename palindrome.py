def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    else:
        if word[0] != word[-1]:
            return False
        return is_palindrome(word[1:-1])
    
print(is_palindrome("mantle"))
print(is_palindrome("racecar"))
