from .calculator_4 import Calculator4
from pytest import raises
from typing import Dict
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate_average_with_empty_list():
    mock_request = MockRequest({"numbers": []})
    calculator_4 = Calculator4()
    with raises(HttpUnprocessableEntityError) as excinfo:
        calculator_4.calculate_average(mock_request.json["numbers"])

    assert str(excinfo.value) == "Lista de números não fornecida ou mal formatada!"


def test_calculate_average_with_valid_numbers():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_4 = Calculator4()
    response = calculator_4.calculate_average(mock_request.json["numbers"])

    assert response == {
        'data': {'Calculator': 4, 'average': 20.8}
    }
