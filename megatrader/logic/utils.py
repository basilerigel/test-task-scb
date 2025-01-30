from decimal import Decimal

from megatrader.logic.constants import COUPON_PAYMENT_DAYS, BOND
from collections import namedtuple

SerializedLot = namedtuple('SerializedLot', 'full_name profit price')
Balance = Decimal


def calculate_lot_purchase_price(*, percent: Decimal, count: int) -> Decimal:
    """
    Расчет цены покупки лота.
    """
    return BOND * count * percent


def calculate_lot_profit(*, purchase_price: Decimal, count: int) -> Decimal:
    """
    Расчет прибыльности лота на N+30 день (COUPON_PAYMENT_DAYS).
    """
    coupon_profit = count * COUPON_PAYMENT_DAYS
    recovery = count * BOND

    return coupon_profit + recovery - purchase_price


def parse_data(*,file_path: str) -> tuple[Balance, list[SerializedLot]]:
    """
    Парсинг файла.
    Пример входных данных:
        2 2 8000 (сколько длятся торги, сколько максимум облигаций в день, баланс трейдера)
        1 alfa-05 100.2 2 (день, название лота, цена, кол-во облигаций в лоте)
        2 alfa-05 101.5 5
        2 gazprom-07 100.0 2
    """
    data = []
    balance = None
    with open(file_path) as f:
        lines = f.readlines()
        is_header = True
        for line in lines:
            l = line.split()
            if is_header:
                balance = Decimal(l[2])
                is_header = False
                continue
            percent = Decimal(l[2]) / Decimal(100)
            count = int(l[3])
            price = calculate_lot_purchase_price(percent=percent, count=count)
            profit = calculate_lot_profit(purchase_price=price, count=count)
            data.append(
                SerializedLot(
                    full_name=line,
                    profit=profit,
                    price=price,
                )
            )

    return balance, data

def write_result(*, max_profit, strategy):
    """
    Запись результата в файл.
    """
    with open('result', 'w') as f:
        f.write(f'{str(max_profit)}\n')
        f.writelines(strategy)
