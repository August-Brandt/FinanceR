
class GraphMaker:
    def DrawBarChart(self, data: dict) -> None:
        datasum = sum(data.values())
        for dataname, datapoint in zip(data.keys(), data.values()):
            print(dataname + "\t" + "#"*int(datapoint/datasum*50))


if __name__ == "__main__":
    graphMaker = GraphMaker()
    # data = {"1": 5, "2": 10, "3": 2, "4": 5, "5": 14, "6": 7}
    # data = {"1": 5, "2": 10, "3": 2, "123": 30}
    data = {"Food": 5500, "House": 7435, "Transport": 2300, "Other": 4203}
    graphMaker.DrawBarChart(data)