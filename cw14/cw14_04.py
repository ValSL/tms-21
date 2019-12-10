import sys
import csv
import argparse

print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-a', '--age', required=True)
args = parser.parse_args()
with open('newfile.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow([args.first_name, args.last_name, args.age])
