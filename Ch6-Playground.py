# ################# STRING TRAVERSAL ################# #
# Write a while loop that starts at the last character in the string and works
# its way backwards to the first character in the string, printing each letter
# on a separate line, except backwards.


fruit = 'banana'
index = len(fruit) - 1
while index >= 0:
    print(fruit[index])
    index -= 1


# ################# COUNT FUNCTIONS ################# #
# Encapsulate this code in a function named count, and generalize it so that it
# accepts the string and the letter as arguments.


def count(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
            print(count)
        else:
            print('No such letter')


# ################# COUNT . NOTATION ################# #
# There is a string method called count that is similar to the function in the
# previous exercise. Write an invocation that counts the number of times the
# letter a occurs in "banana".


word = 'bAnana'
word.lower().count('a')


# ################# SLICING ################# #
# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into
# a floating point number.


str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
extract = str[colon+1:]
print(float(extract))


# Similarly: Write code using find() and string slicing to extract the number at
# the end of the line below. Convert the extracted value to a floating point
# number and print it out.


text = "X-DSPAM-Confidence:    0.8475"
find_numb = text.find('0')
extract_numb = text[find_numb+1:]
print(float(extract_numb))
