from functools import reduce
# examples with filter, map and reduce

my_list = [12, 34, 10, 31, 15]

# ----- FILTER -----------
# get odd numbers without bucle for

numbers = list(filter(lambda x: x % 2 != 0, my_list))
# print(numbers)

# with bucle for
new_list = []

for i in my_list:
    if i % 2 != 0:
        new_list.append(i)

# print(new_list)

# -------- MAP -------------
WORDS = ['alex', 'edgar', 'brian']

new_words = list(map(lambda word: word.capitalize(), WORDS))
print(new_words)

# --------- REDUCE -----------------

# sum all numbers in my_list

sum_all = reduce(lambda previous_number, actual_number: previous_number * actual_number, my_list)
print(sum_all)


