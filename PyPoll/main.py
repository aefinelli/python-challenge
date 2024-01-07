#Import os
import os
#create import to read csv files
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
#Open the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
print(csvreader)
csv_header=next(csvreader)
print(f"CSV Header: {csv_header}")
for row in csvreader: 
    print(row)