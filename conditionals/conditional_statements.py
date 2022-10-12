# Lone Star Development Training - Conditional Statements
# CONDITIONALS
# Conditionals are used everywhere in Python. Conditionals can be used for comparison, algorithms,
# math, and data manipulation.


# Conditions
# Equals = ==
# Not Equals = !=
# Less Than = <
# Greater Than = >
# Less Than or Equal To = <=
# Greater Than or Equal To = >=

# If = used for if statements and loops
# Elif = Python's approach for if the previous conditions were not true, then try this condition
# Else = Catches anything not caught by the preceding conditions

# And = Logical operator and used to combine conditional statements
# Or = Logical operator and used to combine conditional statements


# If / Elif / Else Example
print("If, Elif and Else Example")


# Compare Numbers Function
def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 == num2:
        print(f"{num1} is equal to {num2}")
    else:
        print(f"{num1} is less than {num2}")


v = 138
w = 121
x = 172
y = 148
z = 172

# Call method and pass in numbers
compare_numbers(x, y)
compare_numbers(x, z)
compare_numbers(y, x)


# Short Hand If Statement
print("Short hand if statement")
print("X is greater") if x > y else print("Y is greater")


# Short Hand If / Else Statement
print("Short hand if / else statement")
print("X is greater") if x > y else print("X = Y") if x == y else print("Y is greater")


# And Example v=138 w=121 Y=148
print("And example")
if v > w and v < y:
    print("V is between W and Y")
else:
    print("V is not between W and Y")




# EXERCISES

# Exercise 1
# Lets take in two inputs from the user and then decide if the first number that is entered is larger
# than the second number or the second number is larger than the first number. We will then want to display
# string stating that "{number1} is greater/less than {number2}". This should be completed within a function.

print("Exercise 1 - Lets compare two numbers and print out the results!")
number1 = input("Please enter the first number:")
number2 = input("Please enter the second number:")



# Exercise 2
# Lets create a guessing game for states within the US. We have a selected tuple of states 'states_list' and we will
# take an input from the user as a guess 'guessed_state', to see if that guess is a state that is within our list (one
# of the states that we are thinking about 'thinking_states').
# Possible results:
# If their guess is not a valid state, we will return "{state} is not a valid state"
# If it is, we will display "Good guess on picking {state}"
# If it is not, we will display "{state} is not a state we were thinking about"

# NOTES: allow for uppercase or lowercase input. If the state is correct, capitalization should not matter
import string

states_list = ("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
               "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
               "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
               "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
               "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
               "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
               "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming")

thinking_states = ("Florida", "Virginia", "Texas", "Tennessee", "Hawaii")


guessed_state = input("I am thinking of five different states out of the 50 states in the US. Can you "
                      "guess one of the states I am thinking about? What state do you want to guess?")




# Exercise  3
# Lets create a dice roll game. The computer will roll a single dice and then we will let the user try and
# guess what number was rolled. We will validate the input to an int between 1-6. If it is not a valid int,
# we will give the user a validation error. If it is a valid int, we will let the user know if they
# guessed the correct number, if they guessed lower than the correct number or if they guessed higher
# than the correct number.

import numpy as np
dice_roll = int(np.random.uniform(low=1, high=6, size=1).astype(int))

dice_guess = input("Please guess the number that is going to be rolled (1-6):")


