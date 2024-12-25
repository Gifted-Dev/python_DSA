'''
Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190
'''

expense_list = [2200, 2350, 2600, 2130, 2190]

#  In Feb, how many dollars you spent extra compare to January?
print('Extra expense compared to jan:', expense_list[1] - expense_list[0])

# Find out your total expense in first quarter (first three months) of the year.
print('total expense in first 3 quarter of the year is', expense_list[0] + expense_list[1] + expense_list[2])

# Find out if you spent exactly 2000 dollars in any month
print(2000 in expense_list)

# June month just finished and your expense is 1980 dollar. 
# Add this item to our monthly expense list
expense_list.append(1980)
print('New expense list:', expense_list)

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expense_list[3] -= 200
print('Expense list after 200$ return on April', expense_list)

