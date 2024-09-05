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
quality_series = wine_df["quality"]
# quality_series user named variable, using dataframe bracket notation ['<column name>']
print("Quality Series")
print(quality_series)

# multiple columns
# can convert this into a list and do multiple column names
# quality_series = wine_df['<column name, column name list>']


# Indexing
# return a list with the quality column dataset
# grabbing the values out of the series <.values> and converting it to a python list <.tolist()>
quality_list = wine_df["quality"].values.tolist()
print("Quality List")
print(quality_list)
# list python format


# General Note: If feeding directly from Pandas to an AI model , the libraries using like psykitlearn, carras, pytorch are going to be able to handle pandas dataframe objects, but if using a more custom implementation or library that doesnt support this useful to get them into a different format

# Using .loc
# Method indexing dataframe
# Label based
# indexing based on feature name using loc property of dataframe
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

#Another Slice Method
print("Everything before and up to the fifth indexed quality value")
print(wine_df.loc[:5,"quality"])
# :5 everything and up to 5

#Slice After Index Value
print("Everything after the 4890th indexed quality value")
print(wine_df.loc[4890:, "quality"])

#List to Get More Than One Column on Slice
print("Everything after the 4890th indexed quality and sulfates value")
print(wine_df.loc[4890:, ["quality","sulphates"]])


# Using iloc
# works on numeric indexing instead of label indexing
# If slicing end exclusive (number we put at end of slice is not going to be included)
# using indexes for both rows and columns

# Subset of dataframe
# Slice
print("Row Indexes 1-2 and Column Indexes 1-4")
print(wine_df.iloc[1:3,1:5]) 

# index with single number 
print("4th Row Index, First Item")
# Actually the 5th row
print(wine_df.iloc[4,0])

print("All columns, row index 4")
print(wine_df.iloc[4,:])

#Selecting a row or rows based on a condition
print("Want all rows where the wine quality is above 5")
print(wine_df.loc[wine_df["quality"] > 5])
# passing in the quality column of the winedf
# dont know why just dont use the column directly
# locating all instances where quality > 5 is true
# getting the entire dataframe back 

# use length property of the index of the subdata frame
print("How many rows is this?")
print(len(wine_df.loc[wine_df["quality"] > 5].index))
#length function
#index gives us row count 

# for conditional expressions you can use the and symbol and the pipe symbol for or to combine conditions into different expressions
# if your going to do that make sure you have () around subconditions

# Make a more restricted veiw 
print("All rows where quality is above 5 and sulphates are above 0.45")
sub_df = wine_df.loc[(wine_df["quality"]>5) & (wine_df["sulphates"]<0.45)]
print(sub_df.head())
print(len(sub_df.index))
# set equal to a subdata frame <sub_df> 
# will create a copy of dataframe

# when have new dataframe will not automatically reset your index so if your using an indexing method in Pandas can cause issues
# function to reset the index 
# sub_df.reset.index() 

# Handling Missing Data
# Data Entry, Blank Space in Column or Row
# AI technique can sometimes handle a missing entry in column or row
# Find them, handle them - may want to take out column or row or fill the data 

# Data set doesnt have any missing values 
# way to look at that using isna()
print(wine_df.isna())
# Way to get our counts of our na values is using the value counts property 
print(wine_df.isna().value_counts())
# prints out number of true or false values per column
# only false so everything has a value- total count for each false value is size of data set

# Insert a Non-number (NaN) Value
# Get first column value in dataframe
print(wine_df.loc[0, "quality"])
# Create New Dataframe so dont screw up anything
new_df = wine_df
# Grab First quality score in new dataframe and set to python keyword none to create NaN
new_df.loc[0, "quality"] = None
print(new_df.loc[0,"quality"])

print("New Missing Value Counts")
print(new_df.isna().value_counts())

# Drop the NaN
print("Number of Rows before dropping NaN")
print(len(new_df.index))
cleaned_df =  new_df.dropna()
# going to drop the NaN value and not reset the index
# want a brand new dataframe with its own fresh index 
cleaned_df.reset_index(inplace=True)
# also creating a copy so we can reset this function back to the clean dataframe or we can use optional function keywords such as do this in place so we dont have to reset again
print("Number of Rows after dropping NaN")
print(len(cleaned_df.index))
# what had been set to NaN location 
print(cleaned_df.loc[0,"quality"])


# Visualizing Data
# import data visualization libraries 
import matplotlib.pyplot as plt
# matlab has plotting library very common to use in python 
import seaborn as sns

# Correlation
# See how much these variables are correlated
print(wine_df.corr())
# corr function will input correlation matrix
# plot it using heat map
plot = sns.heatmap(wine_df.corr())
# pop it up in terminal 
# using jupityr notebook probably dont have to call this
plt.show()
# clear plot
plt.clf()


#--------------------------------RESOURCES AND REFERENCES-------------------
# DATASET: P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.Modeling wine preferences by data mining from physicochemical properties.In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236
# CODE CONTRIBUTOR: Mary Everett, University of Idaho PHD
