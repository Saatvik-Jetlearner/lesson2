contact = ["Charles", "Hunter", "Frank", "Hannah", "Bill"]
target = input("Who are you looking for?")
if target in contact:
    print("Contact Found")
else:
    print("Contact Not Found")
    
for i in range(0, len(contact)):
    if contact[i] == target:
        print("Contact Found")
        break



