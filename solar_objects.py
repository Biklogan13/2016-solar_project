# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды в массах земли"""

    x = 0
    """Координата по оси **x** в астрономических единицах"""

    y = 0
    """Координата по оси **y** в астрономических единицах"""

    Vx = 0
    """Скорость по оси **x** в км/с"""

    Vy = 0
    """Скорость по оси **y** в км/с"""

    Fx = 0
    """Сила по оси **x** """

    Fy = 0
    """Сила по оси **y** """

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты в массах земли"""

    x = 0
    """Координата по оси **x** в астрономических единицах"""

    y = 0
    """Координата по оси **y** в астрономических единицах"""

    Vx = 0
    """Скорость по оси **x** в км/с"""

    Vy = 0
    """Скорость по оси **y** в км/с"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""