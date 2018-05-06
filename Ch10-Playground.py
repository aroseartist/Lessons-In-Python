# ################# TUPLES 1 ################# #
# Revise a previous program as follows: Read and parse the "From" lines and pull out
# the addresses from the line. Count the number of messages from each person using
# a dictionary. After all the data has been read, print the person with the most
# commits by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most commits.


get_file = input('Enter file name: ')
try:
    fhandle = open(get_file, 'r')
    read_file = fhandle.readlines()
except:
    print('File not found!')
    quit()


def parse_lines(read_file):
    email_dict = dict()
    for line in read_file:
        if line.startswith('From: '):
            words = line.lower().split()
            address = words[1]
            email_dict[address] = email_dict.get(address, 0) + 1

    count_email = list()
    for k, v in list(email_dict.items()):
        count_email.append((v, k))

    count_email.sort(reverse=True)
    most_sent = max(count_email)
    print(most_sent[1], most_sent[0])


parse_lines(read_file)


# ################# TUPLES 2 ################# #
# This program counts the distribution of the hour of the day for each of the
# messages. You can pull the hour from the "From" line by finding the time string
# and then splitting that string into parts using the colon character. Once you
# have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour.

file_wanted = input('Enter path and file name: ')
try:
    fhandle = open(file_wanted, 'r')
    read_file = fhandle.readlines()
except:
    print('Not found')
    quit()

time_dict = dict()
lst = list()

for line in read_file:
    if line.startswith('From '):
        find_time = line.split()
        time = find_time[5]
        find_each = time.split(':')
        find_time = find_each[0]
        time_dict[find_time] = time_dict.get(find_time, 0) + 1

for k, v in list(time_dict.items()):
    lst.append((k, v))
    lst = sorted(lst)

for k, v in lst:
    print(k, v)


# ################# TUPLES 3 ################# #
# Write a program that reads a file and prints the letters in decreasing order of
# frequency. Your program should convert all the input to lower case and only count
# the letters a-z. Your program should not count spaces, digits, punctuation, or
# anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages.

ask_for_file = input('Enter path / file: ')
try:
    open_file = open(ask_for_file, 'r')
    fhandle = open_file.readlines()
except:
    print('Not found')
    quit()


def letter_freq():
    valids = []
    letter_dict = dict()
    letter_list = list()

    for line in fhandle:
        lower = line.lower()
        for character in lower:
            if character.isalpha():
                valids.append(character)
        letters_only = ''.join(valids)

    for each_letter in letters_only:
        if each_letter not in letter_dict:
            letter_dict[each_letter] = letter_dict.get(each_letter, 0)
        else:
            letter_dict[each_letter] = letter_dict.get(each_letter) + 1

    for k, v in list(letter_dict.items()):
        letter_list.append((v, k))
        letter_list.sort(reverse=True)

    for each_letter in letter_list:
        print(each_letter[1])


letter_freq()
