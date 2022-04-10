from tkinter import *
import csv
from pathlib import Path


def checkFile(button) -> bool:
    """ Check if the corresponding file
    exists in the current directory. """
    path_to_file = button["text"] + ".csv"
    path = Path(path_to_file)

    if path.is_file():
        return True

    return False


def printResult(stat, stat_label) -> None:
    """ Show the statistics of the usage. """
    string = "======== RESULT ========\n"
    total = 0

    for key, value in stat.items():
        string += "{}: ${:.2f}\n".format(key, value[0])
        total += value[0]

    string += "\nTOTAL: ${:.2f}\n".format(total)
    
    stat_label["text"] = string
    

    
def createCSVFile(button) -> None:
    """ Create a new csv file. """
    file_name = button["text"] + ".csv"
    with open(file_name, "+w", newline="") as myCSVFile:
        writeToMyCSV = csv.writer(myCSVFile)
        writeToMyCSV.writerow(["PRODUCT", "PRICE ($)"])


def writeCSVFile(button, product, amount) -> None:
    """ Append the given data
    to the existed csv file. """
    file_name = button["text"] + ".csv"
    with open(file_name, "+a", newline="") as myCSVFile:
        writeToMyCSV = csv.writer(myCSVFile)
        writeToMyCSV.writerow([product, amount])

