#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 6, 2025
# This program converts the inputted celsius
# from the user to fahrenheit.


# Define the fahrenheit function.
def fahrenheit():
    # Get the temperature in celsius from the user as a string.
    user_celsius_str = input("\nEnter the temperature (°C): ")

    # Try to check the validity of the user input.
    try:
        # Attempt to convert the entered string into a float.
        user_celsius_float = float(user_celsius_str)
        # Convert the celsius float to fahrenheit with the conversion formula.
        fahrenheit_conversion = (9 / 5) * user_celsius_float + 32
        # Display the fahrenheit result to the user.
        print(f"\n{user_celsius_float}°C is equal to {fahrenheit_conversion}°F.")

    # Runs if float() could not convert the user's string
    # input into a float.
    except ValueError:
        # Display to the user that they did not enter a valid integer.
        print(f"\n{user_celsius_str} is not a valid number.")


# Define the main function.
def main():
    # Call the fahrenheit function to execute the conversion process.
    fahrenheit()


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
