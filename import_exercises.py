# 1. Import and test 3 of the functions from your functions exercise file. Import each function
# in a different way:
#     a. Run an interactive python session and import the module. Call the is_vowel function 
#     using the . syntax.
    import function_exercises
    function_exercises.is_vowel()

#     b. Create a file named import_exericses.py. Within this file, use from to import the 
#     calculate_tip function directly. Call this function with values you choose and print the result.
    from function_exercises import calculate_tip
    print(f'Q: How much to tip on a bill of $50.00 if we want to tip 20%? A: {calculate_tip(0.2, 50.00)}')

#     c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade
#     function and give it an alias. Test this function in your notebook.
    Done

# Make sure your code that tests the function imports is run from the same directory that your 
# functions exercise file is in.

# 2. Read about and use the itertools module from the python standard library to help you solve 
# the following problems:
#   - How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools
print('Number of combinations in a,b,c to 1,2,3')
print(len(list(itertools.product('abc', '123'))))

#   - How many different combinations are there of 2 letters from "abcd"?
letter_combinations = len(list(itertools.combinations('abcd', 2)))
print(f'There are {letter_combinations} ways to combine abcd in pairs')

#   - How many different permutations are there of 2 letters from "abcd"?
letter_permutations = len(list(itertools.permutations('abcd', 2)))
print(f'There are {letter_permutations} ways to permute abcd in pairs')

# 3. Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
# Use the load function from the json module to open this file.

  import json
  json.load(open('profiles.json')

# Your code should produce a list of dictionaries. Using this data, write some code that calculates and 
# outputs the following information:

#     - Total number of users
    numusers = len(profiles)
    print(f'Total number of users in profiles: {numusers}')

#     - Number of active users
    active_accounts = [accnt for accnt in profiles if accnt['isActive']]
    print(f'Total number of active users in profiles: {len(active_accounts)}')

#     - Number of inactive users
    inactive_users = []
    for accnt in profiles:
        if not accnt['isActive']:
            inactive_users.append(accnt)
    print(f'Total number of inactive users in profiles: {len(inactive_users)}')

#     - Grand total of balances for all users
    bal_list = []
    for accnt in profiles:
        bal_list.append(float(accnt['balance'][1:].replace(',','')))
    total_balances = sum(bal_list)
    print(f'Total balance in users: ${total_balances}')

#     - Average balance per user
    avg_balance = total_balances / numusers
    print(f'Average balance in users: ${avg_balance:.6}')

#     - User with the lowest balance
    min_bal_usr = [accnt for accnt in profiles if float(accnt['balance'][1:].replace(',','')) == max(bal_list)][0]
    print('User with minimum balance: ', min_bal_usr['name'])

#     - User with the highest balance
    max_user = {}
    for accnt in profiles:
        if float(accnt['balance'][1:].replace(',','')) == max(bal_list):
            max_user = accnt['name']
    print(f'User with maximum account balance: {max_user}')

#     - Most common favorite fruit
    all_fruits = [accnt['favoriteFruit'] for accnt in profiles]

    def fruit_counts(fruitlist):
        '''
        counts the number of each item in a list of strings and 
        returns a dictionary of the counts of each item
        '''
        fruit_counts = {}
        for fruit in fruitlist:
            if fruit not in fruit_counts.keys():
                fruit_counts[fruit] = 1
            else:
                fruit_counts[fruit] = fruit_counts[fruit] + 1
        return fruit_counts

    fruitcount_dict = fruit_counts(all_fruits)
    fave_fruit = [fruit for fruit in fruitcount_dict \
        if fruitcount_dict[fruit] == max(fruitcount_dict.values())][0]
    print(f'Most popular fruit: {fave_fruit}')

#     - Least most common favorite fruit
    least_fave_fruit = ''
    for k, v in fruitcount_dict.items():
        if v == min(fruitcount_dict.values()):
            print('least favorite fruit: ',k)

#     - Total number of unread messages for all users
    list_comp_all_unreads = sum([int(''.join([val for val in accnt['greeting'] if val.isdigit()])) for accnt in profiles])