from __future__ import annotations

from decimal import Decimal

from megatrader.logic.utils import SerializedLot
import copy


def calculate_profit_strategy(
        *,
        total_balance: Decimal,
        lots: list[SerializedLot]
) -> tuple[Decimal, list[str]]:
    """
    Подбор наиболее выгодной стратегии методом динамического программирования.
    """
    dp_mapping = {Decimal('0'): (Decimal('0'), [])}
    for lot in lots:
        dp_mapping_copy = copy.deepcopy(dp_mapping)
        lot_price, lot_profit = lot.price, lot.profit
        for price, (profit, strategy) in dp_mapping.items():
            new_price = price + lot_price
            new_profit = profit + lot_profit
            recurrent_conditions = [
                new_price <= total_balance,
                new_price not in dp_mapping_copy or new_profit > dp_mapping_copy[new_price][0],
            ]
            if all(recurrent_conditions):
                dp_mapping_copy[new_price] = (new_profit, strategy + [lot.full_name])

        dp_mapping = dp_mapping_copy

    max_profit, strategy = max(dp_mapping.values(), key=lambda x: x[0])

    return max_profit, strategy
