"""
Долевое строительство
Дан набор из N долей, представленных в виде N рациональных. Необходимо представить
эти доли в процентном выражении c точностью до трех знаков после запятой.

Входные данные:
Первая строка содержит значение N - число долей, каждая последующая содержит
числовое выражение доли.


Выходные данные:
N строк с процентным выражением долей. Значение в строке k является процентным
выражение доли из строки k+1 входных данных.
[0.125, 0.250, 0.500, 0.125]
"""


def calculate_ratios(*, ratios: list[float]) -> list[float]:
    ratios_sum = sum(ratios)
    result = []
    for ratio in ratios:
        result.append(float('{:.3f}'.format(ratio / ratios_sum)))

    return result


if __name__ == '__main__':
    print('Enter ratios count:')
    ratios_count = int(input())
    print('Enter ratios by lines:')
    ratios = [float(input()) for _ in range(ratios_count)]

    print(calculate_ratios(ratios=ratios))
