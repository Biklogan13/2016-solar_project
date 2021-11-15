# coding: utf-8
# license: GPLv3

gravitational_constant = 1.17481
scale = 3153600000
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += (G * body.m * obj.m) * (obj.x - body.x) / (r**3)
        body.Fy += (G * body.m * obj.m) * (obj.y - body.y) / (r**3)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    body.x += body.Vx * (dt/scale) + 0.5 * ax * (dt/scale) ** 2
    body.Vx += ax * (dt/scale)

    ay = body.Fy / body.m
    body.y += body.Vy * (dt/scale) + 0.5 * ay * (dt/scale) ** 2
    body.Vy += ay * (dt/scale)


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
