import add
import math

def board_component(center=[0,0,0], w=10, l=5, color=(0, 0, 255)):
    vertical_piece = [1, w+1, l]
    horizontal_piece = [w-1, 1, 1]
    cx, cy, cz = center
    # add.rectangle3D([cx-w/2,cy,cz], vertical_piece, color)
    add.rectangle3D([cx+w/2, cy, cz], vertical_piece, color)

    add.rectangle3D([cx, cy - w / 2, cz - math.trunc(l / 2)], horizontal_piece, color)
    add.rectangle3D([cx, cy-w/2+w, cz-math.trunc(l / 2)], horizontal_piece, color)
    add.rectangle3D([cx, cy+w/2, cz+math.trunc(l / 2)], horizontal_piece, color)
    add.rectangle3D([cx, cy+w/2-w, cz+math.trunc(l / 2)], horizontal_piece, color)


def edge(center=[0,0,0], w=10, l=5, color=(0, 0, 255)):
    cx, cy, cz = center
    vertical_piece = [1, w + 1, l]
    add.rectangle3D([cx - w / 2, cy, cz], vertical_piece, color)

def bottom(center=[0,0,0], w=10, l=5, color=(0, 0, 255)):
    cx, cy, cz = center
    horizontal_piece = [w-1, 1, l]
    add.rectangle3D([cx, cy-w/2, cz], horizontal_piece, color)

def helix(t):
    r = 5
    return [r * math.cos(t), r * math.sin(t), 2]

def circle_at(t, x=0, y=0, l=5):
    r = 4.5
    z= math.trunc(l/2)
    return [r * math.cos(t) + x, r * math.sin(t) + y, z]

width = 10
lenght = 5
color = (0, 0, 255)
circle_quality = 10

for i in range(6):
    # Edge here to reduce overlaps :)
    edge([0, i*10, 0], width, lenght, color)
    for j in range(7):
        board_component([j*10, i*10, 0], width, lenght, color)
    bottom([i*10, 0, 0], width, lenght, color)
bottom([6*10, 0, 0], width, lenght, color)
# Create circles at different positions

for i in range(6):
    for j in range(7):
        # Create a circle at position [j*10, i*10, 0]
        def current_circle(t):
            return circle_at(t, j * 10, i * 10, lenght)
        def current_circle2(t):
            return circle_at(t, j * 10, i * 10, -lenght)
        add.curve(current_circle, 0, 2 * math.pi, circle_quality, 5, 0.5, color, False)
        add.curve(current_circle2, 0, 2 * math.pi, circle_quality, 5, 0.5, color, False)

board_component([0, 0, 0], width, lenght, color)

add.off("board.off")