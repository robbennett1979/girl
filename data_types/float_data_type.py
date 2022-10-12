# Lone Star Development Training - Float Data Type
# FLOATING-POINT Numbers
# Floats are one of the common data types that you will see in Python. The float type in Python designates a floating
# point number. Float values are designtated with a decimal point. It is possible to specify scientific
# notation with an e or E followed by a positive or negative integer. Python float values are represented
# as 64-bit 'Double Precision' values as per the IEEE754 standard.
# Maximum value of a float is 1.8 x 10^308. Anything over that will be indicated by string inf

# Imports
import math
from decimal import Decimal as D


# Should display value 1.79e308
print(1.79e308)
# Should display inf (infinity) due to maximum capacity or limitations of the computer
print(1.8e308)

float1 = 1.957
print(type(float1))
print(float1)


# Limitation Example 1
# Python.org website (2001-2021). Representation error. Retrieved July 1, 2022 from
# https://docs.python.org/3.6/tutorial/floatingpoint.html
# This section explains the “0.1” example in detail, and shows how you can perform an exact analysis
# of cases like this yourself. Basic familiarity with binary floating-point representation is assumed.
# Representation error refers to the fact that some (most, actually) decimal fractions cannot be
# represented exactly as binary (base 2) fractions. This is the chief reason why Python
# (or Perl, C, C++, Java, Fortran, and many others) often won’t display the exact decimal number you expect.
# Why is that? 1/10 is not exactly representable as a binary fraction. Almost all machines today
# (November 2000) use IEEE-754 floating point arithmetic, and almost all platforms map Python
# floats to IEEE-754 “double precision”. 754 doubles contain 53 bits of precision, so on input
# the computer strives to convert 0.1 to the closest fraction it can of the form J/2**N where
# J is an integer containing exactly 53 bits.
float2 = 0.1
float3 = 0.1
float4 = 0.1
float_limitation1 = float2 + float3 + float4
print("Limitation Example:")
print(float2)
print(float_limitation1)
print(type(float_limitation1))


# Bool number comparison
bool_result1 = .3 == float2 + float3 + float4
print(bool_result1)


# Decimal Example
decimal1 = D('0.1')
decimal2 = D('0.1')
decimal3 = D('0.1')

decimal_result1 = decimal1 + decimal2 + decimal3
print(decimal_result1)
print(type(decimal_result1))

bool_result2 = (D('0.3') == decimal1 + decimal2 + decimal3)
print(bool_result2)

# Complex Numbers
z1 = 2 + 3j
z2 = 4 + 5j
print("Complex Numbers Example:")
print(z1 + z2)
print(z1 * z2)



# Math Functions
# math.sqrt(x) = Returns square root of x
# math.pow(x,y) = Returns x raised to the power of y
# math.log2(x) = Returns the base 2 lagarithm of x
# math.log10(x) = Returns the base 10 lagarithm of x
# math.exp(x) = Returns e raised to the power of x, where e = 2.718281
# math.trunc(x) = Return x with the fractional part removed, leaving the int part
# math.remainder(x,y) = Return the remainder of x with respect to y
# math.isnan(x) = Return true if x is NaN(not a number)
# math.isfinite(x) = Return true if x is neither an infinity nor a NaN
# math.isclose(x,y) = Returns true if x and y are close to each other(based on absolute and relative tol)
# math.gcd(*int) = Returns greatest common divisor
# math.floor(x) = Returns the floor of x
# math.ceil(x) = Returns the ceiling of x

# Constants
# math.pi = 3.141592.......
# math.2 = 2.718281........
# math.tau = 6.283185...... circle constant equal to 2pi, the ratio of a circles circumference to its radious
# math.inf = a floating point positive infinity
# math.nan = a floating point not a number

# Also included trigonometric functions, angular conversion, hyperbolic functions, special functions, etc

# Math Square Root Example
print("Square Root Example")
sqrt_result1 = math.sqrt(9)
print(sqrt_result1)

# Math is Close Example
print("Math Close Example")
bool_result2 = math.isclose(.3, float2 + float3 + float4)
print(bool_result2)

# Math Ceiling and Floor Example
print("Ceiling and Floor Example")
ceiling_number = 3.14
ceiling_result1 = math.ceil(ceiling_number)
print(ceiling_result1)
floor_result1 = math.floor(ceiling_number)
print(floor_result1)




print("Exercises:")

# Exercise 1
# Let's go ahead and add float_ex1a and float_ex1b together and store in
# a variable named float_result1 and then print. The answer should be equal to 2.2
print("Exercise 1:")
float_ex1a= '1.1'
float_ex1b = 1.1



# Exercise 2
# Look at the example below and reference the decimal 1, 2 and 3 brom up above and figure out why
# the bool_result2 is false and fix it so that it is true as we want to recognize that 0.3 = .1 + .1 + .1
print("Exercise 2:")
float_result2 = 0.3
bool_result2 = (float_result2 == decimal1 + decimal2 + decimal3)
print(bool_result2)



# Exercise 3
# We want to use the math constant from up above in the Math Functions Constant section and
# multiply pi * 5 and return result in a float_result3 variable. We then want to return the
# float_result3 value rounded to the floor in float_result3_floor and then also return a value with
# that float_result3 rounded up to the ceiling in float_result3_ceiling and then print all the results
# and print that value
print("Exercise 3:")



# Exercise 4
# Use the float_ex4 below and use one of the math functions up above so that you can
# return only the number 3 in a variable float_result4 and print that out.
print("Exercise 4:")
float_ex4 = math.pi
print(float_ex4)


