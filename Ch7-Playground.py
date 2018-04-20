# ################# PRINT LINES ################# #
# Write a program to read through a file and print the contents of the file (line
# by line) all in upper case. Executing the program will look as follows:
# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500


file_name = input('Enter a file name: ')
try:
    handle_file = open(file_name)
except:
    print('Not a file name:', file_name)
    quit()

for line in handle_file:
    print(line.strip().upper())


# ################# SIMILAR EXAMPLE PROBLEM ################# #


fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Not a file name:', file_name)
    quit()

for line in fh:
    print(line.strip().upper())


# ################# FIND LINES ################# #
# Write a program to prompt for a file name, and then read through the file and
# look for lines of the form:
# X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the
# line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.


file_name = input('Enter a file name: ')
try:
    file = open(file_name)
except:
    print('Not a file name:', file_name)
    quit()

total = 0
count = 0
for line in file:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    numb = float(line[21:])
    count += 1
    total = numb + total

average = total / count
print('Average spam confidence:', average)


# ################# EASTER EGGS ################# #
# Sometimes when programmers get bored or want to have a bit of fun, they add a
# harmless Easter Egg to their program. Modify the program that prompts the user for
# the file name so that it prints a funny message when the user types in the exact
# file name "na na boo boo". The program should behave normally for all other files
# which exist and don't exist. Here is a sample execution of the program:
# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!


file_name = input('Enter a file name: ')
if file_name == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
else:
    try:
        handle_file = open(file_name)
    except:
        print('Not a file name:', file_name)
        quit()

for line in handle_file:
    print(line.strip().upper())
