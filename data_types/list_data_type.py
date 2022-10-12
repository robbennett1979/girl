# Lone Star Development Training - List Data Type
# LISTS
# Lists are one of the data types that you will work with in Python. Lists can be created in multiple ways within
# Python or from different packages that are available.


# List Methods
# Append() - Add an element to the end of a list
# Extend() - Add all elements of a list to another list
# Insert() - Insert an item at the defined index
# Remove() - Remove an item from the list
# Pop() - Removes and returns an element at the given index
# Clear() - Removes all items from the list
# Index() - Returns the index of the first matched item
# Count() - Returns count of the number of items passed as an argument
# Sort() - Sort items in a list in ascending order
# Reverse() - Reverse the order of items in the list
# copy() - Returns a copy of the list


# Built in Functions with Lists
# reduce() - apply a particular function passed in its argument to all of the
#               list elements stores the intermediate result and only returns the final summation value
# sum() - Sums up numbers in a list
# ord() - Returns an integer representing the Unicode code point of the given Unicode character
# min() - Return minimum element of a given list
# max() - Return maximum element of a given list
# cmp() - This function returns 1 if the first list is “greater” than the second list
# all() - Returns true if all element is true or if the list is empty
# any() - Return true if any element of the list is true. if the list is empty, return false
# len() - Returns length of the list or size of the list
# enumerate() - Returns enumerate object of the list
# accumulate() - Apply a particular function passed in its argument to all of the list elements returns
#                   a list containing the intermediate results
# filter() - Tests if each element of a list is true or not
# map() - Returns a list of the results after applying the given function to each item of a given iterable
# lambda() - This function can have any number of arguments but only one expression, which is evaluated and returned



car_list = ["Chevrolet", "Ferrari", "Ford", "Lamborghini", "Porsche", "Maserati", "Toyota", "Honda"]


car_list2 = ["Saturn", "Pontiac", "Hummer"]

# Append example to add an item to the end of an existing list
print("Append Example")
print(car_list)
car_list.append("Tesla")
print(car_list)

# Insert example to add an item to the middle of an existing list
print("Insert Example")
print(car_list)
car_list.insert(2, "Subaru")
print(car_list)

# Extend example to add list to another list
print("Extend Example")
car_list.extend(car_list2)
print(car_list)

# Remove example to remove Saturn from car list
print("Remove Example")
car_list.remove("Saturn")
print(car_list)

# Index example to get index of matched item
print("Index Example")
pontiac_index = car_list.index("Pontiac")
print(pontiac_index)

# Pop example to remove an element at given index (remove Pontiac by index retrieved in last example
print("Pop Example")
print(car_list)
car_list.pop(pontiac_index)
print(car_list)

# Count example to count number of items passed in as argument
print("Count Example")
print(car_list)
lambo_count = car_list.count("Lamborghini")
print(lambo_count)
# Add another lamborghini to confirm count
car_list.append("Lamborghini")
lambo_count = car_list.count("Lamborghini")
print(car_list)
print(lambo_count)

# Sort example to sort the items in the list
print("Sort Example")
print(car_list)
car_list.sort()
print(car_list)

# Remove example to remove an item from the list (only removed one Lambo)
print("Remove Example")
print(car_list)
car_list.remove("Lamborghini")
print(car_list)

# Lambda and filter example to remove all lamborghini's in the list
print("Lambda Example")
car_list.append("Lamborghini")
print(car_list)
# Create new list by filtering every item that is not a lamborghini
final_car_list = list(filter(lambda x: (x != "Lamborghini"), car_list))
print(final_car_list)





# EXERCISES

states = ["tExas", "coloRado", "FloRida", "OhiO", "new yOrk", "ariZona", "WYoming", "NEVaDa", "FlORIDA", "ColORAdo"]
import string

# Exercise 1
# Create a for loop and iterate over each state in state_list to fix capitalization issues where the
# first letter of each word should be capitalized and store in state_list then print state list
# Hint: look into importing Pythons string module
print("Exercise 1")



# Exercise 2
# Remove any duplicate states in the state_list list that has been generated from exercise 1 and
# sort in alphabetical order
print("Exercise 2")



# Exercise 3
# Insert new state "Tennessee" in the ordered list without resorting to get in correct order
print("Exercise 3")




# Exercise 4
# Count the number of 'o' in the list, case doesn't matter.
print("Exercise 4")
count = 0

