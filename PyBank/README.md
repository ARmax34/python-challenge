# python-challenge
Georgia Tech Bootcamp module 3


The instructions For the Activity
---------------------------------------------------------------------------------------------------------------------------

## Instructions

PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period


---------------------------------------------------------------------------------------------------------------------------

The first step is extracting the information in the csv file and convening it to a list.

After that, the data is then spliced into two list (numbers and dates) using a for loop.
    These lists will also be lined up where their index numbers will match based on the csv file.

Then a couple of variables are found with simple setups.
    periodMonths for the total number of months.

    totalNumber for the total of all profits and losses over this period.

The next step is creating a list that is based off the changes between each month.
    This is done by using a for loop that comparers the values of the current to the previous months.
        This list will be one less then the previous list in length.
            The fist month does not have a prior month to compare to.

The average of the change list is calculated.

The Min and Max changes mirror each other in their setups. Max will be used as the example.
    -The max value is first found.
    -The index for that number is then found in the list.

    (there is a step there the change index is converted to the primary/main/first index, but the difference is made up in the next step)

    -the corresponding index number to the primary index is found to and then stores the value of the date in a variable.

Finally, there is the writing out in the print version that will appear in terminal and the writing of the values that were just printed onto the text file.

