import math

class GraphMaker:
    def CreateBarChart(self, data: dict) -> list[str]:
        longestTitle = len(max(data.keys(), key=len))
        datasum = sum(data.values())
        chart = []
        for dataname, datapoint in zip(data.keys(), data.values()):
            if len(dataname) > 14:
                chart.append(dataname[:10] + "..." + "\t" + "#" * int(datapoint/datasum*50))
            elif len(dataname) > 7:
                chart.append(dataname + "\t" + "#" * int(datapoint/datasum*50))
            else:
                chart.append(dataname + "\t"*min(math.ceil(longestTitle/7), 2) + "#"*int(datapoint/datasum*50))
        return chart

    def DrawBarChart(self, data: dict) -> None:
        print("\n".join(self.CreateBarChart(data)))


if __name__ == "__main__":
    graphMaker = GraphMaker()
    # data = {"1": 5, "2": 10, "3": 2, "4": 5, "5": 14, "6": 7}
    # data = {"1": 5, "2": 10, "3": 2, "123": 30}
    data = {"Food": 5500, "House": 7435, "Transportabcde": 2300, "Other": 4203}
    graphMaker.DrawBarChart(data)