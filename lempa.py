import add
import math

def lempos_virsus(u, v):
    x = (10**((max_v-v+100)/100))*math.cos(u)**2* math.cos(u)
    z = (10**((max_v-v+100)/100))*math.sin(u)**2* math.sin(u)
    y = v
    return (x, y, z)

min_u = 0
max_u = 2 * math.pi
grid_u = 100
min_v = 150
max_v = 250
grid_v = 100

add.cylinder((0, 0, 0), (0, 10, 0), 30, 100, (0, 0, 0))
add.cylinder((0, 10, 0), (0, 200, 0), 5, 100, (0, 0, 1))
add.parametric(lempos_virsus, min_u, max_u, grid_u, min_v, max_v, grid_v, (0, 0, 1))



add.off("lempa.off")