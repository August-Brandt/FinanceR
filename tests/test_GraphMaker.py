import pytest
from ConsoleGraphMaker.Graphmaker import GraphMaker

@pytest.mark.parametrize("test_input,expected", [
    ({"1": 5, "2": 10, "3": 2}, 
        "1\t" + "#"*14 + "\n2\t" + "#"*29 + "\n3\t" + "#"*5 + "\n"),
    ({"10": 40, "11": 30, "12": 67}, 
        "10\t" + "#"*14 + "\n11\t" + "#"*10 + "\n12\t" + "#"*24 + "\n"),
    ({"100": 5500, "120": 7435, "90": 2300, "154": 4203}, 
        "100\t" + "#"*14 + "\n120\t" + "#"*19 + "\n90\t" + "#"*5 + "\n154\t" + "#"*10 + "\n")
])
def test_DrawNumberDataPoints(test_input, expected, capture_stdout):
    grapher = GraphMaker()
    grapher.DrawBarChart(test_input)
    assert capture_stdout["stdout"] == expected

@pytest.mark.parametrize("test_input,expected", [
    ({"a": 5, "b": 10, "c": 2},
        "a\t" + "#"*14 + "\nb\t" + "#"*29 + "\nc\t" + "#"*5 + "\n"),
    ({"aa": 40, "bb": 30, "cc": 67},
        "aa\t" + "#"*14 + "\nbb\t" + "#"*10 + "\ncc\t" + "#"*24 + "\n"),
    ({"Food": 5500, "House": 7435, "Transport": 2300, "Other": 4203},
        "Food\t" + "#"*14 + "\nHouse\t" + "#"*19 + "\nTransport\t" + "#"*5 + "\nOther\t" + "#"*10 + "\n")
])
def test_DrawStringDataPoints(test_input, expected, capture_stdout):
    grapher = GraphMaker()
    grapher.DrawBarChart(test_input)
    assert capture_stdout["stdout"] == expected