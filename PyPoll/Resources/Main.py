#Importing Modules

import csv
import os
#Loading files 
csvpath = os.path.join( "Resources", "election_data.csv")
output_path = os.path. join("./Analysis", "election_data.txt")

#Creaed Variables and assigned values. 
total_vote = 0 
candidates = {}
vote_percentage = []
winner = 0
candidate = ''
votes_per = []
winner = ''
winner_i = 0

with open(csvpath, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    csv_header = next(data)
    #Setting up loops
    for row in data:
        total_vote += 1 
        #finding the different elements in each row
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
#Seperate the elemets into keys and vak=lues list 
candidate = list(candidates.keys())
votes_per = list(candidates.values())
for i in range(len(candidate)):
    vote_percentage.append((votes_per[i] / total_vote) * 100)
for i in range(len(votes_per)):
    if votes_per[i] > votes_per[winner_i]:
        winner_i = i 


output = (

    f"---Election Results---\n"
    f"----------------------\n"
    f"-Total Votes: {total_vote}-\n"
    f"----------------------\n"
    "for i in range(len(candidate))\n"
    f"{candidate[i]}: {round(vote_percentage[i], 3)}% ({votes_per[i]})\n"

    f"----------------------\n"
    f"Winner: {candidate[winner_i]})\n"
    f"----------------------\n")
print(output)

output_path = open('Analysis/election_data.txt', 'w') 
output_path.write(output)
output_path.close()
    