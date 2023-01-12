import os
import csv

csv_path=os.path.join(r"C:\Users\lintu\Documents\git\Assignment-UoTBootCamp\python-challenge\PyBank\Resources\budget_data.csv")
ProfitLossChange = []
Months=[]
countmonths=0
netprofitloss=0
currentmonthprofitloss=0
previousmonthprofitloss=0
profitlossdiff=0
with open(csv_path,encoding='utf') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        countmonths=countmonths+1
        currentmonthprofitloss=int(row[1])
        netprofitloss = netprofitloss+currentmonthprofitloss
        if(countmonths==1):
            previousmonthprofitloss=currentmonthprofitloss
        else:
            profitlossdiff=currentmonthprofitloss-previousmonthprofitloss
        ProfitLossChange.append(profitlossdiff)
        Months.append(row[0])
        previousmonthprofitloss=currentmonthprofitloss
    Netprofitlosses=sum(ProfitLossChange)
    numberofmonths=countmonths
    Averagechange=round(Netprofitlosses/(countmonths-1),2)
    Greatestincrease=max(ProfitLossChange)
    Smallestincrease=min(ProfitLossChange)
    Greatestmonthindex=ProfitLossChange.index(Greatestincrease)
    Smallestmonthindex=ProfitLossChange.index(Smallestincrease)
    Greatestmonth=Months[Greatestmonthindex]
    Smallestmonth=Months[Smallestmonthindex]
print(f"{numberofmonths}")
print(f"{netprofitloss}")
print(f"{Greatestincrease}")
print(f"{Greatestmonth}")
print(f"{Averagechange}")

