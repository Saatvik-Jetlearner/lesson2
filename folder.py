import os

main_folder = "datasets"

os.makedirs(main_folder, exist_ok=True)

name = input("Enter your name: ")

subfolder = os.path.join(main_folder, name)

os.makedirs(subfolder, exist_ok=True)

print(f"Folder '{subfolder}' has been created.")
print("Path:", subfolder)