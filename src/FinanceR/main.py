import csv
from FinanceR.transaction import Transaction
from datetime import date

# Returns a list of rows from the passed .csv file 
def ReadCsv(filepath: str) -> list:
    rows = []
    with open(filepath, newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=";")
        for row in filereader:
            rows.append(row)
    
    return rows


def CreateTransaction(row: list) -> Transaction:
    return Transaction(float(row[4].replace(",", ".")), row[11], row[12], date.strptime(row[0], '%d.%m.%Y'), row[2])

def CreateDataSet(transactions: list) -> dict:
    dataSet = {}
    for transaction in transactions:
        if transaction.type not in dataSet.keys():
            dataSet[transaction] = 0
        
        dataSet[transaction] = dataSet[transaction] + transaction.amount
    
    return dataSet

def main():
    filepath = input("Path to the .csv file > ")
    transactions = []
    for row in ReadCsv(filepath)[1:]:
        transactions.append(CreateTransaction(row))
    for _transaction in transactions:
        print(_transaction.amount)


if __name__ == "__main__":
    main()