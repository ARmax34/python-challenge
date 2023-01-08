#Imprting the Modules
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")



    #Creating the polls list
    polls =[]
    for votes in csvreader:
        polls.append(votes[2])
    #print(polls)


    #total votes
    all_votes = len(polls)
    #print(all_votes)



    candidates = []

    votes = []

    for person in polls:
        if person not in candidates:
            candidates.append(person)
            votes.append(1)

        else:
            candidate_index = candidates.index(person)
            votes[candidate_index] += 1

    #print("index return" + str(candidates))
    #print("vote count: " + str(votes))


    #percentage_count list creation
    percentage_count = []
    percentage_count = [(votes[k]/all_votes)*100 for k in range(0,len(votes))]
    #print(percentage_count)

    #The Printout card
    print("Election Results" + '\n')
    print("-------------------------" + '\n'),

    for p in range(0,len(votes)):
        print(candidates[p] + "   " + str(votes[p]) + "   %" + str(percentage_count[p]) + '\n')
        if votes[p] > votes[p-1]:
            winner = candidates[p]

    print("-------------------------" + '\n'),
    print("Winner: " + winner + '\n'),
    print("-------------------------" + '\n')



    #printing report to text file
    report = open('analysis/electionResults','w')

    report.write("Election Results" + '\n')
    report.write("-------------------------" + '\n'),

    for p in range(0,len(votes)):
        report.write(candidates[p] + "   " + str(votes[p]) + "   %" + str(percentage_count[p]) + '\n')
        if votes[p] > votes[p-1]:
            winner = candidates[p]

    report.write("-------------------------" + '\n'),
    report.write("Winner: " + winner + '\n'),
    report.write("-------------------------" + '\n')

    report.close()