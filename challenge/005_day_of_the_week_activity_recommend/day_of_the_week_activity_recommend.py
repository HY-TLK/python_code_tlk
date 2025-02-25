#-----------------------------------------------------------------------------------------
# Name:         Day of the week activity recommend (005_day_of_the_week_activity_recommend.py)
# Purpose:      To create a daily activity recommender
#
# Author:       Harry Yang
# Created:      24-Feb-2025
#-----------------------------------------------------------------------------------------

# Ask the user to enter the current day of the week (e.g., "Monday", "Tuesday").
# Store the day in a variable.
day_input = input("please enter the current day of the week: ")
day_input = day_input.title()


#Use conditional statements to recommend an activity based on the day.

#- If the day is "Monday", print: `"Start your week with a workout!"`
if day_input == "Monday":
    print("Start your week with a workout!")

#- If the day is "Tuesday", print: `"It's a great day to read a book!"`
elif day_input == "Tuesday":
    print("It's a great day to read a book!")

#- If the day is "Wednesday", print: `"Mid-week movie night!"`
elif day_input == "Wednesday":
    print("Mid-week movie night!")

#- If the day is "Thursday", print: `"Try a new recipe!"`
elif day_input == "Thursday":
    print("Try a new recipe!")

#- If the day is "Friday", print: `"Relax and enjoy the weekend!"`
elif day_input == "Friday":
    print("Relax and enjoy the weekend")

#- If the day is "Saturday", print: `"Go for a hike!"`
elif day_input == "Saturday":
    print("Go for a hike!")

#- If the day is "Sunday", print: `"Prepare for the week ahead with some self-care."
elif day_input == "Sunday":
    print("Prepare for the week ahead with some self-care")

