import pytest
from FinanceR.TransactionHistory import TransactionHistory


def test_ReadingCsv():
    transactionHistory = TransactionHistory("data/correctFormat.csv")
    assert transactionHistory.transactions[0].amount == 90.5

def test_CreateDataSet():
    transactionHistory = TransactionHistory ("data/correctFormat.csv")
    assert transactionHistory.CreateDataSet() == {"Food": 90.5}