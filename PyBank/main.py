#Imprting the Modules
import os
import csv

#creating the path for the csv to be accessed
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    cr = csv.reader(csvfile, delimiter=',')
    crb = cr

    # Read the header row first (skip this step if there is now header)
    csv_header = next(cr)

    #print(list(cr)[77])

#Testing block
    #print(f"CSV Header: {csv_header}")

    #Creating the Numbers and Dates Array
    numbers = []
    dates =[]
    for row in cr:
        numbers.append(int(row[1]))
        dates.append(row[0])
    #list(map(int,numbers))
    #print(numbers)
    #print(dates)



    #Total Months
    periodMonths = len(numbers)
    #print (periodMonths)

    #The total sum of profits + Loss
    totalNumber = sum(numbers)
    #print(totalNumber)




    #Creating the Changes Array 
    #changes = []
    changes = [(numbers[i + 1] - numbers[i]) for i in range(0,len(numbers)-1)]
    #print("printing changes",changes)

    #Average Change
    avgChange = sum(changes) / len(changes)
    #avgChange = round(avgChange,2)
    #print("average change:",avgChange)





    #Max Changes
    maxChanges = max(changes)
    #print(maxChanges)

    #Max Index for Changes
    maxChangesIndex = changes.index(maxChanges)
    #print(maxChangesIndex)   

    #Max Index change for cr
    maxMainIndex = maxChangesIndex
    #print(maxMainIndex)
    #print("amount of change", changes[maxMainIndex])
    #print("dates -------: ", dates[maxMainIndex + 1])
    #maxChanges = changes[maxMainIndex]
    periodMaxDate = dates[maxMainIndex + 1]



    #Min Changes
    minChanges = min(changes)
    #print(minChanges)

    #Min Index for Changes
    minChangesIndex = changes.index(minChanges)
    #print(minChangesIndex)   

    #Max Index change for cr
    minMainIndex = minChangesIndex
    #print(minMainIndex)
    #print("amount of change", changes[minMainIndex])
    #print("dates -------: ", dates[minMainIndex + 1])
    #minChanges = changes[minMainIndex]
    periodMinDate = dates[minMainIndex + 1]







    #Print test
    print("Financial Analysis" + '\n'),
    print("----------------------------" + '\n'),
    print("Total Months: " + str(periodMonths) + '\n'),
    print("Total : $" + str(totalNumber) + '\n'),
    print("Average Change: $" + str(avgChange) + '\n'),
    print("Greatest Increase in Profit: " + str(periodMaxDate) + "; Amount: $" + str(maxChanges) + '\n'),
    print("Greatest Decrease in Profit: " + str(periodMinDate) + "; Amount: $" + str(minChanges) + '\n')



    #Writing to text file
    report = open('analysis/financialAnalysis','w')

    report.write("Financial Analysis" + '\n'),
    report.write("----------------------------" + '\n'),
    report.write("Total Months: " + str(periodMonths) + '\n'),
    report.write("Total : $" + str(totalNumber) + '\n'),
    report.write("Average Change: $" + str(avgChange) + '\n'),
    report.write("Greatest Increase in Profit: " + str(periodMaxDate) + "; Amount: $" + str(maxChanges) + '\n'),
    report.write("Greatest Decrease in Profit: " + str(periodMinDate) + "; Amount: $" + str(minChanges) + '\n')

    report.close()

