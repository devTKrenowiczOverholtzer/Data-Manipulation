#--------------------------------METADATA------------------------------------
# TORI OVERHOLTZER
# CS404: AI Data Analysis for Manufacturing , Agriculture and Energy
# DESCRIPTION: Data Manipulation of wine quality based on physicochemical properties (Agricultural Application)
# ENVIORMENT: Python 3, Pandas

#Python line comments denoted by <#>

#--------------------------------LIBRARIES-----------------------------------
# import <libraryname> as <alias>
import pandas as pd

# Read dataset into the dataframe variable "wine_df"
# dataframes: how things in Pandas are represented 
wine_df = pd.read_csv("winequality-white.csv", sep=";")
#using pandas function read csv using separator argument 
#csv doesn't use standard seperators (uses ; instead of standard , separators)


# Get overview of Data
# Use function head
# Gives summary of dataset, first 5 rows
# If using googlecolab print statment unnecessary
print(wine_df.head())


# Printing Column Methods Useful for Large CSV files
# Print the Columns (method 1)
# Displays features of dataset
# using pandas dataframe index object returned
print("Columns Index")
print(wine_df.columns)

# Print the Columns (method 2)
# returns columns as Python list object
# may want python list object instead of pandas index object depending on what is used or working outside of pandas
# wrapped list function will convert index into a list
print("Columns as a List")
print(list(wine_df.columns))


# Describe the Data
# Describe function on the dataframe
# Give Columns, Count, Mean, Standard Deviation, Max Value, Min Value, Quartile
print("Describe the Data")
print(wine_df.describe())


# Indexing
# Indexing Data
# Take dataframe and generate useful subsets of dataframes
# Filtering Data
# Return a series object (Filtered View of Pandas Dataframe)
# Return a series with only the "quality" column of dataset
quality_series = wine_df['quality']
# quality_series user named variable, using dataframe bracket notation ['<column name>']
print("Quality Series")
print(quality_series)

# multiple columns
# can convert this into a list and do multiple column names
# quality_series = wine_df['<column name, column name list>']


# Indexing
# return a list with the quality column dataset
# grabbing the values out of the series <.values> and converting it to a python list <.tolist()>
quality_list = wine_df['quality'].values.tolist()
print("Quality List")
print(quality_list)
# list python format


# General Note: If feeding directly from Pandas to an AI model , the libraries using like psykitlearn, carras, pytorch are going to be able to handle pandas dataframe objects, but if using a more custom implementation or library that doesnt support this useful to get them into a different format

# Using .loc
# Method indexing dataframe
# Label based
# Can select different rows and columns
# Columns are generally selected by label
# Can pass conditions into location
# When using row and column indexers order is row x column if having to specify both
# Are different situations in which pass either row or column, don't have to specify both
# If slicing on .loc it is end inclusive
# Get everything in quality column
print("Entire Quality Column")
print(wine_df.loc[:, "quality"])
# notation df.loc[row, column]
# using normal slicing notation [:]
# : substituion for everything
# Want all rows, and just the quality column
# Series Object

# Using .iloc
# If slicing on .iloc it is end exclusive

# Get first Quality Value
print("First Quality Value")
print(wine_df.loc[0, "quality"])
# first row which is index 0

# Slice
# Get Multiple values for each index
# Going to Slice
print("1-5 (first and up to fifth) indexed quality value")
print(wine_df.loc[0:5, "quality"])
# end inclusive so it gives 6 values index 0-5

#--------------------------------RESOURCES AND REFERENCES-------------------
# DATASET: P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.Modeling wine preferences by data mining from physicochemical properties.In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236
# CODE CONTRIBUTOR: Mary Everett, University of Idaho PHD
