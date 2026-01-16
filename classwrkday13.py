item = input("Enter the name of the new item: ")

with open("items.txt", "a") as file:
    file.write(item + "\n")

print("\nList of items in the shop:")
with open("items.txt", "r") as file:
    for line in file:
        print(line.strip())
