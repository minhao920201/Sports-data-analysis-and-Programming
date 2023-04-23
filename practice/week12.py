import csv
with open("players.csv") as infile:
    data = list(csv.DictReader(infile))
    print(data)
