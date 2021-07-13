# 1. Define a function named is_two. It should accept one input and return True if the passed input 
# is either the number or the string 2, False otherwise.
def is_two(x):
    return x == 2 or x == "2"

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False 
# otherwise.
def is_vowel(string):
    if type(string) == str:
        result = string.lower() in ["a", "e", "i", "o", "u"]
        return result
    else:
        return False

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant,
# False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(string):
    if type(string) == str:
        is_only_letters = string.isalpha()
        return is_only_letters and not is_vowel(string)
    else:
        return False

# 4. Define a function that accepts a string that is a word. The function should capitalize the 
# first letter of the word if the word starts with a consonant.
def capitalize_starting_consonant(string):
    if type(string) != str:
        return False
    
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    
    return string

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 
# and 1) and the bill total, and return the amount to tip.
def calculate_tip(bill, tip_percentage = 0.2):
    if tip_percentage < 0 or tip_percentage > 1:
        return "The tip percentage must be a value between 0 and 1"
    
    tip_amount = tip_percentage * bill
    return tip_amount

# 6. Define a function named apply_discount. It should accept a original price, and a discount 
# percentage, and return the price after the discount is applied.
def apply_discount(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount

# 7. Define a function named handle_commas. It should accept a string that is a number that contains 
# commas in it as input, and return a number as output.
def handle_commas(string):
    if type(string) != str:
        return "Input must be a string."

    return float(string.replace(",", ""))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade 
# associated with that number (A-F).
def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Input must be a number"

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the 
# vowels removed.
def remove_vowels(string):
    if type(string) != str:
        return False
    
    output = ""
    for letter in string:
        if not is_vowel(letter):
            output += letter
    return output


# 10. Define a function named normalize_name. It should accept a string and return a valid python 
# identifier, that is:
#     - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
#     - for example:
#         - Name will become name
#         - First Name will become first_name
#         - % Completed will become completed

import re

def normalize_name(s):

    # Replace blank spaces with underscores and remove invalid characters
    s = s.replace(' ','_')
    s = re.sub('[^0-9a-zA-Z_]', '', s)
   
    # Remove leading characters until we find a letter then lowercase everything
    s = re.sub('^[^a-zA-Z]+', '', s)
    s = s.lower()
    return s
# Send the function a string of characters to test the code
s = normalize_name(' % First Name')
print(s)


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that 
# is the cumulative sum of the numbers in the list.
#     - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#     - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(numbers):
    output = []
    
    # Enumerate gives us the index as well as the element at that index
    for i, number in enumerate(numbers):
        
        # Calculate the sum of the list up to and including the given index
        sum_so_far = sum(numbers[:i + 1])
        
        # append the sum_so_far to the output list
        output.append(sum_so_far)
    
    return output