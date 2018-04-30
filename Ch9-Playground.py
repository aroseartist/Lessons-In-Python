# ################# DICTIONARY BASICS 1 ################# #
# Write a program that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn't matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.

text_words_dict = dict()
read_words = open('words.txt', 'r')
for each_line in read_words:
    clean_line = each_line.split()
    for word in clean_line:
        lower_word = word.lower()
        if lower_word not in text_words_dict:
            text_words_dict[lower_word] = 1
        else:
            text_words_dict[lower_word] = text_words_dict[lower_word] + 1
print('\nWords in dict:', text_words_dict)
read_words.close()


# ################# DICTIONARY BASICS 1.2 ################# #

text_words_dict = dict()
read_words = open('words.txt', 'r')
for each_line in read_words:
    clean_line = each_line.split()
    for word in clean_line:
        lower_word = word.lower()
        text_words_dict[lower_word] = text_words_dict.get(lower_word, 0) + 1
print('\nWords in dict 2:', text_words_dict)
read_words.close()


# ################# DICTIONARY BASICS 2 ################# #
# Write a program that categorizes each mail message by which day of the week the
# commit was done. To do this look for lines that start with "From", then look for
# the third word and keep a running count of each of the days of the week. At the
# end of the program print out the contents of your dictionary (order does not
# matter). Sample Line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

def day_from():
    days_dict = dict()
    read_words = open('mbox-short.txt', 'r')
    for line in read_words:
        if line.startswith('From '):
            split_line = line.split()
            day = split_line[2]
            days_dict[day] = days_dict.get(day, 0) + 1
    print('\nWeekday:', days_dict)
    read_words.close()


day_from()


# ################# DICTIONARY BASICS 3 ################# #
# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the
# dictionary.

def emails():
    from_whom = dict()
    read_lines = open('mbox-short.txt', 'r')
    for line in read_lines:
        if line.startswith('From'):
            words = line.split()
            email = words[1]
            from_whom[email] = from_whom.get(email, 0) + 1
    print('\nFrom whom:', from_whom)
    read_lines.close()


emails()


# ################# DICTIONARY BASICS 4 ################# #
# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look
# through the dictionary using a maximum loop (see Section [maximumloop]) to find
# who has the most messages and print how many messages the person has.

def emails():
    from_whom = dict()
    read_lines = open('mbox-short.txt', 'r')
    for line in read_lines:
        if line.startswith('From '):
            words = line.split()
            email = words[1]
            from_whom[email] = from_whom.get(email, 0) + 1
            max_value = max(from_whom, key=lambda x: from_whom.get(x))
            min_value = min(from_whom, key=lambda x: from_whom.get(x))
    print(from_whom.values())
    print('\nEmailed most:', max_value)
    print('Emailed least:', min_value)
    read_lines.close()


emails()


# ################# DICTIONARY BASICS 5 ################# #
# This program records the domain name (instead of the address) where the message
# was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

def domain(given_file):
    domain_dict = dict()
    open_file = open(given_file, 'r')
    for line in open_file:
        if line.rstrip().startswith('From'):
            words = line.split()
            find_email = words[1]
            from_domain = find_email.split('@')
            domain_dict[from_domain[1]] = domain_dict.get(from_domain[1], 1) + 1
    print('\nWhich domain:', domain_dict)
    open_file.close()


domain('mbox-short.txt')
