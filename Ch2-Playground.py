print(1 + 2 * 3 - 8 / 4)

# "print your first words" assignment
print("This is my python3 printed string screenshot!")


# get the user name and welcome them
name = input("Enter your name:\n")
print("Hello " + name + "\n")


# ################# PAYRATE ################# #
# find out the pay owed to the user based on input and rate
# ################# PAYRATE ################# #
hours = input("Hours worked?\n")
rate = input("Rate of pay?\n")
owed = int(hours) * int(rate)
print("Pay: " + str(owed) + "\n")


# For each of the following expressions, write the value of the
# expression and the type (of the value of the expression).
width = 17
height = 12.0
width//2
print(type(width))
width/2.0
print(type(width))
height/3
print(type(height))
plus_times = 1 + 2 * 5
print(type(plus_times))


# ################# F to C ################# #
# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.
# ################# F to C ################# #

get_celsius = input("\nWhat temperature is it in Celsius?\n")
try:
    fahr = float(get_celsius)
    given_celsius_rounded = "%.2f" % ((fahr - 32.0) * 5.0 / 9.0)
    print("That is", str(given_celsius_rounded), "in Fahrenheit\n")
except ValueError:
    print("Ummm..that should have been a number, silly.\n")
