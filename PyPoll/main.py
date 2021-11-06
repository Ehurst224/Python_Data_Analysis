import os
import csv
import numpy as np

election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Skip the header
    csv_header = next(csv_reader)

#   * The total number of votes cast
    # Count number of rows
    file = open(election_csv)
    csv_reader = csv.reader(csv_file, delimiter = ",")
    num_rows = -1

    for row in open(election_csv):
        num_rows = num_rows + 1

# Print total months
    # print("Total votes: ", num_rows)

#   * A complete list of candidates who received votes
    candidates = []
    i = ["Voter ID", "County", "Candidate"]

   #  for candidate_name in candidates:
    for row in csv_reader:
        candidates.append(row[2])

    alpha_order= np.sort(list(set(candidates)))

    # print(list(set(candidates)))

    # print(alpha_order)

#   * The total number of votes each candidate won
    
    count_khan = 0
    for candidate in candidates:
        if candidate == "Khan":
            count_khan = count_khan + 1

    # print(count_khan)
   
    count_correy = 0
    for candidate in candidates:
        if candidate == "Correy":
            count_correy = count_correy + 1

    # print(count_correy)

    count_li = 0
    for candidate in candidates:
        if candidate == "Li":
            count_li = count_li + 1

    # print(count_li)

    count_ot = 0
    for candidate in candidates:
        if candidate == "O'Tooley":
            count_ot = count_ot + 1

    # print(count_ot)

#   * The percentage of votes each candidate won

    khan_percent = round((count_khan / num_rows * 100),2)
    # print(f'{khan_percent} %')

    correy_percent = round((count_correy / num_rows * 100),2)
    # print(f'{correy_percent} %')

    li_percent = round((count_li / num_rows * 100),2)
    # print(f'{li_percent} %')

    ot_percent = round((count_ot / num_rows * 100),2)
    # print(f'{ot_percent} %')

#   * The winner of the election based on popular vote.

    winner = {"Khan": khan_percent, "Correy" : correy_percent, "Li" : li_percent, "O'Tooley" : ot_percent}
    max_value = max(winner, key=winner.get)
    # print(max_value)

print ("-------------------------")
print ("Election Results")
print ("-------------------------")
print("Total votes: ", num_rows)
print ("-------------------------")
print (f'{alpha_order[1]}: {khan_percent}% ({count_khan})')
print (f'{alpha_order[0]}: {correy_percent}% ({count_correy})')
print (f'{alpha_order[2]}: {li_percent}% ({count_li})')
print (f'{alpha_order[3]}: {ot_percent}% ({count_ot})')
print ("-------------------------")
print (f"Winner: {max_value}")
print ("-------------------------")

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

export_to_terminal = os.path.join("analysis", "poll.budget.txt")
f = open (export_to_terminal, "w")
f.write ("-------------------------")
f.write ("\n")
f.write ("Election Results")
f.write ("\n")
f.write (f'Total votes: {num_rows}')
f.write ("\n")
f.write (f'{alpha_order[1]}: {khan_percent}% ({count_khan})')
f.write ("\n")
f.write (f'{alpha_order[0]}: {correy_percent}% ({count_correy})')
f.write ("\n")
f.write (f'{alpha_order[2]}: {li_percent}% ({count_li})')
f.write ("\n")
f.write (f'{alpha_order[3]}: {ot_percent}% ({count_ot})')
f.write ("\n")
f.write (f"Winner: {max_value}")
f.write ("\n")
f.write ("-------------------------")