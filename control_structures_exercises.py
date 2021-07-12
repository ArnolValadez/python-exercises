# 1. Conditional Basics
#    a. prompt the user for a day of the week, print out whether the day is Monday or not
        day_of_the_week = input('Please input a day of the week: ')
        day_of_week
        if day_of_the_week.lower() == 'monday':
            print ("Today is Monday")
        else:
            print ("Today is not Monday") 

        # Other response
        day_of_week = input('Please input a day of week: ')
        if day_of_week.lower() == 'monday':
            print('lasagna')
        else:
            print('not monday')

#    b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
        if day_of_the_week.lower().startswith('s'):
            print('weekend')
        else:
            print('weekday')

        # John's Response:




#    c. create variables and make up values for
#        - the number of hours worked in one week
            hours_worked_in_week = 45
#        - the hourly rate
            hourly_rate = 15
#        - how much the week's paycheck will be
#    write the python code that calculates the weekly paycheck. You get paid time and a half if you work 
#    more than 40 hours
        if hours_worked_in_week <= 40:
            paycheck = hours_worked_in_week * hourly_rate
        else: 
            paycheck = hourly_rate * (((hours_worked_in_week - 40) * 1.5) + 40)
        print (paycheck)

        #Edited
        if hours_worked_in_week <=40:
            paycheck = hours_worked_in_week * hourly_rate
        else:
            print('made it here')
            paycheck = hourly_rate * (((hours_worked_in_week - 40) * 1.5) + 40)
        print(paycheck)

# 2. Loop Basics
#    a. While
#        - Create an integer variable i with a value of 5.
#        - Create a while loop that runs so long as i is less than or equal to 15
#        - Each loop iteration, output the current value of i, then increment i by one.
#        - Your output should look like this:

            i = 5
            while i < 16:
                print(i)
                i += 1
#               i = i + 1
#           not gonna happen: i++

#        - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number
#        with a new line.
        i = 0
        while i < 101:
            print(i)
            i += 2
#        - Alter your loop to count backwards by 5's from 100 to -10.
        i = 100
        while i >= -10:
            print(i)
            i += -5

        # John's response:



#        - Create a while loop that starts at 2, and displays the number squared on each line while the 
#        number is less than 1,000,000. Output should equal:
        i = 2
        while i < 1_000_000:
            print(i)
            i **= 2

        # John's response

        

#        - Write a loop that uses print to create the output shown below.
        i = 100
        while i >= 5:
            print(i)
            i += -5

#    b. For Loops
#        i. Write some code that prompts the user for a number, then shows a multiplication table up through 
#        10 for that number.
#        For example, if the user enters 7, your program should output:
        proposed_num = input('Please insert a positive integer ')
        proposed_num = int(proposed_num)
        for n in range(1,11):
            print(f'{proposed_num} X {n} = {proposed_num * n}')

#        ii. Create a for loop that uses print to create the output shown below.
        for n in range(1,10):
            print(str(n) * n)

#    c. break and continue
#         i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to 
#         continue prompting the user if they enter invalid input. (Hint: use the isdigit method on 
#         strings to determine this). Use a loop and the continue statement to output all the odd numbers 
#         between 1 and 50, except for the number the user entered.
#         - Your output should look like this:
        while True:
            posited_num = input('Please insert an odd number between 1 and 50: ')
            if posited_num.isdigit():
                if int(posited_num) % 2 == 1 and int(posited_num) <= 50:
                    break
        posited_num = 27

        posited_num = int(posited_num)
        for num in range(1, 50, 2):
            if num == posited_num:
                print('Yikes! Skipping number: ', num)
            else:
                print('Here is an odd number: ', num)

#   Other possible code
#           posited_num = input('Please insert a digit that is odd and under 50')
#           while not posited_num.isdigit():
#           posited_num = input('Your input did not meet the qualifications. Please enter a digit that is odd and under 50')
#           if posited_num.isdigit():
#               while int(posited_num) % 2 ==0 or int(posited_num) >50:
#                   posited_num = 'try again'
#                   break       

#    d. The input function can be used to prompt for input and use that input in your python code. 
#     Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#     (Hints: first make sure that the value the user entered is a valid number, also note that the 
#     input function returns a string, so you'll need to convert this to a numeric type.)
        while True:
            posited_num = input('Please insert a positive integer: ')
            if posited_num.isdigit():
                if int(posited_num) > 0:
                    break
        posited_num = int(posited_num)
        for num in range(0, posited_num + 1):
            print(num)

#    e. Write a program that prompts the user for a positive integer. Next write a loop that prints 
#     out the numbers from the number the user entered down to 1.
        while True:
            posited_num = input('Please insert a positive integer: ')
            if posited_num.isdigit():
                if int(posited_num) > 0:
                    break
        posited_num = int(posited_num)
        for num in range(posited_num, 0, -1):
            print(num)

# 3. Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
#   - Write a program that prints the numbers from 1 to 100.
#   - For multiples of three print "Fizz" instead of the number
#   - For the multiples of five print "Buzz".
#   - For numbers which are multiples of both three and five print "FizzBuzz".  
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 4. Display a table of powers.
#   - Prompt the user to enter an integer.
#   - Display a table of squares and cubes from 1 to the value entered.
#   - Ask if the user wants to continue.
#   - Assume that the user will enter valid data.
#   - Only continue if the user agrees to.
#   - Example Output
#   - Bonus: Research python's format string specifiers to align the table
while True:
    posited_num = input('Please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
proceed = input('Do you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for i in range(1, posited_num + 1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f'{i: 6} | {i_squared: 7} | {i_cubed: 5}')

# 5. Convert given number grades into letter grades.
#    - Prompt the user for a numerical grade from 0 to 100.
#    - Display the corresponding letter grade.
#    - Prompt the user to continue.
#    - Assume that the user will enter valid integers for the grades.
#    - The application should only continue if the user agrees to.
#    - Grade Ranges:
#        - A : 100 - 88
#        - B : 87 - 80
#        - C : 79 - 67
#        - D : 66 - 60
#        - F : 59 - 0
#    - Bonus
#        - Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
while True:
    user_number = input("Please enter a numerical between 0 and 100")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number < 0 or user_number > 100: 
            continue
        break

grade = 63

if 60 < grade < 67:
    print('yup')

if grade in range(60):
    grade = 'F'
elif grade in range(60,67):
    grade = 'D'
elif grade in range(67,80):
    grade = 'C'
elif grade in range(80,88):
    grade = 'B'
else:
    grade = 'A'

# 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each 
# dictionary in the list should have the keys title, author, and genre. Loop through the list and print
# out information about each book.
#     a. Prompt the user to enter a genre, then loop through your books list and print out the titles of 
#        all the books in that genre.
bookshelf = [
    {'title': 'Annihilation',
    'author': 'Jeff Vandermeer',
    'genre': 'Science Fiction'},
    {'title': 'Octopus Pie',
    'author': 'Maredeth Gran',
    'genre': 'Comic'},
    {'title': 'Cabin At the End of the World',
    'author': 'Paul Tremblay',
    'genre': 'Horror'},
    {'title': 'Severance',
    'author': 'Ling Ma',
    'genre': 'Science Fiction'},
]

for book in bookshelf:
    [print(key,': ', book[key]) for key in book]
    print('--------')

picked_genre = input('Please pick a genre and I will return the titles we have on the shelf: ')

matches= []
for book in bookshelf:
    if book['genre'].lower() == picked_genre.lower():
        matches.append(book['title'])
if matches == []:
    print("No books in that genre right now.  Please check back later!")
else:
    print(f'I have the following titles in the genre {picked_genre}:')
    [print(match) for match in matches]