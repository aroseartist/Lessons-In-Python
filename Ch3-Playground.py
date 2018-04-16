# ################# PAYRATE ################# #
# Rewrite your pay computation to give the employee 1.5 times the hourly
# rate for hours worked above 40 hours
# ################# PAYRATE ################# #

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Rate of pay?")
r = float(rate)
if h > 40:
    base_owed = 40 * r
    overtime_owed = (h - 40) * (r * 1.5)
    total_owed = base_owed + overtime_owed
    print(str(total_owed))
else:
    total_owed = h * r
    print(str(total_owed))


# Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program.
hrs = input("Enter Hours:")
rate = input("Rate of pay?")
try:
    h = float(hrs)
    r = float(rate)
    if h > 40:
        base_owed = 40 * r
        overtime_owed = (h - 40) * (r * 1.5)
        total_owed = base_owed + overtime_owed
        print(str(total_owed))
    else:
        total_owed = h * r
        print(str(total_owed))
except ValueError:
    print("Ummm..that should have been a number, silly.\n")


# ################# SCORE ################# #
# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the given table
# ################# SCORE ################# #

score = input("Enter Score: ")
try:
    score_float = float(score)
    if score_float >= 0.9:
        print("A")
    elif score_float >= 0.8:
        print("B")
    elif score_float >= 0.7:
        print("C")
    elif score_float >= 0.6:
        print("D")
    elif score_float < 0.6:
        print("E")
except ValueError:
    print("Bad score\n")
