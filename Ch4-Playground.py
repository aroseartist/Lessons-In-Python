# ################# PAYRATE ################# #
# Rewrite your pay computation with time-and-a-half for overtime and create a
# function called computepay which takes two parameters (hours and rate).
# ################# PAYRATE ################# #

hrs = input("Enter Hours:")
rate = input("Rate of pay?")


def computepay(hrs, rate):
    try:
        h = float(hrs)
        r = float(rate)
        if h > 40:
            base_owed = 40 * r
            overtime_owed = (h - 40) * (r * 1.5)
            total_owed = base_owed + overtime_owed
            # print(str(total_owed))
            return str(total_owed)
        else:
            total_owed = h * r
            # print(str(total_owed))
            return str(total_owed)
    except ValueError:
        # print("Ummm..that should have been a number, silly.\n")
        return "Ummm..that should have been a number, silly.\n"


# (computepay(hrs, rate)
final_pay_amount = computepay(hrs, rate)
print(final_pay_amount, "owed")


# ################# SCORE ################# #
# Rewrite the grade program from the previous chapter using a function called
# computegrade that takes a score as its parameter and returns a grade as a string.
# ################# SCORE ################# #

score = input("Enter Score: ")


def computegrade(score):
    try:
        score_float = float(score)
        if score_float >= 0.9 and score_float <= 1.0:
            # print("A")
            return("A")
        elif score_float >= 0.8 and score_float < 0.9:
            # print("B")
            return("B")
        elif score_float >= 0.7 and score_float < 0.8:
            # print("C")
            return("C")
        elif score_float >= 0.6 and score_float < 0.7:
            # print("D")
            return("D")
        elif score_float < 0.6:
            # print("E")
            return("E")
        elif score_float > 1.0:
            # print("Too big! Between 0.0 and 1.0")
            return "Too big. Must be between 0.0 and 1.0 -- try again!"
    except ValueError:
        # print("Bad score")
        return "Bad score. Must be a number between 0.0 and 1.0 -- try again!"


final_score = computegrade(score)
print("Final score:", final_score)
