# Import os and cvs
import csv
import os
import numpy as np
from numpy import complex64, longlong

budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Skip the header
    csv_header = next(csv_reader)

# Count number of rows
    file = open(budget_csv)
    csv_reader = csv.reader(csv_file, delimiter = ",")
    num_rows = 0

    for row in open(budget_csv):
        num_rows = num_rows + 1

# Print total months
print("Total months: ", num_rows)

#   * The net total amount of "Profit/Losses" over the entire period

total_profit_losses = 0



# for row in open(budget_csv):
#     total_Profit_Losses += float(row[1])

#     print(float("Total: {total_Profit_Losses}"))

# for row in open(budget_csv):
#     total_profit_losses += float(0)

# print(float("Total: ", total_profit_losses))


#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

average_profit_losses = 0

#   * The greatest increase in profits (date and amount) over the entire period

increase_profit = 0
increase_profit_month = ""

#   * The greatest decrease in profits (date and amount) over the entire period

decrease_profit = 0
decrease_profit_month = ""

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
