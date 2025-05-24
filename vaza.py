import add
import math

def vaza(u, v):
    f=50-0.002*u**2
    x=f*math.cos(v)
    y=f*math.sin(v)
    z=u
    return (x, y, z)

min_u = 10     # flat bottom inner radius
max_u = 100      # outer radius
grid_u = 50       # radial detail
min_v = 0
max_v = 2 * math.pi
grid_v = 50       # angular detail
RGB = (255, 100, 100)  # brownish color

bottom_ring = [vaza(min_u, v) for v in [min_v + i*(max_v-min_v)/grid_v for i in range(grid_v + 1)]]
top_ring = [vaza(max_u, v) for v in [min_v + i*(max_v-min_v)/grid_v for i in range(grid_v + 1)]]

bottom_center = (0, 0, min_u)
top_center = (0, 0, max_u)

# Vertices list for both caps
cap_vertices = [bottom_center] + bottom_ring + [top_center] + top_ring
# Indices
N = len(add.vertices)  # get current vertex offset

faces = []

# Bottom cap triangles
for i in range(grid_v):
    faces.append(f'3 {N} {N+1+i+1} {N+1+i} {RGB[0]} {RGB[1]} {RGB[2]}')

# Top cap triangles
offset = N + 1 + (grid_v + 1)
for i in range(grid_v):
    faces.append(f'3 {offset} {offset+1+i} {offset+1+i+1} {RGB[0]} {RGB[1]} {RGB[2]}')

# Add the mesh
# Convert your cap vertices (which are tuples) to strings
cap_vertices_str = [f"{x} {y} {z}" for x, y, z in cap_vertices]

# Use mesh with string vertices
add.mesh([cap_vertices_str, faces])

add.parametric(vaza, min_u, max_u, grid_u, min_v, max_v, grid_v, RGB)

add.off('vaza.off')