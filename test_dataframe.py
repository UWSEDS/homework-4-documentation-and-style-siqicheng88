"""
This module perfomrs three tests for given data frame
Check that all columns have values of the corect type.
Check for nan values.
Verify that the dataframe has at least one row.
"""

 ## Check that all columns have values of the corect type.

def correct_type(data):
    """
    Return True if all columns have values of the correct type

    Argument: dataframe
    Output: True if all columns have values of the correct type
    """

    if all(data[col].dtypes == data.dtypes[0] for col in data.columns):
        if all(data[col].isnull().sum() == 0 for col in data.columns):
            print('All columns have values of the correct type.')
    else:
        print('Bad result.')



## Check for nan values.

def nan_value(data):
    """

    Return True if there is null value.

    Argument: dataframe
    Output: True if there is null value 
    """
    return data.isnull().any()

## Verify that the dataframe has at least one row.

def at_least_one_row(data):
    """
    Return True if the dataframe has at least one row.
    Argument: dataframe
    Output: True if there is at least one row data frame.
    """
    if len(data) >= 1:
        print('The dataframe has at least one row')
    else:
        print('The dataframe has least than one row')
