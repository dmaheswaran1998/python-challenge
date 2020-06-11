#importing the relevant modules 

import os 
import csv
import sys 


#defining all the variables needed in order to run the analysis 
candidate_list=list()
candidate_list1=list()
candidate_vote=list()
percentages_list=list()
percentage=float()
total_candidate_vote=0
greatest=0
winner=list()



#opening the python csv file  eith os package
election_path = os.path.join("Resources", "election_data.csv")
with open(election_path, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #defining and storing the csv header
    csv_header=next(csvreader)


    for row in csvreader:
        #storing the candidate votes as a separate list 
        candidate=row[2]
        candidate_list.append(candidate)

#obtaining the total cotes as the number of votes cast
total_votes=len(candidate_list)

#adding all the unique candidate names into a separate list (candidate_list1)
for candidate in candidate_list:
    if candidate not in candidate_list1:
        candidate_list1.append(candidate)



#Tallying up the Votes in the candidate list 


#tallying up the total amount of votes for each unique candidate 
for x in range(len(candidate_list1)):
    for candidate in candidate_list:
        if candidate==candidate_list1[x]:
            candidate_vote_number=1
            total_candidate_vote=total_candidate_vote+candidate_vote_number
        #storing the total candidate votes for each candidate vote in a separate list 
    candidate_vote.append(total_candidate_vote)
    total_candidate_vote=0



#storing the percentages for each of the candidates and storing them in a percentages list 
for x in range(len(candidate_vote)):
    percentage=(candidate_vote[x]/total_votes)*100
    percentages_list.append(percentage)



#storing "greatest" as the highest percentage number   
#first need to modify the length of the list so that the code can run

for x in range(len(percentages_list)-1):
    if percentages_list[x+1]>percentages_list[x] and percentages_list[x+1]>greatest:
        greatest= percentages_list[x+1]
    elif percentages_list[x]>percentages_list[x+1] and percentages_list[x]>greatest:
        greatest= percentages_list[x]


#Zipping all the lists together containing summary statistics for each candidate (name of eahc unique candidate, percetnage each candidate received and )
summary_data=zip(candidate_list1, percentages_list, candidate_vote)
#writing the summary zipped lists into a csv file
with open("Resources/summary_data.csv", "w", newline='') as output_csv_file:
    csvwriter = csv.writer(output_csv_file, delimiter = ",")

    csvwriter.writerow(["Candidate Name", "Percentages","Number of Votes"])

    csvwriter.writerows(summary_data)

#reading the csv file that was just created 
summary_final = os.path.join("Resources", "summary_data.csv")
with open(summary_final, 'r') as csvfile:
    # Split the data on commas
    csvreader1 = csv.reader(csvfile, delimiter=',')
    #defining and storing the csv header for the new csv file 
    header_1=next(csvreader1)


#matching the greatest percentage number obtained earlier with the candidate that received this amount of votes
    for row in csvreader1:
        if float(row[1])==greatest:
            winner.append(row[0])

winner_1=str(winner[0])

#Printing final output to terminal
print("Election Results")
print("---------------------------------------------------")
print(f"Total Votes: {total_votes} ")
print("---------------------------------------------------")
for x,y,z in zip(candidate_list1, percentages_list, candidate_vote):
    print(f"{x}: {y:.3f}% ({z})")
print("---------------------------------------------------")
print(f"Winner: {winner_1}")
print("---------------------------------------------------")

#Printing final output to a text file 
sys.stdout = open("Analysis/Election_Analysis.txt", "w")

print("Election Results")
print("---------------------------------------------------")
print(f"Total Votes: {total_votes} ")
print("---------------------------------------------------")
for x,y,z in zip(candidate_list1, percentages_list, candidate_vote):
    print(f"{x}: {y:.3f}% ({z})")
print("---------------------------------------------------")
print(f"Winner: {winner_1}")
print("---------------------------------------------------")

sys.stdout.close()
