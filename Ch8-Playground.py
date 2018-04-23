# ################# LIST SLICES ################# #
# Write a function called chop that takes a list and modifies it, removing the
# first and last elements, and returns None. Then write a function called middle
# that takes a list and returns a new list that contains all but the first and
# last elements.

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def chop(given_list):
    try:
        return given_list[1:-1]
    except TypeError:
        return 'Not a list'


def middle(given_list):
    try:
        middle_of_list = given_list[1:-1]
        print('Middle of List:', middle_of_list)
    except TypeError:
        return 'Not a list'


chop(given_list)
middle(given_list)


# ################# GUARDING ################# #
# Figure out which line of the above program is still not properly guarded. See if
# you can construct a text file which causes the program to fail and then modify
# the program so that the line is properly guarded and test it to make sure it
# handles your new text file.


file_name = input('Enter a file name: ')
try:
    fhand = open(file_name, 'r')
    fh = fhand.readlines()
except:
    print('Not a file name:', file_name)
    quit()


def chopped(fh):
    for line in fh:
        return line[1:-1]


def middled(fh):
    for l in fh:
        line = l.rstrip()
        if line:
            split_line = line.split()
            middle_of_list = split_line[1:-1]
            if middle_of_list == []:
                continue
            print('Middle of List:', middle_of_list)


chopped(fh)
middled(fh)


# ################# LIST SLICES ################# #
# Rewrite the guardian code in the above example without two if statements.
# Instead, use a compound logical expression using the and logical operator with
# a single if statement.

file_name = input('Enter a file name:')
try:
    fh = open(file_name, 'r').readlines()
except:
    print('Not a file name:', file_name)
    quit()


def middle(fh):
    for l in fh:
        line = l.strip().split()
        if line and line[1: -1] != []:
            print('Middle of the list:', line[1: -1])


middle(fh)


# ################# LIST SORT / COMPARE ################# #
# Write a program to open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function. For each word, check
# to see if the word is already in a list. If the word is not in the list, add it to
# the list. Sort and print the resulting words in alphabetical order.

which_file = input('Which Romeo file? ')
try:
    fhandle = open(which_file, 'r').readlines()
except:
    print("File doesn't exist")


unique_words = []


def romeo(fhandle):
    for line in fhandle:
        word_list = line.split()
        for word in word_list:
            if word not in unique_words:
                unique_words.append(word)
    print(sorted(unique_words))


romeo(fhandle)


# ################# LIST SORTING / SPLIT ################# #
# Write a program to read through the mail box data and when you find line that
# starts with "From", you will split the line into words using the split function.
# We are interested in who sent the message, which is the second word on the
# From line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a
# count at the end.

which_file = input('Which file? ')
try:
    fhandle = open(which_file, 'r')
    fh = fhandle.readlines()
except:
    print('File not found.')
    quit()


def from_whom(fh):
    count = 0
    from_list = []
    for line in fh:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        words = line.split()
        count += 1
        sent_from = words[1]
        # name = sent_from.split('@')[0] # remove @ address to get names only
        # if name not in from_list:
        #     from_list.append(name)
        # receive only unique emails
        if sent_from not in from_list:
            from_list.append(sent_from)
    print(sorted(from_list))
    print('Total:', count)


from_whom(fh)


# ################# MORE SIMPLY PUT ################# #

which_file = input('Which file? ')
try:
    fhandle = open(which_file, 'r')
    fh = fhandle.readlines()
except:
    print('File not found.')
    quit()


def from_whom(fh):
    count = 0
    for line in fh:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        words = line.split()
        count += 1
        sent_from = words[1]
        print(sent_from)
    print('There were %d lines in the file with From as the first word' % count)


from_whom(fh)


# ################# MAX/MIN NUMBER LIST ################# #
# Rewrite the program that prompts the user for a list of numbers and prints out
# the maximum and minimum of the numbers at the end when the user enters "done".
# Write the program to store the numbers the user enters in a list and use the
# max() and min() functions to compute the maximum and minimum numbers after the
# loop completes.

number_list = []
while True:
    given_number = input('Enter an integer between 0 and 100: ')
    if given_number.lower() == 'done':
        break
    try:
        given_number = int(given_number)
        if given_number >= 0 and given_number <= 100:
            number_list.append(given_number)
        else:
            print('Try re-reading the directions!')
    except:
        print("That wasn't even a number at all!")


print('Max:', max(number_list))
print('Min:', min(number_list))
