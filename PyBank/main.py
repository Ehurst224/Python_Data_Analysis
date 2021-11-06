# Import os and cvs
import csv
import os
import numpy as np

budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Skip the header
    csv_header = next(csv_reader)

# Find the total number of months
# Count number of rows
    file = open(budget_csv)
    csv_reader = csv.reader(csv_file, delimiter = ",")
    num_rows = -1

    for row in open(budget_csv):
        num_rows = num_rows + 1

    # Print total months
    # print("Total months: ", num_rows)

#   * The net total amount of "Profit/Losses" over the entire period

    date = []
    profit_losses = []
    for row in csv_reader:
        date.append(row[0])
        profit_losses.append(int(row[1]))

    profit_losses_total = (sum(profit_losses))

    ## print(f'Total: ${profit_losses_total}')
    

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    avg_change = []
    for i in range(len(profit_losses)-1):
        avg_change.append(profit_losses[i+1]-profit_losses[i])

    # print(f'Average Change ${round(sum(avg_change)/len(avg_change),2)}')
    
    # avg_change = round((profit_loses[-1] - profit_loses[0])/num_rows, 2)
    # print (f'Average Change ${avg_change}')

#   * The greatest increase in profits (date and amount) over the entire period

    greatest_increase = max(avg_change)
    increase_indexing = avg_change.index(greatest_increase)
    profit_increase = date[increase_indexing + 1]

    # print(f'Greatest Increase in Profits: {profit_increase} (${greatest_increase})')

#   * The greatest decrease in profits (date and amount) over the entire period

    greatest_decrease = min(avg_change)
    decrease_indexing = avg_change.index(greatest_decrease)
    profit_decrease = date[decrease_indexing + 1]

    # print(f'Greatest Decrease in Profits: {profit_decrease} (${greatest_decrease})')

print ("----------------------------")
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: ", num_rows)
print ("----------------------------")
print (f'Total: ${profit_losses_total}')
print ("----------------------------")
print (f'Average Change ${round(sum(avg_change)/len(avg_change),2)}')
print ("----------------------------")
print (f'Greatest Increase in Profits: {profit_increase} (${greatest_increase})')
print ("----------------------------")
print(f'Greatest Decrease in Profits: {profit_decrease} (${greatest_decrease})')
print ("----------------------------")

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results

export_to_terminal = os.path.join("analysis", "bank.budget.txt")
f = open (export_to_terminal, "w")
f.write ("----------------------------")
f.write ("\n")
f.write ("Financial Analysis")
f.write ("\n")
f.write ("Total months:  {num_rows}")
f.write ("\n")
f.write ((f'Total: ${profit_losses_total}'))
f.write ("\n")
f.write (f'Average Change ${avg_change}')
f.write ("\n")
f.write (f'Greatest Increase in Profits: {profit_increase} (${greatest_increase})')
f.write ("\n")
f.write (f'Greatest Decrease in Profits: {profit_decrease} (${greatest_decrease})')
f.write ("\n")
f.write ("----------------------------")
