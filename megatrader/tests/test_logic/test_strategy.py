from decimal import Decimal

from megatrader.logic.strategy import calculate_profit_strategy
from megatrader.logic.utils import SerializedLot

def test_calculate_profit_strategy():
    lots = [
        SerializedLot(full_name='1 alfa-05 100.2 2', profit=Decimal('56.000'), price=Decimal('2004.000')),
        SerializedLot(full_name='2 alfa-05 101.5 5', profit=Decimal('75.000'), price=Decimal('5075.000')),
        SerializedLot(full_name='2 gazprom-07 100.0 2', profit=Decimal('60.0'), price=Decimal('2000.0')),
    ]
    balance = Decimal('8000')
    expected_result = (Decimal('135.000'), ['2 alfa-05 101.5 5', '2 gazprom-07 100.0 2'])

    assert calculate_profit_strategy(lots=lots, total_balance=balance) == expected_result


if __name__=='__main__':
    test_calculate_profit_strategy()