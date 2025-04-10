#-----------------------------------------------------------------------------------------
# Name:         Voting Eligibility (voting_eligibility.py)
# Purpose:      To create a system to check if you are eligible for voting
#
# Author:       Harry Yang
# Created:      24-Feb-2025
#-----------------------------------------------------------------------------------------

print("Welcome to our Voting Eligibility Checker!")
print()

# Ask the user to enter their age.
# Store the age in a variable.
age_input = int(input("please enter your age: "))


#Use conditional statements to check if the person is eligible to vote.

#If the age is 18 or older, print: `"You are eligible to vote!"`
if age_input > 18:
    print("You are eligible to vote!")

#If the age is under 18, print: `"Sorry, you are not eligible to vote yet."`
elif age_input < 18:
    print("Sorry, You are not eligible to vote!")



