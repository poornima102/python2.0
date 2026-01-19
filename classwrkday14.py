import random
import math

names_input = input("Enter the names of invited guests (comma-separated): ")

names_list = [name.strip() for name in names_input.split(",")]
unique_names = list(set(names_list))

chosen_name = random.choice(unique_names)
reversed_name = chosen_name[::-1]

count_unique = len(unique_names)
rounded_sqrt = round(math.sqrt(count_unique))

print("Randomly selected name:", chosen_name)
print("Reversed name:", reversed_name)
print("Total number of unique names:", count_unique)
print("Rounded square root of unique names:", rounded_sqrt)
