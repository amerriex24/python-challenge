import os 
import csv
import statistics
import math


#declaring variables

Total_Months = 0
net_total  = 0
p_profitloss = 0 
Average_change = 0 
max_increase = 0 
min_increase= 0 
Total = 0 
net_change = 0 
netchange = []
months= []


#Setting up CSV Path

csvpath = os.path.join("Resources", "budget_data.csv")

#read the csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Skipping the header to go to values
    header = next(csvreader)

#Setting loop to start on second row 
    first_row = next(csvreader)
    Total_Months += 1 
    net_total  += int(first_row[1])
    p_profitloss = int(first_row[1])

 #Iterating through the rows
    for row in csvreader:

    #Counting month & Totals
        Total_Months += 1
        net_total += (first_row[1])

#Adding months to the list/appending months     
    months.append(first_row[0])

# Monthly changes
    net_change = int(first_row[1]) - p_profitloss

#appending each month's P/L to the list 
    netchange.append(net_change)    

#Next months P/L 

    p_profitloss = int(first_row[1])

#Calculating the average changes monthly
Average_change = round(statistics.mean(netchange), 2)


#Max Increases 
max_increase = round(max(netchange), 2)
maxmonth = months[netchange.index(max_increase)]



min_increase = round(min(netchange), 2)
minmonth = months[netchange.index(min_increase)]

#Final Analysis 

print("--------------------------Financial Analysis------------------------")
print("--------------------------------------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Net Total : ${Total}")
print(f"Average Change: ${Average_change}")
print(f"Greatest Increase in Profits: {maxmonth}  (${max_increase})")
print(f"Greatest Decrease in Profits: {minmonth} (${min_increase})")






