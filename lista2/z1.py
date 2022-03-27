import math
from typing import Callable
import asyncio


async def bubblesort(to_sort: list) -> list:
    listlen = len(to_sort)
    for i in range(listlen):
        for j in range(listlen - i - 1):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    return to_sort


async def bubblesort_smart(to_sort: list) -> list:
    listlen = len(to_sort)
    for i in range(listlen):
        done = True
        for j in range(listlen - i - 1):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
                done = False
        if done:
            break
    return to_sort


async def bubblesort_naive(to_sort: list) -> list:
    listlen = len(to_sort)
    for i in range(listlen):
        for j in range(listlen - 1):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    return to_sort


async def insertionsort(to_sort: list) -> list:
    for i in range(1, len(to_sort)):
        _key = to_sort[i]
        j = i - 1
        while j >= 0 and _key < to_sort[j]:
            to_sort[j + 1] = to_sort[j]
            j -= 1
        to_sort[j + 1] = _key
    return to_sort


async def selectionsort(to_sort: list) -> list:
    listlen = len(to_sort)
    for i in range(listlen):
        for j in range(i + 1, listlen):
            if to_sort[i] > to_sort[j]:
                temp = to_sort[i]
                to_sort[i] = to_sort[j]
                to_sort[j] = temp
    return to_sort


# todo: schematy blokowe

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import pandas as pd
    import random
    import timeit


    def test_alg(_list: list, alg: Callable):
        start = timeit.default_timer()
        asyncio.run(alg(_list))
        end = timeit.default_timer()
        dt = end - start
        return dt


    def bubble_test_n(n: int, _len) -> dict:
        _lists = []
        for i in range(n):
            _lists.append([random.randint(0, 1000000) for _ in range(_len)])
        bubble = [test_alg(_list[:], bubblesort) for _list in _lists]
        bubble_smart = [test_alg(_list[:], bubblesort_smart) for _list in _lists]
        bubble_naive = [test_alg(_list[:], bubblesort_naive) for _list in _lists]
        results = {'Bubble sort': bubble, 'Bubble sort 1': bubble_smart, 'Bubble sort naiwny': bubble_naive}
        return results


    def test_n(n: int, _len: int = 10) -> dict:
        _lists = []
        for i in range(n):
            _lists.append([random.randint(0, 1000000) for _ in range(_len)])
        bubble = [test_alg(_list[:], bubblesort) for _list in _lists]
        insertion = [test_alg(_list[:], insertionsort) for _list in _lists]
        selection = [test_alg(_list[:], selectionsort) for _list in _lists]
        results = {'Bubble sort': bubble, 'Selection sort': selection, 'Insertion sort': insertion}
        return results


    """podpunkt 2"""
    pd_2 = [10, 20, 50, 100, 200, 500, 1000]
    _n = random.randint(1, 500)
    print(f'b) Wyniki dla 10 przebiegów algorytmów dla listy złożonej z {_n} liczb:')
    for key, test in test_n(10, _n).items():
        _txt = f'{key}:\n\tavg: {sum(test) / len(test) * 1000} ms\n\tmax: {max(test) * 1000} ms'
        print(_txt)

    """podpunkt 3"""
    ticks = [10, 20, 50, 100, 200, 500, 1000]
    results_avg = {}
    results_max = {}
    for tick in ticks:
        test_case = test_n(10, tick)
        for key, test in test_case.items():
            if key not in results_avg:
                results_avg[key] = {}
            if key not in results_max:
                results_max[key] = {}
            results_avg[key][str(tick)] = sum(test) / len(test) * 1000
            results_max[key][str(tick)] = max(test) * 1000
    fig = plt.figure("Podpunkt 3")
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_xlabel('Długość ciągu')
    ax1.set_ylabel('Czas [ms]')
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_xlabel('Długość ciągu')
    ax2.set_ylabel('Czas [ms]')
    df1 = pd.DataFrame(results_avg)
    df2 = pd.DataFrame(results_max)
    df1.plot(ax=ax1, title='Średni czas sortowania dla danej długości ciągu')
    df2.plot(ax=ax2, title='Maksymalny czas sortowania')
    plt.tight_layout()
    plt.autoscale()
    plt.show()

    """podpunkt 5"""
    ticks = [10, 20, 50, 100, 200, 500, 1000]
    results_avg = {}
    results_max = {}
    for tick in ticks:
        test_case = bubble_test_n(10, tick)
        for key, test in test_case.items():
            if key not in results_avg:
                results_avg[key] = {}
            if key not in results_max:
                results_max[key] = {}
            results_avg[key][str(tick)] = sum(test) / len(test) * 1000
            results_max[key][str(tick)] = max(test) * 1000
    bubble_fig = plt.figure("Podpunkt 5")
    ax1 = bubble_fig.add_subplot(2, 1, 1)
    ax1.set_xlabel('Długość ciągu')
    ax1.set_ylabel('Czas [ms]')
    ax2 = bubble_fig.add_subplot(2, 1, 2)
    ax2.set_xlabel('Długość ciągu')
    ax2.set_ylabel('Czas [ms]')
    bubble_df1 = pd.DataFrame(results_avg)
    bubble_df2 = pd.DataFrame(results_max)
    bubble_df1.plot(ax=ax1, title='Średni czas sortowania dla danej długości ciągu')
    bubble_df2.plot(ax=ax2, title='Maksymalny czas sortowania')
    plt.tight_layout()
    plt.show()

    """Podpunkt ostatni"""
    _n_list = [10, 100, 1000]
    _table = {}
    for _n in _n_list:
        eff_test = test_n(1, _n)
        _table[str(_n)] = {}
        print(f'testy wydajnościowe dla n = {_n}:')
        print(f'{"algorytm":<15} | {"n":<4} | {"t(n)":<20}  | {"n * log(n) / n":<20}')
        for key, _time in eff_test.items():
            _txt = f'{key:<15} | {_n:<4} | {_time[0]:<20} | {_n * math.log(_n) / _time[0]:<20}'
            print(_txt)
        print(f'\n')
    """
    for tick in ticks:
        test_case = test_n(10, tick)
        for key, test in test_case.items():
            if key not in results_avg:
                results_avg[key] = {}
            if key not in results_max:
                results_max[key] = {}
            results_avg[key][str(tick)] = sum(test) / len(test) * 1000
            results_max[key][str(tick)] = max(test) * 1000
    """
