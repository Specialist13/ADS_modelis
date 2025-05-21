import add
import math

add.rectangle3D((60, 0, 60), (20, 150, 20), (204, 102, 0))
add.rectangle3D((60, 0, -60), (20, 150, 20), (204, 102, 0))
add.rectangle3D((-60, 0, 60), (20, 150, 20), (204, 102, 0))
add.rectangle3D((-60, 0, -60), (20, 150, 20), (204, 102, 0))
add.rectangle3D((0, 80, 0), (150, 10, 150), (204, 102, 0))

add.off('stalas.off')