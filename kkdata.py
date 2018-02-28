import webget
import csv
import pprint

#url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
# webget.download(url)
filename = './befkbhalderstatkode.csv'

STATISTICS = {}

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        if row[0] in STATISTICS.keys():
            if row[1] in STATISTICS.get(row[0]):
                if row[2] in STATISTICS.get(row[0]).get(row[1]):
                    STATISTICS[row[0]][row[1]][row[2]].update(
                        {row[3]: row[4]})
                else:
                    STATISTICS[row[0]][row[1]].update(
                        {row[2]: {row[3]: row[4]}})
            else:
                STATISTICS[row[0]].update(
                    {row[1]: {row[2]: {row[3]: row[4]}}})
        else:
            STATISTICS.update(
                {row[0]: {row[1]: {row[2]: {row[3]: row[4]}}}})

