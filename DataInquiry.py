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


#--------------------------------RESOURCES AND REFERENCES-------------------
# DATASET: P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.Modeling wine preferences by data mining from physicochemical properties.In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236
# CODE CONTRIBUTOR: Mary Everett, University of Idaho PHD
