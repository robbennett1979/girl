# Lone Star Development Training - Pandas Manipulation
# Pandas
# Pandas is a software library that was written for Python for data analysis and manipulation. This library
# is optimized for large amounts of data for analysis and machine learning. Data can be manipulated several
# ways within Pandas.

# NOTE: will need to install openpyxl
# Go to terminal window and type pip install openpyxl to install (needed to read from Excel)

import pandas as pd

# Set options so that DataFrame is not cut off in terminal
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)

# Read the employee files into a Pandas DataFrame, which is a common data structure in Pandas.
employee_position_df = pd.read_excel(r'../static_files/employee_position.xlsx')
employee_address_df = pd.read_excel(r'../static_files/employee_address.xlsx');
employee_insurance_df = pd.read_excel(r'../static_files/employee_insurance.xlsx');

print("Employee position DataFrame:")
print(employee_position_df)

print("Employee address DataFrame:")
print(employee_address_df)
employee_address_df = employee_address_df.drop(['First Name', 'Last Name'], axis=1)

print("Employee insurance DataFrame:")
print(employee_insurance_df)
employee_insurance_df = employee_insurance_df.drop(columns=['First Name', 'Last Name'])


# Merge the dataframes so we have one key with single row of information
print("Merged DataFrames:")
employee_df = employee_position_df.merge(employee_address_df, on='Email').merge(employee_insurance_df, on='Email')
print(employee_df)

# Approach 1
# Add a column based off of two other concatenated columns with + sign
print("Added Full Name column based on concatenation of First name column and last name column")
employee_df['Full Name'] = employee_df['First Name'].astype(str) + ' ' + employee_df['Last Name'].astype(str)
print(employee_df)

# Approach 2
# Add column based off of two other concatenated columns with cat function
print("Remove spaces in column names")
employee_df.columns = employee_df.columns.str.replace(' ', '')
print(employee_df)

employee_df['FullNameCat'] = employee_df.FirstName.str.cat(employee_df.LastName, sep=" ")
print(employee_df)


###############################################################################################
# loc & iloc
###############################################################################################
# loc & iloc to select the desired data
# loc[] Example - Used to select rows/columns based on labels
# df.loc[row start:row stop:row step, column start:column stop:column step]
# start = name of the row/column label to start with
# stop = name of the row/column label to end with
# step = number of indices to advance after each extraction
print("loc example #1 with df by row")
loc1_example_df = employee_df.loc['1':'4']
print(loc1_example_df)

print("loc example #2 with df by column")
loc2_example_df = employee_df.loc[:, 'FirstName':'Email']
print(loc2_example_df)


# iloc[] Example - Used to select rows/columns based on index
# df.iloc[row start:row stop:row step, column start:column stop:column step]
print("iloc example #1 with df by row")
iloc1_example_df = employee_df.iloc[0:3]
print(iloc1_example_df)

print("iloc example #2 with df by column")
# NOTE: notice the index value different due to the index column
iloc2_example_df = employee_df.iloc[:, 0:4]
print(iloc2_example_df)

print("iloc example with df by rows and columns")
iloc3_example_df = employee_df.iloc[1:4, 1:4]
print(iloc3_example_df)

print("Concatenated examples")
concatenated_example1_df = pd.concat([loc1_example_df, iloc1_example_df])
print(concatenated_example1_df)


###############################################################################################
# Melt
###############################################################################################
print("Melt Example")
melt_example1_df = pd.melt(employee_df)
print(melt_example1_df)


###############################################################################################
# Merging DataFrames
###############################################################################################

complete_aircraft_data = [['1983', 'Cameron', 'Viva', 'N 748CB', '77,000 cf', '8', 'parachute top', 'hot air balloon'],
                       ['1996', 'Cameron', 'A', 'N 3028J', '105,000 cf', '20', 'parachute & smart top', 'hot air balloon'],
                       ['2004', 'Brandon M Smith', '110 18S', 'N 110BS', '110,000 cf', '18', 'parachute top', 'hot air balloon'],
                       ['2012', 'Head', 'AS105', 'N 12123', '105,000 cf', '24', 'spring top', 'hot air balloon']]

complete_aircraft_df = pd.DataFrame(complete_aircraft_data, columns=['Year', 'Manufacture', 'Model',
                                                                     'Registration', 'Size', 'Gores', 'Top', 'Type'])
print("Aircraft Data - Balloon")
print(complete_aircraft_df)


retired_aircraft_data = [['N 748CB', '07/23/2002', 'No', 'Balloon', 'Would not pass annual'],
                       ['N 212J', '09/03/2012', 'No', 'Helicopter', 'Crash'],
                       ['N 3028J', '02/12/12013', 'No', 'Balloon', 'Would not pass annual']]

retired_aircraft_df = pd.DataFrame(retired_aircraft_data, columns=['Registration', 'OutOfServiceDate',
                                                                   'HoldRegistration', 'Type', 'Reason'])
print("Retired Aircraft")
print(retired_aircraft_df)


print("Aircraft Merge Examples")
print("Left Merge Example")
balloon_left_df = complete_aircraft_df.merge(retired_aircraft_df, how='left', on='Registration')
print(balloon_left_df)

print("Right Merge Example")
balloon_right_df = complete_aircraft_df.merge(retired_aircraft_df, how='right', on='Registration')
print(balloon_right_df)

print("Inner Merge Example")
balloon_inner_df = complete_aircraft_df.merge(retired_aircraft_df, how='inner', on='Registration')
print(balloon_inner_df)

print("Outer Merge Example")
balloon_outer_df = complete_aircraft_df.merge(retired_aircraft_df, how='outer', on='Registration')
print(balloon_outer_df)


###############################################################################################
# Stacked DataFrame Example
###############################################################################################
print("Stacked DataFrame")
stacked_df = complete_aircraft_df.stack()
print(stacked_df)


###############################################################################################
# EXERCISES
###############################################################################################
# Exercise 1
print(employee_df)
# Using the employee_df, figure out how to return only column with email addresses and print it
print("Exercise 1")


# Exercise 2
# using the employee_df, return rows for Matt, Joe and Michelle:
# Include first name, last name, position, email, start date, address1, address2, city, state, zip
# print results
print("Exercise 2")


# Exercise 3
# using the employee_df, return all the data for Anita
print("Exercise 3")


# Exercise 4
# using the complete_aircraft_df and retired_aircraft_df, return list of balloons that are not retired
print("Exercise 4")




