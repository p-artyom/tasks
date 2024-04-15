def is_prime_number(number: int) -> bool:
    '''Проверка на простое число.'''
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def number_in_range(min_value: int, max_value: int) -> list[int]:
    '''Возвращает список всех простых чисел в заданном диапазоне.'''
    return [
        number
        for number in range(min_value, max_value + 1)
        if is_prime_number(number)
    ]
