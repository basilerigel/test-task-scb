from decimal import Decimal

from megatrader.logic.utils import (
    SerializedLot,
    calculate_lot_purchase_price,
    calculate_lot_profit,
    parse_data,
)


def test_calculate_lot_purchase_price():
    test_cases = [
        ((Decimal('1.005'), 1), Decimal('1005')),
        ((Decimal('0.15'), 1), Decimal('150')),
    ]
    for case, expected_result in test_cases:
        assert calculate_lot_purchase_price(percent=case[0], count=case[1]) == expected_result


def test_calculate_lot_profit():
    test_cases = [
        ((Decimal('1000'), 1), Decimal('30')),
        ((Decimal('5040'), 10), Decimal('5260')),
    ]
    for case, expected_result in test_cases:
        assert calculate_lot_profit(purchase_price=case[0], count=case[1]) == expected_result


def test_parse_data():
    expected_result = (
        Decimal('8000'),
        [
            SerializedLot(full_name='1 alfa-05 100.2 2\n', profit=Decimal('56.000'), price=Decimal('2004.000')),
            SerializedLot(full_name='2 alfa-05 101.5 5\n', profit=Decimal('75.000'), price=Decimal('5075.000')),
            SerializedLot(full_name='2 gazprom-07 100.0 2', profit=Decimal('60.0'), price=Decimal('2000.0'))
        ]
    )
    assert parse_data(file_path='../test_input') == expected_result


if __name__ == '__main__':
    test_calculate_lot_purchase_price()
    test_calculate_lot_profit()
    test_parse_data()
