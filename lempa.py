import add
import math

def lempos_virsus(u, v):
    x = (10**(0.95*(max_v-v+100)/100))*math.cos(u)**2* math.cos(u)
    z = (10**(0.95*(max_v-v+100)/100))*math.sin(u)**2* math.sin(u)
    y = v
    return (-x, y, z)

min_u = 0
max_u = 2 * math.pi
grid_u = 100
min_v = 150
max_v = 220
grid_v = 100

add.cylinder((0, 0, 0), (0, 10, 0), 30, 100, (185, 161, 121))
add.cylinder((0, 10, 0), (0, 200, 0), 5, 100, (185, 161, 121))
add.parametric(lempos_virsus, min_u, max_u, grid_u, min_v, max_v, grid_v, (255, 255, 255))

# Create a center point for the cap
cap_center = [0, max_v, 0]
top_ring = []

for i in range(grid_u + 1):
    u = min_u + (max_u - min_u) * i / grid_u
    x, y, z = lempos_virsus(u, max_v)
    top_ring.append((x, y, z))

# Add the center vertex
center_index = len(add.vertices)
add.vertices.append(f"{cap_center[0]} {cap_center[1]} {cap_center[2]}")

# Add the ring vertices
ring_indices = []
for pt in top_ring:
    add.vertices.append(f"{pt[0]} {pt[1]} {pt[2]}")
    ring_indices.append(len(add.vertices) - 1)

# Add triangle faces (fan)
for i in range(len(ring_indices) - 1):
    a = ring_indices[i]
    b = ring_indices[i + 1]
    c = center_index
    add.faces.append(f"3 {a} {b} {c} 255 255 255")




add.off("lempa.off")