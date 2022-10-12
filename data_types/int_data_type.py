# Lone Star Development Training - Int Data Types
# INTEGERS (INTS)
# Ints are one of the most common data types that you will see in Python.
# They are numbers without decimals and can be positive, negative, or zero.
# Python also supports numbers with decimals, but they are classified as a different
# data type and will be covered later.

# Examples
my_int1 = 0
my_int2 = 55
my_int3 = -10

# Print each of the int examples above
print(my_int1)
print(my_int2)
print(my_int3)

# Now that we have introduced two data types, if you have a variable, and you're not sure what
# the type of the variable is, you can use the print() function combined with the type() function
# as shown in the example below.
variable1 = '25'
variable2 = 25

# When we print the type of variable1, we will get a statement that declares it a string.
# These are the variable types that you worked with over the last two sessions.
print(type(variable1))

# Now, print the type of variable2, and see how it differs.


# MATH WITH INTS
# As you might have guessed, ints in python allow us to do math calculations.
# Python has 7 main arithmetic operators
#   - Addition: +
#   - Subtraction: -
#   - Multiplication: *
#   - Division: /
#   - Modulus (or Remainder): %
#   - Exponentiation (exponents): **
#   - Floor Division (rounds result to nearest whole number): //

# Exercise 1
# Create a variable with your age
# Create two more variables with the ages of two other people in your life
# Calculate the combined age of you and two other people in your life (add all of your ages together)
# and store it in a variable called total_age
# Print out the results


# Exercise 2
# Create a variable with the current year
# Calculate the number of years since the first Top Gun movie was released in 1986 and store it in a
# variable called years_since_tg
# Print out the results
top_gun = 1986


# Exercise 3
# Create a variable with a rectangle side length
# Create a variable with a rectangle side width
# Calculate the area of the rectangle (length x width) and store it in a variable called area
# Print out the results


# Exercise 4
# Calculate the number of days in a quarter of a year.
# Do this once with regular division and store it in a variable called normal_division
# Do this again with floor division and store it in a variable called floor_division
# Print out the results of both types of division. What do you notice is different?


# Exercise 5
# The modulus, or remainder, operation tell you how much is left over if normal division produces a
# decimal in the answer. For example, if you do 12 / 5, you will get 2.4 because 5 goes into 12 two
# whole times, but there is still some left over. The modulus (%) operator, tells you how much is left
# over. Thus, 12 % 5, will result in 2, since the remainder is 2.
# Calculate the remainder of 133 / 11 and store it in a variable called remainder.
# Print out the results


# Exercise 6
# Exponentiation is raising one number to the power of another (think 3^2 = 9 or 3^4 = 81)
# The operation to do this in python is a double asterisk: **
# Calculate 5^3, 4^6, and 2^8 and store them in separate variables.
# Print out the results


# If you wish to use multiple operators in one math statement, you can! Python math follows the same
# order of operations as regular math.
# For example, if you have 4 variables, w, x, y, and z, and have the math statement (x-y) * (z/w),
# everything inside the parentheses will happen first and then the multiplication will happen.


