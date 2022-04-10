import csv


class Uber:
    def __init__(self):
        self.trip = ""
        self.amount = 0
        self.total_amount = 0

    def setTrip(self, trip: str):
        self.trip = trip

    def setAmount(self, amount: float):
        self.amount = amount

    def getAmount(self) -> float:
        return self.total_amount
    
    def updateTotalAmount(self):
        self.total_amount += self.amount

    def createCSVFile(self):
        with open("UBER.csv", "+w", newline="") as myCSVFile:
            writeToMyCSV = csv.writer(myCSVFile)
            writeToMyCSV.writerow(["TRIP", "AMOUNT ($)"])
                     
    def writeCSVFile(self):
        with open("UBER.csv", "+a", newline="") as myCSVFile:
            writeToMyCSV = csv.writer(myCSVFile)
            writeToMyCSV.writerow([self.trip, self.amount])
