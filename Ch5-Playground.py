# ################# NUMBER LOOP ################# #
# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using
# try and except and print an error message and skip to the next number.
# ################# NUMBER LOOP ################# #

total = 0
count = 0
average = 0
while True:
    number = input('Enter a number: ')
    if number.lower() == 'done':
        break
    try:
        total += float(number)
        count += 1
        average = total / count
    except ValueError:
        print ("Invalid input")
print ('\nTotal:', total, '\nCount:', count, '\nAverage:', average)
print('All done\n')

# ################# MAX / MIN ################# #
# Write another program that prompts for a list of numbers as above and at the
# end prints out both the maximum and minimum of the numbers instead of the average.
# ################# MAX / MIN ################# #

min = None
max = None
while True:
    number = input('Enter a number: ')
    if number.lower() == 'done':
        break
    try:
        numnum = int(number)
        if max is None or numnum > max:
            max = numnum
        if min is None or numnum < min:
            min = numnum
    except ValueError:
        print ("Invalid input")
        continue
print ('Maximum is', max)
print('Minimum is', min)
