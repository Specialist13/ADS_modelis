import add
import math

# Constants for customization
DEFAULT_BOARD_COLOR = (0, 0, 255)  # Blue
PLAYER_X_COLOR = (255, 0, 0)  # Red
PLAYER_O_COLOR = (255, 255, 0)  # Yellow
DEFAULT_WIDTH = 10
DEFAULT_LENGTH = 5
DEFAULT_CIRCLE_QUALITY = 10
DEFAULT_DISC_RADIUS = 4.5
DEFAULT_DISC_SEGMENTS = 10

#chatukas graziau suformatavo mano messy koda (kurio dalis irgi buvo chatuko parasyta xdd)
def create_board_component(center, width=DEFAULT_WIDTH, length=DEFAULT_LENGTH, color=DEFAULT_BOARD_COLOR):
    """Create a single board component (cell)."""
    cx, cy, cz = center
    vertical_piece = [1, width + 1, length]
    horizontal_piece = [width - 1, 1, 1]
    half_length = math.trunc(length / 2)

    # Vertical piece
    add.rectangle3D([cx + width / 2, cy, cz], vertical_piece, color)

    # Horizontal pieces
    add.rectangle3D([cx, cy - width / 2, cz - half_length], horizontal_piece, color)
    add.rectangle3D([cx, cy - width / 2 + width, cz - half_length], horizontal_piece, color)
    add.rectangle3D([cx, cy + width / 2, cz + half_length], horizontal_piece, color)
    add.rectangle3D([cx, cy + width / 2 - width, cz + half_length], horizontal_piece, color)


def create_edge(center, width=DEFAULT_WIDTH, length=DEFAULT_LENGTH, color=DEFAULT_BOARD_COLOR):
    """Create a vertical edge piece."""
    cx, cy, cz = center
    vertical_piece = [1, width + 1, length]
    add.rectangle3D([cx - width / 2, cy, cz], vertical_piece, color)


def create_bottom(center, width=DEFAULT_WIDTH, length=DEFAULT_LENGTH, color=DEFAULT_BOARD_COLOR):
    """Create a bottom piece."""
    cx, cy, cz = center
    horizontal_piece = [width - 1, 1, length]
    add.rectangle3D([cx, cy - width / 2, cz], horizontal_piece, color)


def create_circle(center_x, center_y, length=DEFAULT_LENGTH, quality=DEFAULT_CIRCLE_QUALITY,
                  radius=DEFAULT_DISC_RADIUS, color=DEFAULT_BOARD_COLOR):
    """Create circles at the specified position."""
    half_length = math.trunc(length / 2)

    def circle_at(t, z):
        return [radius * math.cos(t) + center_x, radius * math.sin(t) + center_y, z]

    # Create top and bottom circles
    add.curve(lambda t: circle_at(t, half_length), 0, 2 * math.pi, quality, 5, 0.5, color, False)
    add.curve(lambda t: circle_at(t, -half_length), 0, 2 * math.pi, quality, 5, 0.5, color, False)


def create_column_number(column, width=DEFAULT_WIDTH):
    """Create and position a 3D number for column identification."""
    vertices, faces = add.load(f"numbers/{column + 1}.off")
    number_mesh = [vertices, faces]

    number_mesh = add.zoom(number_mesh, 0.7)
    center = add.center(number_mesh)

    number_mesh = add.move(number_mesh, [column * width - center[0], -width / 2, -center[2] + 3])
    number_mesh = add.color(number_mesh, [255, 255, 255])
    add.mesh(number_mesh)


def create_game_piece(x, y, piece_type, thickness, radius=DEFAULT_DISC_RADIUS, segments=DEFAULT_DISC_SEGMENTS):
    """Create a 3D disc representing a player's piece."""
    color = PLAYER_X_COLOR if piece_type == 'X' else PLAYER_O_COLOR

    cx, cy = x * DEFAULT_WIDTH, y * DEFAULT_WIDTH
    z_top = thickness / 2
    z_bottom = -thickness / 2

    # Create vertices for top and bottom faces
    top_center_index = len(add.vertices)
    add.vertices.append(f"{cx} {cy} {z_top}")
    bottom_center_index = len(add.vertices)
    add.vertices.append(f"{cx} {cy} {z_bottom}")

    # Create vertices around the circle
    top_start_index = len(add.vertices)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        vx = cx + radius * math.cos(angle)
        vy = cy + radius * math.sin(angle)
        add.vertices.append(f"{vx} {vy} {z_top}")  # Top vertex
        add.vertices.append(f"{vx} {vy} {z_bottom}")  # Bottom vertex

    # Create faces
    for i in range(segments):
        # Top face triangles
        v1, v2 = top_center_index, top_start_index + i * 2
        v3 = top_start_index + ((i + 1) % segments) * 2
        add.faces.append(f"3 {v1} {v2} {v3} {color[0]} {color[1]} {color[2]}")

        # Bottom face triangles
        v1, v2 = bottom_center_index, top_start_index + ((i + 1) % segments) * 2 + 1
        v3 = top_start_index + i * 2 + 1
        add.faces.append(f"3 {v1} {v2} {v3} {color[0]} {color[1]} {color[2]}")

        # Side quad faces
        v1, v2 = top_start_index + i * 2, top_start_index + ((i + 1) % segments) * 2
        v3 = top_start_index + ((i + 1) % segments) * 2 + 1
        v4 = top_start_index + i * 2 + 1
        add.faces.append(f"4 {v1} {v2} {v3} {v4} {color[0]} {color[1]} {color[2]}")


def create_board_structure(rows=6, columns=7):
    """Create the physical structure of the Connect 4 board."""
    # Create board components
    for i in range(rows):
        create_edge([0, i * DEFAULT_WIDTH, 0])

        for j in range(columns):
            create_board_component([j * DEFAULT_WIDTH, i * DEFAULT_WIDTH, 0])

        create_bottom([i * DEFAULT_WIDTH, 0, 0])

    create_bottom([rows * DEFAULT_WIDTH, 0, 0])
    create_board_component([0, 0, 0])


def create_board_circles(rows=6, columns=7):
    """Create circles for each position on the board."""
    for i in range(rows):
        for j in range(columns):
            create_circle(j * DEFAULT_WIDTH, i * DEFAULT_WIDTH)


def create_column_numbers(columns=7):
    """Create column number indicators."""
    for j in range(columns):
        create_column_number(j)


def place_game_pieces(board, rows=6, columns=7):
    """Place game pieces on the board according to the game state."""
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 'X':
                create_game_piece(j, 5 - i, 'X', DEFAULT_LENGTH - 3)
            elif board[i][j] == 'O':
                create_game_piece(j, 5 - i, 'O', DEFAULT_LENGTH - 3)


def generate_board(board, output_file="board.off"):
    """
    Generate a 3D visualization of the Connect 4 board.

    Args:
        board: 2D list representing the game state
        output_file: Path for the output OFF file
    """
    rows = len(board)
    columns = len(board[0]) if rows > 0 else 7

    create_board_structure(rows, columns)
    create_board_circles(rows, columns)
    create_column_numbers(columns)
    place_game_pieces(board, rows, columns)

    add.off(output_file)