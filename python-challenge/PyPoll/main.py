import os
import csv

#file path for csv input file
csv_path=os.path.join(R"Resources","election_data.csv")
#declare variables to zero
countvotes=0
Candidates=[]
votes=[]

#read from csv file
with open(csv_path,encoding='utf-8-sig') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #stores header
    csv_header=next(csvreader)
    for row in csvreader:
        #count each row to find total votes
        countvotes=countvotes+1
        if(row[2] not in Candidates):
            Candidates.append(row[2])
         

