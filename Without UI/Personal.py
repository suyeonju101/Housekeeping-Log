import csv


class Personal:
    def __init__(self):
        self.product = ""
        self.amount = 0
        self.total_amount = 0

    def setProduct(self, product: str):
        self.product = product

    def setAmount(self, amount: float):
        self.amount = amount

    def getAmount(self) -> float:
        return self.total_amount
    
    def updateTotalAmount(self):
        self.total_amount += self.amount

    def createCSVFile(self):
        with open("PERSONAL.csv", "+w", newline="") as myCSVFile:
            writeToMyCSV = csv.writer(myCSVFile)
            writeToMyCSV.writerow(["PRODUCT", "AMOUNT ($)"])

    def writeCSVFile(self):
        with open("PERSONAL.csv", "+a", newline="") as myCSVFile:
            writeToMyCSV = csv.writer(myCSVFile)
            writeToMyCSV.writerow([self.product, self.amount])
