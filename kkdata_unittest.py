import kkdata
import csv
import pprint

filename = './befkbhalderstatkode.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        assert kkdata.STATISTICS[row[0]][row[1]][row[2]][row[3]] == row[4]

