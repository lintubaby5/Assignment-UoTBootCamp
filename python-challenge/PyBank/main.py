import os
import csv

#file path for csv input file
csv_path=os.path.join(r"Resources","budget_data.csv")
#lists to extract Months and Difference of ProfitLoss between each rows
ProfitLossChange = []
Months=[]
#declare variables to zero
countmonths=0
netprofitlosses=0
currentmonthprofitloss=0
previousmonthprofitloss=0
profitlossdiff=0
#read from csv file
with open(csv_path,encoding='utf-8-sig') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #delete header line to read from second row
    next(csvreader, None)
    #loop to go through each row
    for row in csvreader:
        #count each row to find total months
        countmonths=countmonths+1
        #current row's profitloss value
        currentmonthprofitloss=int(row[1])
        #variable to calculate the sum of profitloss
        netprofitlosses = netprofitlosses+currentmonthprofitloss
        #loop to store first profitloss change as 0 and next values as difference between current row and previous row
        if(countmonths==1):
            previousmonthprofitloss=currentmonthprofitloss
        else:
            profitlossdiff=currentmonthprofitloss-previousmonthprofitloss
        #append the difference value to the list
        ProfitLossChange.append(profitlossdiff)
        #append the months to the month list
        Months.append(row[0])
        #set previous value as the current rows profitloss
        previousmonthprofitloss=currentmonthprofitloss
    #to find number of months
    numberofmonths=countmonths
    #find average change of profit losses
    netprofitloss=sum(ProfitLossChange)
    Averagechange=round(netprofitloss/(countmonths-1),2)
    #find the greatest and smallest increase by Max and Min operations in the Change list
    Greatestincrease=max(ProfitLossChange)
    Smallestincrease=min(ProfitLossChange)
    #find the index of greatest and smallest increase to get the month from the months list
    Greatestmonthindex=ProfitLossChange.index(Greatestincrease)
    Smallestmonthindex=ProfitLossChange.index(Smallestincrease)
    #find the greatest and smallest increase months from the list of Months
    Greatestmonth=Months[Greatestmonthindex]
    Smallestmonth=Months[Smallestmonthindex]
#print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {numberofmonths}")
print(f"Total : ${netprofitlosses}")
print(f"Average Change : ${Averagechange}")
print(f"Greatest Increase in Profits : {Greatestmonth} (${Greatestincrease})")
print(f"Greatest Decrease in Profits : {Smallestmonth} (${Smallestincrease})")

#declare the text file to write the output to
txtfilepath=os.path.join("outputPyBank.txt")
with open(txtfilepath,'w') as txtfile:
    #write into the file
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months : {numberofmonths}\n")
    txtfile.write(f"Total : ${netprofitlosses}\n")
    txtfile.write(f"Average Change : ${Averagechange}\n")
    txtfile.write(f"Greatest Increase in Profits : {Greatestmonth} (${Greatestincrease})\n")
    txtfile.write(f"Greatest Decrease in Profits : {Smallestmonth} (${Smallestincrease})\n")