from FinanceR.TransactionHistory import TransactionHistory
from ConsoleGraphMaker.GraphMaker import GraphMaker

def main():
    filepath = input("Path to the .csv file > ")
    transactionHistory = TransactionHistory(filepath)
    transactionHistory.PrintTransactionAmounts()

    grapher = GraphMaker()
    grapher.DrawBarChart(transactionHistory.CreateDataSet())


if __name__ == "__main__":
    main()