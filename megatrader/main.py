from megatrader.logic.strategy import calculate_profit_strategy
from megatrader.logic.utils import parse_data, write_result


def process():
    balance, lots = parse_data(file_path='trading_data')
    max_profit, strategy = calculate_profit_strategy(total_balance=balance, lots=lots)
    write_result(max_profit=max_profit, strategy=strategy)

if __name__ =='__main__':
    process()