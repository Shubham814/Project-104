import csv
import pandas as pd
import statistics as st


pd_data = pd.read_csv("CSV_Data.csv")


totalPeople = 0
totalWeight = 0

weight_array = []

# for i in range(len(pd_data)):
#     totalPeople += 1
#     totalWeight += float(pd_data[i][2]) 
    
weight_array = pd_data["Weight(Pounds)"].tolist()

print(weight_array[0:6])

    


def findMean(weight):
    mean = st.mean(weight)
    statement = print("Mean of given Dataset is " + str(mean))
    return statement

def findMode(data):
    formula = st.mode(data)
    # mode = round(formula,4)
    statement = print("Mode of given Dataset is " + str(formula))
    return statement

def findMedian(data):
    formula = st.median(data)   
    # median = round(formula,4)
    statement = print("Median of given Dataset: " + str(formula))
    return statement


def setup():
    findMean(weight_array)
    findMode(weight_array)
    findMedian(weight_array)

setup()







# For arranging the numbers in ascending order 
    # if float(data[i][2]) < float(minimum):
    #     minimum = float(data[i][2])
    #     ascendingArray.insert(data[i][2])
    #     data.pop(i) 
    # elif float(data[i][2]) > float(minimum):
    #     ascendingArray.append(data[i][2])
    #     data.pop(i)