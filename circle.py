import math


def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
                r (float) : радиус круга

        Возвращаемое значение:
                float : площадь круга с радиусом r
    ''' 
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности.

        Параметры:
                r (float) : радиус окружности

        Возвращаемое значение:
                float : длина окружности радиуса r
    ''' 
    return 2 * math.pi * r

