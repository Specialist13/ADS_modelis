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

    add.off('lentyna.off')