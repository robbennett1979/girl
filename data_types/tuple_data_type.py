# Lone Star Development Training - Tuple Data Type
# TUPLE
# TUPLES are one of the data types that you will see in Python. Tuples are used
# to store data values similar to lists. A Tuple is like a
# list but it is immutable. It is also more memory efficient than lists.

# mutable object - can change their state or contents
# immutable object - can't change their state or contents

# Tuple Methods
# count() - returns the number of times a specified value occurs in a tuple
# index() - Searches the tuple for a specified value and returns the position


import sys


sample_list = ["Python", "Java", "ActionScript", "C#", "TypeScript", "JavaScript", "Kotlin", "Objective C"]
sample_tuple = ("Python", "Java", "ActionScript", "C#", "TypeScript", "JavaScript", "Kotlin", "Objective C")
sample_dictionary = {1:"Python", 2:"Java", 3:"ActionScript", 4:"C#", 5:"TypeScript", 6:"JavaScript", 7:"Kotlin", 8:"Objective C"}


# Tuple count example
print("Tuple Count Example")
tuple_count = sample_tuple.count("Python")
print(tuple_count)

# Tuple index example
print("Tuple Index Example")
tuple_index = sample_tuple.index("C#")
print(tuple_index)


# Object sizing example
print("Object Sizing List vs Tuple")
print("Sample list:")
print(sample_list)
print("Sample tuple:")
print(sample_tuple)
print("Sample dictionary")
print(sample_dictionary)

print("Bytes for the list object")
print(sys.getsizeof(sample_list))
print("Bytes for the tuple object")
print(sys.getsizeof(sample_tuple))
print("Bytes for the dictionary object")
print(sys.getsizeof(sample_dictionary))


# Object sizing with 10k int
count = 0
count_ceiling = 10000
size_list = []
size_tuple = ()
size_dictionary = {}

while count < count_ceiling:
    size_list.append(count)
    size_dictionary[count] = count
    count += 1

size_tuple = tuple(size_list)
print("Size List")
print(size_list)
print("Size Tuple")
print(size_tuple)
print("Size Dictionary")
print(size_dictionary)

print("Bytes for the size list object")
print(sys.getsizeof(size_list))
print("Bytes for the size tuple object")
print(sys.getsizeof(size_tuple))
print("Bytes for the size dictionary object")
print(sys.getsizeof(size_dictionary))


# EXERCISES
# Exercise 1
# If you uncomment the lines (84-86) below, it will throw an error. We are trying to add the string "101" to the
# 5th index of the collection. Fix as needed to get rid of error while accomplishing what is needed.

#exercise1_collection = ("Lone", "Star", "Analysis", "Python", "Training", "Collections", "Exercise")
#exercise1_collection[5] = "101"
#print(exercise1_collection)


# Why is this error throwing?

# Fix the collection so that the "101" can be added as desired and printed


# Exercise 2
# We want to create a collection of 5 different color strings (ex. "Red"). They
# will not need to be changed or have a key, but we are concerned with size. Create the best collection for this
# task and print.


# Exercise 3
# We want to make a collection for our various settings within our application. Please create a collection of the
# following settings and the reference keys should be 1-7 respectively.
# ReportViewer, ReportReader, ReportEditor, GeneralAdmin, GlobalAdmin, BillingEditor, BillingViewer


# Exercise 4
# Create a collection of all the states that you have visited. Once you have the collection created,
# sort the collection by alphabetical order and print the state that is the 4th on your list a


# Exercise 5
# Find out the size of the collection that you created in exercise #2 and print it


# Exercise 6
# Find out the size of the collection that you created in exercise #3 and print it


# Exercise 7
# Find out the size of the collection that you created in exercise #4 and print it


