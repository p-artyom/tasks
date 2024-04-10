import math
from typing import Tuple


class Point:
    '''Класс, который представляет собой точку в двумерном пространстве.'''

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def distance(self, other_point: 'Point') -> float:
        '''Вычислить расстояние до другой точки.'''
        return math.sqrt(
            (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2,
        )

    def get_cordinates(self) -> Tuple[int, int]:
        '''Получить координаты.'''
        return (self.x, self.y)

    def set_cordinates(self, x: float, y: float) -> None:
        '''Изменить координаты.'''
        self.x = x
        self.y = y
        return f'Новые координаты: {self.x, self.y}'
