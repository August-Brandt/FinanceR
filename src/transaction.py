class Transaction:
    def __init__(self, amount, type, subtype, date, desciption=""):
        self.amount = amount
        self.type = type
        self.subtype = subtype
        self.date = date
        self.description = desciption
    