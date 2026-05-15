# class Stack:

#     def __init__(self, n):
#         self.stack = []
#         self.n = n
    
#     def push(self, k):
#         if len(self.stack) < self.n:
#             self.stack.append(k)
#         else:
#             print("The stack is full.")

#     def pop(self):
#         if len(self.stack) == 0:
#             print("The stack is empty")
#         else:
#             return self.stack.pop(-1)
            
#     def top(self):
#         if len(self.stack) == 0:
#             print("The stack is empty")
#         else:
#             return self.stack[-1]
    
#     def display(self):
#         print(self.stack)

#     def size(self):
#         return len(self.stack)
    
    
# s = Stack(6)
# s.push("P")
# s.push("Y")
# s.push("T")
# s.push("H")
# s.push("O")
# s.push("N")
# s.display()
# print(s.top())

stack = []
text = input("Enter a string")
for i in text:
    stack.append(i)
reverse = ""
while len(stack) > 0:
    s = stack.pop()
    reverse = reverse + s

print(reverse)