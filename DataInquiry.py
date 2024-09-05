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


#--------------------------------RESOURCES AND REFERENCES-------------------
# DATASET: P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.Modeling wine preferences by data mining from physicochemical properties.In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236
# CODE CONTRIBUTOR: Mary Everett, University of Idaho PHD
