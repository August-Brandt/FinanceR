from datetime import date

class Transaction:
    def __init__(self, amount: float, type: str, subtype: str, date: date, description="") -> None:
        self.amount = amount
        self.type = type
        self.subtype = subtype
        self.date = date
        self.description = description
    