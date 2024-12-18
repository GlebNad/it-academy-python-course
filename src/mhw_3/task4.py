"""Element pairs.
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def element_pairs(seq: str) -> str:
    """
    Count number of pairs element of sequence has.

    Args:
        seq (str): Sequence to check.

    Return:
        str: element and number of pairs.
    """
    seq_set = set(seq.split())
    elements_amount = [seq.split().count(element) for element in seq_set]
    num_pairs = [0 for _ in range(len(elements_amount))]
    for ind, num in enumerate(elements_amount):
        for count in range(num):
            num_pairs[ind] += count
    answer_list = [
        '{0}: {1}'. format(key, value) for
        key, value in zip(seq_set, num_pairs)
    ]
    return ', '.join(answer_list)


print(element_pairs(input('Введите последовательность: ')))
