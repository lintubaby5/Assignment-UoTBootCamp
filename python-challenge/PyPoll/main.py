import os
import csv
from collections import Counter

#file path for csv input file
csv_path=os.path.join(R"Resources","election_data.csv")
#declare variables to zero
countvotes=0
total_candidates=0
Candidates=[]
DistinctCandidates=[]
Candidatevotes=[]
HighestVotes=0
HighestVoteCandidate=""
#read from csv file
with open(csv_path,encoding='utf-8-sig') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #stores header
    csv_header=next(csvreader)
    for row in csvreader:
        #count each row to find total votes
        countvotes=countvotes+1
        #add the candidate to list
        Candidates.append(row[2])
    #find the counter for each Candidates and store it in a dict
    result=Counter(Candidates)
    #convert dictionary to lists
    for key, value in result.items():
        Candidate=key
        Votes=value
        DistinctCandidates.append(Candidate)
        Candidatevotes.append(Votes)
    #find total condidates
    total_candidates=len(DistinctCandidates)
    #print headers
    print("Election results")
    print("-------------------------")
    print(f"Total Votes: {countvotes}")
    print("-------------------------")
    #iterate through lists to print the Candidates and the Votes
    for i in range(total_candidates):
        CandidateiPercent=round(int(Candidatevotes[i])/int(countvotes)*100,3)
        print(f"{DistinctCandidates[i]}: {CandidateiPercent}% ({Candidatevotes[i]})")
        if(Candidatevotes[i]>HighestVotes):
            HighestVotes=Candidatevotes[i]
            HighestVoteCandidate=DistinctCandidates[i]
    print("-------------------------")
    print(f"Winner: {HighestVoteCandidate}")
    print("-------------------------")
#declare the text file to write the output to
txtfilepath=os.path.join(r"Analysis","outputPyPoll.txt")
with open(txtfilepath,'w') as txtfile:
    #write into the file
    txtfile.write("Election results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {countvotes}\n")
    txtfile.write("-------------------------\n")
    for i in range(total_candidates):
        CandidateiPercent=round(int(Candidatevotes[i])/int(countvotes)*100,3)
        txtfile.write(f"{DistinctCandidates[i]}: {CandidateiPercent}% ({Candidatevotes[i]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {HighestVoteCandidate}\n")
    txtfile.write("-------------------------\n")
    


