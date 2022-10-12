# Lone Star Development Training - Loops
# LOOPS
# For and while are some of the Loops that you will see in Python. A for loop is used for iterating over a standard
# sequence, such as a list, tuple, dictionary, set or a string. This is more like an iterator method found in other
# object oriented programming languages and less like standard for loops in other languages.
# A while loop is going to keep looping until a condition has been met.

# Here is a list of programming languages
languages = ["Python", "C#", "Java", "Objective C", "ActionScript", "JavaScript", "TypeScript", "C++"]

# in this for loop, we are going to take each one of the items in the list and print in the order
# that they are in the list
for x in languages:
    print(x)

# Here is a trick that we can use to verify and test that by reversing the list order
print("We are going to reverse the list here and verify that the list will be printed out in reverse order")
languages.reverse()

for x in languages:
    print(x)

# Here is an example of breaking the loop and printing if a match exists
print("Example with break for C# and should print C#")
for x in languages:
    if x == "C#":
        print(x)
        break
else:
    print("Reached end of FOR")


# Here is an example of using a range parameter and it will count from 0 to 6 (but not include 6)
print("Example with a range parameter")
for x in range(6):
    print(x)

# Here is an example of using two range parameters and it will count from first param to second param
print("Example with two range parameters")
for x in range(3,6):
    print(x)

# Here is an example of using three range parameters and will count from first number to sec number by
# increment of third number
print("Example with three range parameters")
for x in range(20,30,2):
    print(x)


# Nested Loop or Inner Loop
first_names = ["Brandon", "George", "Brian", "Dave"]
last_names = ["Smith", "Jones", "Johnson", "Moore"]
print("Nested loop example")
for x in first_names:
    for y in last_names:
        print(x, y)

# For loop index example to fix name issue above
print("For loop with index example")
for x in first_names:
    index_value = first_names.index(x)
    print(x, last_names[index_value])


print("While loop example")
count1 = len(first_names)
count2 = len(last_names)
i = 0
if count1 == count2:
    while i < count1:
        print(first_names[i], last_names[i])
        i += 1



# Exercises

# Exercise 1
# Create a loop that will loop through and print individual numbers 1-12.



# Exercise 2
# Create a loop that will loop through both lists of names below and look for the name Leonard and
# if that name is found, print "Leonard is in the list" if not, print "That name doesn't exist in the list
# run them through one at a time. Bonus points for creating a method that you can pass a list into so
# you can reuse code.
print("Exercise #1")
names_exercise2a = ["Brian", "JoAnne", "Stephanie", "Joy", "Jay", "Peter", "Mike", "Jennifer"]
names_exercise2b = ["Eric", "Cory", "Leonard", "Chris", "Sherry", "Katelyn", "Caleb", "Bruce"]



# Exercise 3
# Create a loop that will loop through the numbers 2-26 in reverse and print out even numbers
print("Exercise 3")



# Exercise 4
# Create a while loop and increment 1 every loop and continue to loop through it while i < 7
print("Exercise 4")
