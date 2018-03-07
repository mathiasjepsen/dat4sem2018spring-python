import webget
import pandas as pd
import numpy as np
import random

surnames_txt = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.all.last'
female_names_txt = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.female.first'
male_names_txt = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.male.first'

surnames_csv = pd.read_csv(webget.download(surnames_txt)).as_matrix()
female_names_csv = pd.read_csv(webget.download(female_names_txt)).as_matrix()
male_names_csv = pd.read_csv(webget.download(male_names_txt)).as_matrix()

surnames = []
female_names = []
male_names = []

for row in surnames_csv:
    names = row[0].split()
    surnames.append(names[0].title())

for row in female_names_csv:
    names = row[0].split()
    female_names.append(names[0].title())

for row in male_names_csv:
    names = row[0].split()
    male_names.append(names[0].title())


random_female_names = [random.choice(female_names) + " " + random.choice(surnames) for _ in range(50)]
random_male_names = [random.choice(female_names) + " " + random.choice(surnames) for _ in range(50)]

random_names = random_female_names + random_male_names

print(random_names)

#random_groups = [group_names[random.randrange(len(group_names))] for _ in group_names]
#filtered_groups = list(set(random_groups))
