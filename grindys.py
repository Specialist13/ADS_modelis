import add
import math

for i in range (20):
    for j in range (20):
        if (i+j) % 2 == 0:
            add.rectangle3D((i*35, 0, j*35), (35, 1, 35), (194, 142, 100))
        else:
            add.rectangle3D((i*35, 0, j*35), (35, 1, 35), (227, 223, 200))

add.off('grindys.off')