
import pandas, numpy

# Python test object

test_data = {
    "name": [ "John", "Mary", "Joan"],
    "age": [ 42, 21, 46],
}

# Converting test object into Panda dataframe

test_frame = pandas.DataFrame(test_data)

# Printing out test_frame

print(test_frame.to_string())

# Reads the Excel file into a Panda dataframe

f1data = pandas.read_excel("2023f1data.xlsx")

# Display first five rows of data

#print(f1data.head())

# Display column names and data types

#print(f1data.info())

# Print out the dataframe

print(f1data.to_string())

#### Series - One-dimensional ####

# Create Series and print. One dimensional data

row_data = [1, 4, 2]

# Index specifies labels. 
row = pandas.Series(row_data, index = ["One", "Two", "Three"])

print(row)

print(row["One"]) # Print out data for one label

# Using a key/value pair means that the keys will become the labels

# Selects only names from the data
test_row = pandas.Series(test_data, index=["name"])

print(test_row.to_string())

#### DataFrame Two-dimensional ####

# Load test_data into a DataFrame
data_frame = pandas.DataFrame(test_data)

print("-----")
#print(data_frame)
print(data_frame.loc[1]) # Print out information row. Provides additional information
print(data_frame.loc[[0, 1]]) # Print out more than one row.

# Names records in the DataFrame
named_data_frame = pandas.DataFrame(test_data, index = ["record1", "record2", "record3"])

print(named_data_frame)

# Print out only one named record
print(named_data_frame.loc["record2"])