# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named 
# uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', 
# etc...]
uppercase_fruits = [fruit.upper() for fruit in fruits]
uppercase_fruits

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce 
# output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.title() for fruit in fruits]
capitalized_fruits 

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
capitalized_fruits
# Doesn't capitalize two words

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels =
    [fruit for fruit in fruits 
    if len([letter for letter in fruit if letter in 'aeiou']) > 2]
fruits_with_more_than_two_vowels

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi',
# 'strawberry']
fruits_with_only_two_vowels = 
    [fruit for fruit in fruits 
    if len([letter for letter in fruit if letter in 'aeiou']) == 2]
fruits_with_only_two_vowels

# Exercise 5 - make a list that contains each fruit with more than 5 characters
[fruit for fruit in fruits if len(fruit) > 5]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
[fruit for fruit in fruits if len(fruit) == 5]

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
[fruit for fruit in fruits if len(fruit) <= 4]

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 
# 10, etc... ]
[len(fruit) for fruit in fruits]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits 
# that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
fruits_with_letter_a

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
[num for num in numbers if num % 2 == 0]

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [num for num in numbers if num % 2 == 1]
odd_numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [num for num in numbers if num > 0]
positive_numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [num for num in numbers if num < 0]
negative_numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with
# 2 or more numerals

# base 10 method:
[num for num in numbers if not (-10 < num < 10)]

# string length method
[num if (num < 0 and len(str(num)) > 2) else num for num in numbers if len(str(num)) > 1]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element 
# squared. Output is [4, 9, 16, etc...]
[num ** 2 for num in numbers]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both 
# odd and negative.
odd_negative_numbers = [num for num in numbers if (num < 0 and num % 2 == 1)]
odd_negative_numbers

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus 
# five. 
[num + 5 for num in numbers]

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list.
# *Hint* you may want to make or find a helper function that determines if a given number is prime or 
# not.
def is_prime(num):          
    absv = abs(num)
    for i in range(2, absv):
        if absv % i == 0:
            return False
            break
    else:
        return True

prime_numbers = [n for n in numbers if is_prime(n)]
prime_numbers