# 3. Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

# [Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/Solution/3_odd_even_numbers.py)

user_input = int(input('Enter a number: ')) # collect's user input
odd_list = [] # Adds the user input to a list

for i in range(user_input + 1): 
    if i % 2 == 1:
        odd_list.append(i)

print(odd_list)
