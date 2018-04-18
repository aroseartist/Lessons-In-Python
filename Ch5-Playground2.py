# ################# NUMBER LOOP ################# #
# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using
# try and except and print an error message and skip to the next number.
# ################# NUMBER LOOP ################# #

total = 0
count = 0
while True:
    given_number = input('Enter a number:\n')
    if given_number.lower() == 'done':
        break
    try:
        total += float(given_number)
        count += 1
    except ValueError:
        print('Invalid input')
average = total/count
print('\nTotal:', total)
print('Count:', count)
print('Average:\n', average)


# ################# NUMBER LOOP - MUTATING LISTS ################# #
# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using
# try and except and print an error message and skip to the next number.
# ################# NUMBER LOOP - MUTATING LISTS ################# #

input_list = list()
while True:
    input_numb = input('Enter a number: ')
    if input_numb.lower() == 'done':
        print('moving on...')
        break
    input_float = float(input_numb)
    input_list.append(input_float)

average = sum(input_list) / len(input_list)
print('Average:', average)


# ################# MAX / MIN ################# #
# Write another program that prompts for a list of numbers as above and at the
# end prints out both the maximum and minimum of the numbers instead of the average.
# ################# MAX / MIN ################# #

min = None
max = None
while True:
    given_number = input('\nEnter a number:\n')
    if given_number.lower() == 'done':
        break
    try:
        given_number_float = float(given_number)
        if max is None or given_number_float > max:
            max = given_number_float
        if min is None or given_number_float < min:
            min = given_number_float
    except ValueError:
        print('Invalid input')
print('\nMinimum:\n', min)
print('Maximum:\n', max)
