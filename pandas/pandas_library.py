# Lone Star Development Training - Pandas Library
# Pandas
# Pandas is a software library that was written for Python for data analysis and manipulation. This library
# is optimized for large amounts of data for analysis and machine learning.


# DATA STRUCTURES

# DataFrame - is a 2-dimensional labeled data structure with columns of potentially different types. You can
# think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly
# used pandas object. DataFrame accepts many different kinds of input - retrieved from
# https://pandas.pydata.org/docs/user_guide/dsintro.html

# Series - is a one-dimensional labeled array capable of holding any data type (integers, strings, floating
# point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. - retrieved from
# https://pandas.pydata.org/docs/user_guide/dsintro.html


# DataFrame Attributes
# at - Access a single value for a row/column label pair
# attrs - Dictionary of global attributes of this dataset
# axes - Return a list representing the axes of the DataFrame
# columns - The column labels of the DataFrame
# dtypes - Return the dtypes in the DataFrame
# empty - Indicator whether Series/DataFrame is empty
# flags - Get the properties associated with this pandas object
# iat - Access a single value for a row/column pair by integer position
# iloc - Purely integer-location based indexing for selection by position
# index - The index (row labels) of the DataFrame
# loc - Access a group of rows and columns by label(s) or a boolean array
# ndim - Return an int representing the number of axes / array dimensions
# shape - Return a tuple representing the dimensionality of the DataFrame
# size - Return an int representing the number of elements in this object
# style - Returns a Styler object
# values - Return a Numpy representation of the DataFrame


# DataFrame Methods
# abs - Return a Series/DataFrame with absolute numeric value of each element
# add - Get Addition of dataframe and other, element-wise (binary operator add)
# add_prefix - Prefix labels with string prefix
# add_suffix - Suffix labels with string suffix
# agg - Aggregate using one or more operations over the specified axis
# aggregate - Aggregate using one or more operations over the specified axis
# align - Align two objects on their axes with the specified join method
# all - Return whether all elements are True, potentially over an axis
# any - Return whether any element is True, potentially over an axis
# append - (DEPRECATED) Append rows of other to the end of caller, returning a new object
# apply - Apply a function along an axis of the DataFrame
# applymap - Apply a function to a Dataframe elementwise
# asfreq - Convert time series to specified frequency
# asof - Return the last row(s) without any NaNs before where
# assign - Assign new columns to a DataFrame
# astype - Cast a pandas object to a specified dtype dtype
# at_time - Select values at particular time of day (e.g., 9:30AM)
# backfill - Synonym for DataFrame.fillna() with method='bfill'
# between_time - Select values between particular times of the day (e.g., 9:00-9:30 AM)
# bfill - Synonym for DataFrame.fillna() with method='bfill'
# bool - Return the bool of a single element Series or DataFrame
# boxplot - Make a box plot from DataFrame columns
# clip - Trim values at input threshold(s)
# combine - Perform column-wise combine with another DataFrame
# combine_first - Update null elements with value in the same location in other
# compare - Compare to another DataFrame and show the differences
# convert_dtypes - Convert columns to best possible dtypes using dtypes supporting pd.NA
# copy - Make a copy of this object's indices and data
# corr - Compute pairwise correlation of columns, excluding NA/null values
# corrwith - Compute pairwise correlation
# count - Count non-NA cells for each column or row
# cov - Compute pairwise covariance of columns, excluding NA/null values
# cummax - Return cumulative maximum over a DataFrame or Series axis
# cummin - Return cumulative minimum over a DataFrame or Series axis
# cumprod - Return cumulative product over a DataFrame or Series axis
# cumsum - Return cumulative sum over a DataFrame or Series axis
# describe - Generate descriptive statistics
# diff - First discrete difference of element
# div - Get Floating division of dataframe and other, element-wise (binary operator truediv)
# divide - Get Floating division of dataframe and other, element-wise (binary operator truediv)
# dot - Compute the matrix multiplication between the DataFrame and other
# drop - Drop specified labels from rows or columns
# drop_duplicates - Return DataFrame with duplicate rows removed
# droplevel - Return Series/DataFrame with requested index / column level(s) removed
# dropna - Remove missing values
# duplicated - Return boolean Series denoting duplicate rows
# eq - Get Equal to of dataframe and other, element-wise (binary operator eq)
# equals - Test whether two objects contain the same elements
# eval - Evaluate a string describing operations on DataFrame columns
# ewm - Provide exponentially weighted (EW) calculations
# expanding - Provide expanding window calculations
# explode - Transform each element of a list-like to a row, replicating index values
# ffill - Synonym for DataFrame.fillna() with method='ffill'
# fillna - Fill NA/NaN values using the specified method
# filter - Subset the dataframe rows or columns according to the specified index labels
# first - Select initial periods of time series data based on a date offset
# first_valid_index - Return index for first non-NA value or None, if no non-NA value is found
# floordiv - Get Integer division of dataframe and other, element-wise (binary operator floordiv)
# from_dict - Construct DataFrame from dict of array-like or dicts
# from_records - Convert structured or record ndarray to DataFrame
# ge - Get Greater than or equal to of dataframe and other, element-wise (binary operator ge)
# get - Get item from object for given key (ex: DataFrame column)
# groupby - Group DataFrame using a mapper or by a Series of columns
# gt - Get Greater than of dataframe and other, element-wise (binary operator gt)
# head - Return the first n rows
# hist - Make a histogram of the DataFrame's columns
# idxmax - Return index of first occurrence of maximum over requested axis
# idxmin - Return index of first occurrence of minimum over requested axis
# infer_objects - Attempt to infer better dtypes for object columns
# info - Print a concise summary of a DataFrame
# insert - Insert column into DataFrame at specified location
# interpolate - Fill NaN values using an interpolation method
# isin - Whether each element in the DataFrame is contained in values
# isna - Detect missing values
# isnull - DataFrame.isnull is an alias for DataFrame.isna
# items - Iterate over (column name, Series) pairs
# iteritems - Iterate over (column name, Series) pairs
# iterrows - Iterate over DataFrame rows as (index, Series) pairs
# itertuples - Iterate over DataFrame rows as namedtuples
# join - Join columns of another DataFrame
# keys - Get the 'info axis' (see Indexing for more)
# kurt - Return unbiased kurtosis over requested axis
# kurtosis - Return unbiased kurtosis over requested axis
# last - Select final periods of time series data based on a date offset.
# last_valid_index - Return index for last non-NA value or None, if no non-NA value is found
# le - Get Less than or equal to of dataframe and other, element-wise (binary operator le)
# lookup - (DEPRECATED) Label-based "fancy indexing" function for DataFrame
# lt - Get Less than of dataframe and other, element-wise (binary operator lt)
# mad - Return the mean absolute deviation of the values over the requested axis
# mask - Replace values where the condition is True
# max - Return the maximum of the values over the requested axis
# mean - Return the mean of the values over the requested axis
# median - Return the median of the values over the requested axis
# melt - Unpivot a DataFrame from wide to long format, optionally leaving identifiers set
# memory_usage - Return the memory usage of each column in bytes
# merge - Merge DataFrame or named Series objects with a database-style join
# min - Return the minimum of the values over the requested axis
# mod - Get Modulo of dataframe and other, element-wise (binary operator mod)
# mode - Get the mode(s) of each element along the selected axis
# mul - Get Multiplication of dataframe and other, element-wise (binary operator mul)
# multiply - Get Multiplication of dataframe and other, element-wise (binary operator mul)
# ne - Get Not equal to of dataframe and other, element-wise (binary operator ne)
# nlargest - Return the first n rows ordered by columns in descending order
# notna - Detect existing (non-missing) values
# notnull - DataFrame.notnull is an alias for DataFrame.notna
# nsmallest - Return the first n rows ordered by columns in ascending order
# nunique - Count number of distinct elements in specified axis
# pad - Synonym for DataFrame.fillna() with method='ffill'
# pct_change - Percentage change between the current and a prior element
# pipe - Apply chainable functions that expect Series or DataFrames
# pivot - Return reshaped DataFrame organized by given index / column values
# pivot_table - Create a spreadsheet-style pivot table as a DataFrame
# plot - alias of pandas.plotting._core.PlotAccessor
# pop - Return item and drop from frame
# pow - Get Exponential power of dataframe and other, element-wise (binary operator pow)
# prod - Return the product of the values over the requested axis
# product - Return the product of the values over the requested axis
# quantile - Return values at the given quantile over requested axis
# query - Query the columns of a DataFrame with a boolean expression
# radd - Get Addition of dataframe and other, element-wise (binary operator radd)
# rank - Compute numerical data ranks (1 through n) along axis
# rdiv - Get Floating division of dataframe and other, element-wise (binary operator rtruediv)
# read_csv - Read csv to DataFrame
# read_excel - Read excel file to DataFrame
# read_html - Read html tables into a list of DataFrame objects
# read_json - Convert json string to pandas object
# read_xml - Read XML document into a DataFrame object
# reindex - Conform Series/DataFrame to new index with optional filling logic
# reindex_like - Return an object with matching indices as other object
# rename - Alter axes labels
# rename_axis - Set the name of the axis for the index or columns
# reorder_levels - Rearrange index levels using input order
# replace - Replace values given in to_replace with value
# resample - Resample time-series data
# reset_index - Reset the index, or a level of it
# rfloordiv  - Get Integer division of dataframe and other, element-wise (binary operator rfloordiv)
# rmod - Get Modulo of dataframe and other, element-wise (binary operator rmod)
# rmul - Get Multiplication of dataframe and other, element-wise (binary operator rmul)
# rolling - Provide rolling window calculations
# round - Round a DataFrame to a variable number of decimal places
# rpow - Get Exponential power of dataframe and other, element-wise (binary operator rpow)
# rsub - Get Subtraction of dataframe and other, element-wise (binary operator rsub)
# rtruediv - Get Floating division of dataframe and other, element-wise (binary operator rtruediv)
# sample - Return a random sample of items from an axis of object
# select_dtypes - Return a subset of the DataFrame's columns based on the column dtypes
# sem - Return unbiased standard error of the mean over requested axis
# set_axis - Assign desired index to given axis
# set_flags - Return a new object with updated flags
# set_index - Set the DataFrame index using existing columns
# shift - Shift index by desired number of periods with an optional time freq
# skew - Return unbiased skew over requested axis
# slice_shift - (DEPRECATED) Equivalent to shift without copying data
# sort_index - Sort object by labels (along an axis)
# sort_values - Sort by the values along either axis
# sparse - alias of pandas.core.arrays.sparse.accessor.SparseFrameAccessor
# squeeze - Squeeze 1 dimensional axis objects into scalars
# stack - Stack the prescribed level(s) from columns to index
# std - Return sample standard deviation over requested axis
# sub - Get Subtraction of dataframe and other, element-wise (binary operator sub)
# subtract - Get Subtraction of dataframe and other, element-wise (binary operator sub)
# sum - Return the sum of the values over the requested axis
# swapaxes - Interchange axes and swap values axes appropriately
# swaplevel - Swap levels i and j in a MultiIndex
# tail - Return the last n rows
# take - Return the elements in the given positional indices along an axis
# to_clipboard - Copy object to the system clipboard
# to_csv - Write object to a comma-separated values (csv) file
# to_dict - Convert the DataFrame to a dictionary
# to_excel - Write object to an Excel sheet
# to_feather - Write a DataFrame to the binary Feather format
# to_gbq - Write a DataFrame to a Google BigQuery table
# to_hdf - Write the contained data to an HDF5 file using HDFStore
# to_html - Render a DataFrame as an HTML table
# to_json - Convert the object to a JSON string
# to_latex - Render object to a LaTeX tabular, longtable, or nested table
# to_markdown - Print DataFrame in Markdown-friendly format
# to_numpy - Convert the DataFrame to a NumPy array
# to_parquet - Write a DataFrame to the binary parquet format
# to_period - Convert DataFrame from DatetimeIndex to PeriodIndex
# to_pickle - Pickle (serialize) object to file
# to_records - Convert DataFrame to a NumPy record array
# to_sql - Write records stored in a DataFrame to a SQL database
# to_stata - Export DataFrame object to Stata dta format
# to_string - Render a DataFrame to a console-friendly tabular output
# to_timestamp - Cast to DatetimeIndex of timestamps, at beginning of period
# to_xarray - Return an xarray object from the pandas object
# to_xml - Render a DataFrame to an XML document
# transform - Call func on self producing a DataFrame with the same axis shape as self
# transpose - Transpose index and columns
# truediv - Get Floating division of dataframe and other, element-wise (binary operator truediv)
# truncate - Truncate a Series or DataFrame before and after some index value
# tshift - (DEPRECATED) Shift the time index, using the index's frequency if available
# tz_convert - Convert tz-aware axis to target time zone
# tz_localize - Localize tz-naive index of a Series or DataFrame to target time zone.
# unstack - Pivot a level of the (necessarily hierarchical) index labels
# update - Modify in place using non-NA values from another DataFrame
# value_counts - Return a Series containing counts of unique rows in the DataFrame
# var - Return unbiased variance over requested axis
# where - Replace values where the condition is False
# xs - Return cross-section from the Series/DataFrame


import pandas as pd
import numpy as np

# Set options so that DataFrame is not cut off in terminal
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)

# Read the csv file All Energy Statistics retrieved from kaggle.com into a Pandas DataFrame, which is a
# common data structure in Pandas.
energy_df = pd.read_csv(r'../static_files/all_energy_statistics.csv');

# Get the shape of the dataframe
print("DataFrame Shape:")
print(energy_df.shape)

# Get the description of the dataframe
print("DataFrame Describe:")
print(energy_df.describe())

# Get the information about the dataframe
print("DataFrame Information:")
print(energy_df.info())

# Lets look at first 5 rows of dataframe to see what we are dealing with
print("DataFrame Head:")
print(energy_df.head(5))

# Lets look at the last 5 rows of dataframe to see what we are looking at
print("DataFrame Tail:")
print(energy_df.tail(5))



###############################################################################################
# Create mew Series
###############################################################################################
list1 = ['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5']
list2 = [1,2,3,4,5]
list3 = [12,13,14,15,16]
np_array1 = np.array(list3)
series1 = pd.Series(data=list1)
series2 = pd.Series(data=list2)
series3 = pd.Series([6,7,8,9,10])
series4 = pd.Series(data=np_array1)
series5 = series2 + series3 + series4

df1 = pd.concat([series2, series3, series4, series5], axis=1, sort=False)
df1 = df1.set_index(series1)
print("This is a DataFrame that is built on concatenated Series:")
print(df1)


# Access value in a series we want series 2 and the third value in that series(reminder-starts on a 0 index)
series2_value3_series = series2[2]
print(series2_value3_series)

# Access values in data frame iloc (row, column)
series2_value3_df = df1.iloc[2][0]
print(series2_value3_df)

###############################################################################################
# Create new DataFrames
###############################################################################################
# Let's create an animals DataFrame (list of lists)
data1 = [['Tom', 'Cat', 'Local Cat', 'Outside', 'tcat@lone-star.com', '123-456-7890'],
                ['Bugs', 'Bunny', 'Local Rabit', 'Front Yard', 'bbunny@lone-star.com', '234-434-4444'],
                ['Tweety', 'Bird', 'Local Bird', 'Green Areas', 'tbird@lone-star.com', '123-222-2222']]

animals_df1 = pd.DataFrame(data1, columns=['First Name', 'Last Name', 'Position', 'Suite',
                                         'Email', 'Phone Number'])

print("Animals DataFrame 1")
print(animals_df1)


# Let's create another animals DataFrame
data2 = [['Jerry', 'Mouse', 'Local Mouse', 'Outside', 'jmouse@lone-star.com', '123-876-7890'],
                ['Pink', 'Panther', 'Local Panther', 'Wild', 'ppanther@lone-star.com', '234-787-4444'],
                ['Silvester', 'Cat', 'Local Cat', 'Outside', 'scat@lone-star.com', '987-987-2222']]

animals_df2 = pd.DataFrame(data2, columns=['First Name', 'Last Name', 'Position', 'Suite',
                                         'Email', 'Phone Number'])

print("Animals DataFrame 2")
print(animals_df2)

# Let concat DataFrame (Note: Tried to append, and it has a warning that it has been deprecated)
animals_concatenated_df = pd.concat([animals_df1, animals_df2], ignore_index=True)
print("Animals DataFrame 1 Concatenated with DataFrame 2")
print(animals_concatenated_df)


###############################################################################################
# REORDER COLUMNS & TRANSPOSE & SET INDEX
###############################################################################################
# Reorder the columns of the data frame
animals_column_reordered_df = animals_concatenated_df[['Position', 'Email', 'Last Name', 'First Name',
                                                       'Phone Number', 'Suite' ]]

print(animals_concatenated_df)

print("Columns reordered Example")
print(animals_column_reordered_df)


print("Transposed DataFrame")
animals_concatenated_transposed_df = animals_concatenated_df.transpose()
print(animals_concatenated_transposed_df)
print("Original object not altered")
print(animals_concatenated_df)

# Let's look at setting index
print("Set email to index")
print(animals_concatenated_df.set_index('Email'))
print(animals_concatenated_df)

# Print df after setting index NOTE: Assignment of DataFrame will change dataframe not just display differently
animals_concatenated_df.index = animals_concatenated_df['Email']
# Drop the duplicated email now that email is index
animals_concatenated_df = animals_concatenated_df.drop(columns=['Email'])
# can also be done with  animals_concatenated_df.drop(['Email'], axis=1)
print(animals_concatenated_df)

# Reset index from the email to PK approach
animals_concatenated_df = animals_concatenated_df.reset_index()
print(animals_concatenated_df)


# Exercises
# Exercise 1
# Create the following series data structures
# name - first and last name of everyone in your family (must have at least 5, if not, go outside immediate family)
# age - age of each person in your family
# relation - relation of everyone in your family (ex. sister, mom, dad)
# yrs_to_100 - create a calculated column for years that the family member needs to get to 100 (100-family member age)
# Create family_df from all the series data
# print DataFrame
print("Exercise 1")




# Exercise 2
# Create a new DataFrame from DataFrame in exercise 1 and call it family_complete_df
# Add another column to the DataFrame with their favorite color
# print DataFrame
print("Exercise 2")


