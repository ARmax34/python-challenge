# python-challenge
Georgia Tech Bootcamp module 3


The instructions For the Activity
---------------------------------------------------------------------------------------------------------------------------

## Instructions

PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote


---------------------------------------------------------------------------------------------------------------------------

The first thing I knew I needed to do was to create a new list that was more useable for me to work with.
    The first list that was extracted from the csv file had more information than necessary to work with.
        Creating a new list that will be called on with less data will decrease the processing time needed if the list in the csv file is replaced with a larger list since the new list will be more lean.

        Simplifying it also makes it more approachable of a program to both read and write it. 
            Any editing can be taken on in a more modular modular approach.

    This is the creation of the polls list and the for loop that cycles through the csv reader list.

The next segment deals with creating two more lists: candidates and votes.
    They loop through the slimmed down polls list and uses an if statement that is reliant on in the polls list names are new (where they are added to the candidates list) or currently on the list and will have their votes tallied on the votes list.

The individual candidate's votes totals on the votes list are then processed through a for loop with an equation to calculate for their percentage.
    The results are then added to percentage_count list.
        This also works well since each list is designed to have each of their values lined up appropriately.
            For example, if you were to find the index for a candidate's name, it would be the same index number for their total votes and percentage of votes.

Then their is the print segment which also acts as a testing ground to see what it will look like before the results are written in the text file.
    There is a for loop in the segment that details out all the information with the corresponding candidates.

Here is a video I found that gave me some inspiration on how to complete the assignment.

https://www.youtube.com/watch?v=b5xPmKcP0qA&list=WL&index=11&t=824s 