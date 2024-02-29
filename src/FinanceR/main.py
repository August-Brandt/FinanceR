import csv
from FinanceR.transaction import Transaction
from datetime import datetime
from ConsoleGraphMaker.GraphMaker import GraphMaker

class TransactionHistory:
    def __init__(self, file: str) -> None:
        self.transactions = []
        self.LoadTransactionsFromCSV(file)

    def LoadTransactionsFromCSV(self, file: str) -> None:
        for row in self.ReadCsv(file)[1:]:
            self.transactions.append(self.CreateTransaction(row))

    @staticmethod
    def ReadCsv(file: str) -> list[list[str]]:
        rows = []
        with open(file, newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=";")
            for row in filereader:
                rows.append(row)
        
        return rows
    
    @staticmethod
    def CreateTransaction(row: list[str]) -> Transaction:
        return Transaction(float(row[4].replace(",", ".")), row[11], row[12], datetime.strptime(row[0], '%d.%m.%Y').date(), row[2])

    def PrintTransactionAmounts(self):
        for transaction in self.transactions:
            print(transaction.amount)
            print(transaction.date)

    def CreateDataSet(self) -> dict:
        dataSet = {}
        for transaction in self.transactions:
            if transaction.type not in dataSet.keys():
                dataSet[transaction.type] = 0
            
            dataSet[transaction.type] = dataSet[transaction.type] + transaction.amount
        
        return dataSet

def main():
    filepath = input("Path to the .csv file > ")
    transactionHistory = TransactionHistory(filepath)
    transactionHistory.PrintTransactionAmounts()

    grapher = GraphMaker()
    grapher.DrawBarChart(transactionHistory.CreateDataSet())


if __name__ == "__main__":
    main()