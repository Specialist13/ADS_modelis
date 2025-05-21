import add
import math

def generate_board(board):
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

    # cia bsk chatuko kodas tbf
    def add3DDisc(x, y, thickness=5, radius=4.5, segments=10, color=(255, 0, 0)):
        """
        Creates a 3D disc (cylinder) centered between lenght and -lenght.

        Args:
            x, y: Position coordinates (grid coordinates, will be multiplied by 10)
            thickness: Thickness of the disc in z-direction
            radius: Disc radius
            segments: Number of segments used to approximate the circle
            color: RGB color tuple
        """
        # Convert grid coordinates to actual coordinates
        cx, cy = x * 10, y * 10
        z_top = thickness / 2
        z_bottom = -thickness / 2

        # Create vertices for top and bottom faces
        top_center_index = len(add.vertices)
        add.vertices.append(f"{cx} {cy} {z_top}")
        bottom_center_index = len(add.vertices)
        add.vertices.append(f"{cx} {cy} {z_bottom}")

        # Create vertices around the circle (top and bottom)
        top_start_index = len(add.vertices)
        for i in range(segments):
            angle = 2 * math.pi * i / segments
            vx = cx + radius * math.cos(angle)
            vy = cy + radius * math.sin(angle)
            # Top vertex
            add.vertices.append(f"{vx} {vy} {z_top}")
            # Bottom vertex
            add.vertices.append(f"{vx} {vy} {z_bottom}")

        # Create top face triangles
        for i in range(segments):
            v1 = top_center_index
            v2 = top_start_index + i * 2
            v3 = top_start_index + ((i + 1) % segments) * 2
            face = f"3 {v1} {v2} {v3} {color[0]} {color[1]} {color[2]}"
            add.faces.append(face)

        # Create bottom face triangles
        for i in range(segments):
            v1 = bottom_center_index
            v2 = top_start_index + ((i + 1) % segments) * 2 + 1
            v3 = top_start_index + i * 2 + 1
            face = f"3 {v1} {v2} {v3} {color[0]} {color[1]} {color[2]}"
            add.faces.append(face)

        # Create side quad faces
        for i in range(segments):
            v1 = top_start_index + i * 2
            v2 = top_start_index + ((i + 1) % segments) * 2
            v3 = top_start_index + ((i + 1) % segments) * 2 + 1
            v4 = top_start_index + i * 2 + 1
            face = f"4 {v1} {v2} {v3} {v4} {color[0]} {color[1]} {color[2]}"
            add.faces.append(face)

    # Example usage - creates discs with thickness equal to the board thickness
    # add3DDisc(3, 0, lenght-3, color=(255, 0, 0))  # Red disc at position (3,1)
    # add3DDisc(4, 0, lenght-3, color=(255, 255, 0))  # Yellow disc at position (4,1)
    for i in range(6):
        for j in range(7):
            if board[i][j] == 'X':
                add3DDisc(j, 5-i, lenght-3, color=(255, 0, 0))
            elif board[i][j] == 'O':
                add3DDisc(j, 5-i, lenght-3, color=(255, 255, 0))


    add.off("board.off")