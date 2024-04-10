from typing import Generator


def bubble_sort(data: list[str]) -> list[str]:
    '''Сортировка пузырьком.'''
    last_index = len(data) - 1
    swapped = True
    while swapped:
        swapped = False
        for item_index in range(last_index):
            if len(data[item_index]) > len(data[item_index + 1]):
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1],
                    data[item_index],
                )
                swapped = True
        last_index -= 1
    return data


def sorted_string_bubble(data: list[str]) -> Generator[list[str], None, None]:
    '''Сортировка пузырьком, сначала по возрастанию, а затем по убыванию.'''
    yield bubble_sort(data.copy())
    yield bubble_sort(data.copy())[::-1]


def sorted_string(data: list[str]) -> Generator[list[str], None, None]:
    '''Сортировка встроенной функцией.'''
    yield sorted(data, key=len)
    yield sorted(data, key=len, reverse=True)
