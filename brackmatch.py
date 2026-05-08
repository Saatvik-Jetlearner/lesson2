# Given an expression string
# Write a python program to find whether a given string has balanced parentheses or not. 
# One approach to check balanced parentheses is to use stack. 
# Each time, when an open parentheses is encountered push it in the stack, 
# and when closed parenthesis is encountered, match it with the top of stack and pop it. 
# If stack is empty at the end, return Balanced otherwise, Unbalanced.


open_list = ["[", "{", "("]
close_list = ["]", "}" ")"]

def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and 
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

string = "{Hello}"
print(string, "-", check(string))