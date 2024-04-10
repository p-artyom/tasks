import unittest

from tasks.number_in_range import number_in_range
from tasks.point import Point
from tasks.sorted_string import sorted_string, sorted_string_bubble
from tasks.unique_elements import unique_elements


class TestUniqueElements(unittest.TestCase):
    '''Функция unique_elements возвращает корректные значения.'''

    def test_unique_elements(self):
        self.assertAlmostEqual(
            unique_elements([1, 1, 2, 2, 4, 5, 6]),
            [1, 2, 4, 5, 6],
        )


class TestNumberInRange(unittest.TestCase):
    '''Функция number_in_range возвращает корректные значения.'''

    def test_number_in_range(self):
        self.assertAlmostEqual(
            number_in_range(1, 20),
            [2, 3, 5, 7, 11, 13, 17, 19],
        )


class TestPoint(unittest.TestCase):
    '''Все функции класса Point работают корректно.'''

    def test_point(self):
        first_point = Point(1, 2)
        self.assertAlmostEqual(
            first_point.get_cordinates(),
            (1, 2),
        )
        first_point.set_cordinates(3, 4)
        self.assertAlmostEqual(
            first_point.get_cordinates(),
            (3, 4),
        )
        second_point = Point(6, 8)
        self.assertAlmostEqual(
            first_point.distance(second_point),
            5.0,
        )


class TestSorted(unittest.TestCase):
    '''Функции сортировки возвращают корректные значения.'''

    def test_sorted_string(self):
        TEST_DATA = ['list', 'string', 'tuple', 'set']

        first_gen = sorted_string_bubble(TEST_DATA)
        second_gen = sorted_string(TEST_DATA)
        self.assertAlmostEqual(
            next(first_gen),
            ['set', 'list', 'tuple', 'string'],
        )
        self.assertAlmostEqual(
            next(second_gen),
            ['set', 'list', 'tuple', 'string'],
        )
        self.assertAlmostEqual(
            next(first_gen),
            ['string', 'tuple', 'list', 'set'],
        )
        self.assertAlmostEqual(
            next(second_gen),
            ['string', 'tuple', 'list', 'set'],
        )


if __name__ == '__main__':
    unittest.main()
