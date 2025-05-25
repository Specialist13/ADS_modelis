import random

import add
import math


def generate_lentyna():
    add.rectangle3D((0, 0, 0), (10, 280, 300), (204, 102, 0))
    add.rectangle3D((55, -135, 0), (100, 10, 280), (204, 102, 0))
    add.rectangle3D((55, 0, -145), (100, 280, 10), (204, 102, 0))
    add.rectangle3D((55, 0, 145), (100, 280, 10), (204, 102, 0))
    # apatine dalis
    add.rectangle3D((55, -30, 0), (100, 10, 280), (204, 102, 0))
    add.rectangle3D((55, -82.5, 0), (100, 95, 10), (204, 102, 0))
    add.rectangle3D((95, -82.5, 72.5), (10, 95, 135), (204, 102, 0))
    add.rectangle3D((95, -82.5, -72.5), (10, 95, 135), (204, 102, 0))
    add.sphere((103, -77.5, -20), 5, 10, (204, 102, 0))
    add.sphere((103, -77.5, 20), 5, 10, (204, 102, 0))
    # virsutine dalis
    add.rectangle3D((55, 25, 0), (100, 10, 280), (204, 102, 0))
    add.rectangle3D((55, 80, 0), (100, 10, 280), (204, 102, 0))
    add.rectangle3D((55, 135, 0), (100, 10, 280), (204, 102, 0))

    for i in range(3):  # kad i visas lentynas idet
        y = i * 55 - 25
        z_position = -140

        while z_position < 140:
            plotis = random.randint(5, 20)
            aukstis = random.randint(30, 54)
            storis = random.randint(5, 30)

            if z_position + storis > 140:
                break

            color = (random.randint(0, 180), random.randint(0, 180), random.randint(0, 150))

            book_center_z = z_position + storis / 2
            add.rectangle3D((55, y + aukstis / 2, book_center_z), (plotis, aukstis, storis), color)

            z_position += storis


    add.off('lentyna.off')

