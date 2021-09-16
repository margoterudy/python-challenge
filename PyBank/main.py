# Create file paths across operating systems
import csv

# Module for reading CSV files
import os

#get file
csvpath = os.path.join( 'Resources', 'budget_data.csv')

# Define variables 
total_months = []
total_profit = []
monthly_profit_change = []


# Open csv file
with open(csvpath, newline="", encoding="utf-8") as csvfile:

# Specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvfile) 

# Read each row of data after the header
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))


# Loop through the profits for monthly change
    for i in range(len(total_profit)-1):
        
        # Take difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])


# Obtain the max and min / montly profit change 

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max & min to correct month using month list and index from max & min
 #(plus 1 at the end bc month associated with change the next mo)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#finacial analysis *tutor help
finacial_analysis=f"""
Financial Analysis
----------------------------
Total Months: {len(total_months)}
Total: ${sum(total_profit)}
Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}
Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})
Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})
"""
print (finacial_analysis)


# Output files 

with open("Analysis/main.txt","w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
 
    file.write(finacial_analysis)