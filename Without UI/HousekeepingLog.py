import csv
import pandas as pd
from pathlib import Path


def readOneFile(name) -> list:
    my_list = []
    my_list.append(name)
    
    with open(name, "r", newline="") as f:
        content = csv.reader(f) # a list with lists
        for row in content:
            my_list.append(tuple(row))

    return my_list


def gatherHousekeepingLog() -> list:
    data = []
    for file in Path.cwd().glob("*.csv"):
        data_sample = []

        my_list = readOneFile(file.name) # a list with tuples
        name = my_list[0]
        list_of_tuples = my_list[1:]
        
        first_value = []
        for tuples in list_of_tuples[1:]:
            first_value.append(tuples[0])

        second_value = []
        total = 0
        for tuples in list_of_tuples[1:]:
            second_value.append(tuples[1])
            total += float(tuples[1])

        total_df = []
        for value in range(len(second_value)):
            if (value == (len(second_value) - 1)):
                total_df.append(total)
            else:
                total_df.append("")
        
        df = pd.DataFrame({list_of_tuples[0][0]: first_value, list_of_tuples[0][1]: second_value})
        df.insert(2, "TOTAL", total_df)
        data_sample.append(name)
        data_sample.append(df)
        data_sample.append(total)
        
        data.append(data_sample)

    return data


def createHousekeepingLog(data) -> None:
    writer = pd.ExcelWriter("HousekeepingLog.xlsx", engine="xlsxwriter")

    
    for data_sample in data:
        data_sample[1].to_excel(writer, sheet_name = data_sample[0][:-4])


    result = analyzeHousekeepingLog(data)
    df = pd.DataFrame(result)
    df.to_excel(writer, sheet_name = "TOTAL")
    
    writer.save()


def analyzeHousekeepingLog(data) -> dict:
    total_dict = {}
    for data_sample in data:
        total_dict[data_sample[0][:-4]] = [data_sample[2]]

    return total_dict


