#importing the relevant modules 

import os 
import csv
import sys


#defining the relevant variables needed to run the code 
month_1=list()
profit_loss=list()
change=list()
greatest=0
less=0
greatest_least_month=list()
average_change=float()
total_profit=0
number_months=0

#defining average as a function in order to use later 

def average(numbers):
    denominator=len(numbers)
    numerator=float(0)
    for number in numbers: 
        numerator=numerator+number
    return numerator/denominator

#opening the python csv file 
budget_path = os.path.join("Resources", "budget_data.csv")
with open(budget_path, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #defining the csv header
    csv_header=next(csvreader)

    
    #reading the csv file 
    for row in csvreader:
        month=row[0]
        profit=int(row[1])
        #keeping track of the total profit in the total_profit variable
        total_profit=total_profit+profit
        #storing the profit/loss column in a separate list to manipulate the values further
        profit_loss.append(profit)
        month_1.append(month)           

#number of months is the list of the month_1 list 
number_months=str(len(month_1))

#defining a new variable (change_1) as the change between two consecutive months.
#storing this value as a list called change
#modifying the length so that the code runs
for x in range(len(profit_loss)-1):
    change_1=profit_loss[x+1]-profit_loss[x]
    change.append(change_1)

#obtaining the average change using the average function and defining the average change function

average_change=(average(change))

#pbtaining the greatest change over all months and storing this variable as "greatest"

for i in range(len(change)-1):
    if change[i+1]>change[i] and change[i+1]>greatest:
        greatest= change[i+1]
    elif change[i]>change[i+1] and change[i]>greatest:
        greatest= change[i]

#pbtaining the least change over all months and storing this variable as "less"


for i in range(len(change)-1):
    if change[i+1]<change[i] and change[i+1]<less:
        less= change[i+1]
    elif change[i]<change[i+1] and change[i]<less:
       less= change[i]


#Adding an element in the change list to account for the fact that the change in the first month is 0
change.insert(0,0)



# zipping these three lists together in a new csv file (and then adding headers after) 
new_profit=zip(month_1, profit_loss, change)

#writing a new csv file tthat also includes the change list
with open("Resources/new_data.csv", "w", newline='') as output_csv_file:
    csvwriter = csv.writer(output_csv_file, delimiter = ",")

    csvwriter.writerow(["Month", "Profit/Loss", "Monthly Change"])

    csvwriter.writerows(new_profit)

#reading the new csv file so that it can be manipulated
new_data = os.path.join("Resources", "new_data.csv")
with open(new_data, 'r') as csvfile:
    # Split the data on commas
    csvreader1 = csv.reader(csvfile, delimiter=',')
    #defining the csv header
    header_1=next(csvreader1)


#finding and storing the month with both the greatest change and lowest change as a list (greatest_least_change)
    for row in csvreader1:
        if float(row[2])==greatest:
            greatest_least_month.append(row[0])
        if float(row[2])==less:
            greatest_least_month.append(row[0])


#storing the month that has the greatest change as greatest_month and month with tleast change as less_month
greatest_month=str(greatest_least_month[0])
less_month=str(greatest_least_month[1])

#Print final output to terminal

print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {number_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest})")
print(f"Greatest Decrease in Profits: {less_month} (${less})")


#Exporting final output to a text file

sys.stdout = open("Analysis/Financial_Analysis.txt", "w")

print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {number_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest})")
print(f"Greatest Decrease in Profits: {less_month} (${less})")

sys.stdout.close()



