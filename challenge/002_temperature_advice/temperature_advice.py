#-----------------------------------------------------------------------------------------
# Name:          (005_day_of_the_week_activity_recommend.py)
# Purpose:      To create a daily activity recommender
#
# Author:       Harry Yang
# Created:      24-Feb-2025
#-----------------------------------------------------------------------------------------

# Ask the user to enter the current temperature (in Celsius).
# Store the temperature in a variable.
tem_input = float(input("please enter the temperature in Celsius: "))


# Use conditional statements to give advice based on the temperature.

# If the temperature is below 10°C, print: `"It's cold outside. Wear a jacket!"`
if tem_input < 10:
    print("it's cold outside! wear a jacket!")

# If the temperature is between 10°C and 25°C, print: `"It's a nice day. Wear short-sleeves!"`
elif 10 < tem_input < 25:
    print("it's a nice day! wear short sleeves!")

# If the temperature is above 25°C, print: `"It's hot outside. Stay cool!"`
elif tem_input > 25:
    print("it's hot outside! stay cool!")


