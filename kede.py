import add
import math

def generate_kede():
    add.rectangle3D((20, 0, 20), (14, 80, 14), (204, 102, 0))
    add.rectangle3D((20, 0, -20), (14, 80, 14), (204, 102, 0))
    add.rectangle3D((-20, 0, 20), (14, 80, 14), (204, 102, 0))
    add.rectangle3D((-20, 0, -20), (14, 80, 14), (204, 102, 0))
    add.rectangle3D((0, 45, 0), (60, 10, 60), (204, 102, 0))
    add.rectangle3D((25, 80, 25), (10, 60, 10), (204, 102, 0))
    add.rectangle3D((25, 80, -25), (10, 60, 10), (204, 102, 0))
    add.rectangle3D((25, 80, 12), (7, 60, 7), (204, 102, 0))
    add.rectangle3D((25, 80, -12), (7, 60, 7), (204, 102, 0))
    add.rectangle3D((25, 80, 0), (7, 60, 7), (204, 102, 0))
    add.rectangle3D((25, 115, 0), (10, 10, 60), (204, 102, 0))

    add.off('kede.off')