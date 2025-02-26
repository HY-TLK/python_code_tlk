#---------------------------------------------------------------
# Name:         School Grading System (001_school_grading_system.py)
# Purpose:      To create a system for school grading
#
# Author:       Harry Yang
# Created:      24-Feb-2025
#---------------------------------------------------------------

# Welcome to School Grading System
print("Welcome to School Grading System!")

# Use a loop to make sure the score is in the right range
while True:

# Ask the user to enter their score
# Store the score in a variable
    user_score = float(input("Please enter your score in numbers from 1 to 100: "))

# Use conditional statements to print the grade based on the score
# If the score is greater than or equal to 90, print: "Grade: A"
    if 90 <= user_score <= 100 :
        print("Grade:A")
        print("Thank you for grading")
        break
# If the score is between 80 and 89, print: "Grade: B"
    elif 80 <= user_score <=89 :
        print("Grade:B")
        print("Thank you for grading")
        break
# If the score is between 70 and 79, print: "Grade: C"
    elif 70 <= user_score <= 79 :
        print("Grade:C")
        print("Thank you for grading")
        break
# If the score is between 60 and 69, print: "Grade: D"
    elif 60 <= user_score <= 69 :
        print("Grade:D")
        print("Thank you for grading")
        break
# If the score is below 60, print: "Grade: E"
    elif 0 < user_score < 60:
        print("Grade:E")
        print("Thank you for grading")
        break
# If the score is greater than 100 or smaller than 0 , it will show "ERROR"
    else:
        print("ERROR")
        print("Please try again")
