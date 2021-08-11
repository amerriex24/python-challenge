import os 
import csv
import statistics
import math

#declaring variables

Total_Months = 0
net_total  = 0
profit_loss = []
largest_increase_date = ""
largest_increase_amount = 0 
change = []
largest_decrease_date = ""
largest_decrease_amount = 0



#Setting up CSV Path

csvpath = os.path.join("Resources", "budget_data.csv")

#read the csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Skipping the header to go to values
    header = next(csvreader)

    for i, row in enumerate(csvreader):
        Total_Months = Total_Months + 1
        #netTotal = netTotal + int(row[1])
        profit_loss.append(int(row[1]))
        if i > 0:
            change_row = int(row[1]) - int(previous_row[1])
            change.append(change_row)
            if  change_row > largest_increase_amount:
                largest_increase_amount = change_row
                largest_increase_date = row[0]
            if change_row < largest_decrease_amount:
                largest_decrease_amount = change_row
                largest_decrease_date = row[0]
        previous_row = row
        
sum_profit_loss = sum(profit_loss)
average_change = sum(change) / len(change)
avg_change_rounded = round(average_change, 2)

output = (f'''
Financial Analysis
----------------------------
Total Months: {Total_Months}
Total: ${sum_profit_loss}
Average  Change: ${avg_change_rounded}
Greatest Increase in Profits: {largest_increase_date} (${largest_increase_amount})
Greatest Decrease in Profits:  {largest_decrease_date} (${largest_decrease_amount})
''')
#print analysis to terminal 
print(output)