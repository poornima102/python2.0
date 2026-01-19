import random
import math

names_input = input("Enter names of customers (comma-separated): ")

names_list = [name.strip() for name in names_input.split(",")]
unique_names = list(set(names_list))

random.shuffle(unique_names)

winners = random.sample(unique_names, 2)

reversed_winner1 = winners[0][::-1]
reversed_winner2 = winners[1][::-1]

count_unique = len(unique_names)
rounded_sqrt = round(math.sqrt(count_unique))

print("Winner 1 (reversed):", reversed_winner1)
print("Winner 2 (reversed):", reversed_winner2)
print("Total unique participants:", count_unique)
print("Rounded square root of participants:", rounded_sqrt)
