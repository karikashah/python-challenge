# Importing libraries
import os
import csv

inputFile = os.path.join("../../../Python Resources", "election_data.csv")
#outputFile = os.path.join("../../../Python Resources", "financialdata_KS.txt")

# Declare variables
totalVotes = 0 # for holding total count of votes 
currentCandidate = "" # holds current candidates name
candidateVotes = {} # has key value pair of each candidate & their votes
candidates = [] # has list of all candidates names

# Read Files
with open(inputFile) as electionData:
    reader = csv.DictReader(electionData)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the total votes
        totalVotes = totalVotes + 1
        currentCandidate = row["Candidate"]
        
        if currentCandidate not in candidates:
            # this is new candidate hence add him in the list of candidates
            candidates.append(currentCandidate)
            
            # also set his voting count to 1
            candidateVotes[currentCandidate] = 1
        else:
            # he is already in the list just add his vote to the dictionary
            candidateVotes[currentCandidate] = candidateVotes[currentCandidate] + 1

print(f"Election results:")
print("-------------------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------------------")
for cv in candidateVotes:
    print(cv + ": " + str(round(((candidateVotes[cv]/totalVotes)*100),3)) + "%" + " (" + str(candidateVotes[cv]) + ")") 
print("-------------------------------------")
print("Winner is ")
# printing the winner 
#print(max(int(s) for s in candidateVotes))
print("-------------------------------------")
