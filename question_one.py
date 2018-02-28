import webget
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#csv_file = webget.download("https://github.com/PatrickFenger/pythonAssignments/raw/master/KoreanConflict.csv")
csv_file = "./KoreanConflict.csv"

def question_1():
    csv = pd.read_csv(csv_file)
    csv_matrix = csv.as_matrix()
    
    mask = (csv_matrix[:, 3] == "MARINE CORPS")
    count = csv_matrix[mask].shape[0]
    print(count)

def question_2():
    csv = pd.read_csv(csv_file)
    csv_matrix = csv.as_matrix()

    enrollment_types = np.unique(csv_matrix[:, 2])
    

    plt.bar(enrollment_types, )




question_2()