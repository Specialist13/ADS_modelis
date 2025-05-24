import add
import math


def generate_grindys():
    grid_size = 20
    cell_size = 35
    total_size = grid_size * cell_size
    offset = total_size / 2  # Half the total grid size

    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate centered coordinates
            x = i * cell_size - offset + (cell_size / 2)
            z = j * cell_size - offset + (cell_size / 2)

            if (i + j) % 2 == 0:
                add.rectangle3D((x, 0, z), (cell_size, 1, cell_size), (194, 142, 100))
            else:
                add.rectangle3D((x, 0, z), (cell_size, 1, cell_size), (227, 223, 200))

    add.off('grindys.off')

if __name__ == '__main__':
    generate_grindys()