import pytest
from ConsoleGraphMaker.Graphmaker import GraphMaker

@pytest.mark.parametrize("test_input,expected", [
    ({"1": 5, "2": 10, "3": 2}, "1\t" + "#"*14 + "\n2\t" + "#"*29 + "\n3\t" + "#"*5 + "\n"),
])
def test_Draw3DataPoints(test_input, expected, capture_stdout):
    grapher = GraphMaker()
    grapher.DrawBarChart(test_input)
    assert capture_stdout["stdout"] == expected