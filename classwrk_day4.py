fruits = ["Apple", "Banana", "Mango"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Tea", "Coffee", "Water"]

fruits.append("Orange")
vegetables.insert(1, "Onion")
beverages.pop()

inventory = [fruits, vegetables, beverages]

print(fruits[:2])
print(vegetables[-1])

fruit_lengths = [len(fruit) for fruit in fruits]
print(fruit_lengths)

print("Water" in beverages)

first_items_tuple = (fruits[0], vegetables[0], beverages[0])
print(first_items_tuple)
