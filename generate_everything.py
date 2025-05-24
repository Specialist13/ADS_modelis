import connect4board
import grindys
import stalas
import kede
import lentyna
import vaza
import add
import os
import math

ZOOM = 1 # cj sito nereiktu liest xdd

def add_board():
    #nedarau checks ar egzistuoja, nes sita callina connect4.py, per kuri vyksta zaidimas
    vertices, faces = add.load("board.off")
    board_mesh = [vertices, faces]

    board_mesh = add.zoom(board_mesh, ZOOM)

    # Get the current center of the mesh
    center = add.center(board_mesh)

    # Move mesh so its center is at [0,0,0]
    # bsk bugas, kad centras pajuda pridejus tile bet shh shh
    board_mesh = add.move(board_mesh, [-center[0], -center[1], -center[2]])

    add.mesh(board_mesh)

def add_floor():


    vertices, faces = add.load("grindys.off")
    grindys_mesh = [vertices, faces]

    # First apply zoom
    grindys_mesh = add.zoom(grindys_mesh, ZOOM)

    # Get the current center of the mesh
    center = add.center(grindys_mesh)

    # Move mesh so its center is at [0,0,0]
    grindys_mesh = add.move(grindys_mesh, [-center[0], -center[1]-160, -center[2]])

    add.mesh(grindys_mesh)

def add_table():

    vertices, faces = add.load("stalas.off")
    stalas_mesh = [vertices, faces]

    # First apply zoom
    stalas_mesh = add.zoom(stalas_mesh, ZOOM)

    # Get the current center of the mesh
    center = add.center(stalas_mesh)

    # Move mesh so its center is at [0,0,0]
    stalas_mesh = add.move(stalas_mesh, [-center[0], -center[1]-86.5, -center[2]])

    add.mesh(stalas_mesh)

def add_kede(count):
    vertices, faces = add.load("kede.off")
    kede_mesh = [vertices, faces]

    # First apply zoom
    kede_mesh = add.zoom(kede_mesh, ZOOM)

    # Get the current center of the mesh
    center = add.center(kede_mesh)
    if count == 1:
        kede_mesh = add.rotateY(kede_mesh, math.pi, center)
        kede_mesh = add.move(kede_mesh, [-center[0] - 100, -center[1] - 69, -center[2]])
    else:
        # cia bsk slight roattion del # detail
        kede_mesh = add.rotateY(kede_mesh, math.pi/8, center)
        kede_mesh = add.move(kede_mesh, [-center[0] + 100, -center[1] - 69, -center[2] - 15])


    add.mesh(kede_mesh)

def add_lentyna():
    vertices, faces = add.load("lentyna.off")
    lentyna_mesh = [vertices, faces]

    # First apply zoom
    lentyna_mesh = add.zoom(lentyna_mesh, ZOOM)

    # Get the current center of the mesh
    center = add.center(lentyna_mesh)
    lentyna_mesh = add.rotateY(lentyna_mesh, -math.pi/2, center)

    # Move mesh so its center is at [0,0,0]
    lentyna_mesh = add.move(lentyna_mesh, [-center[0]-150, -center[1] - 93, -center[2]-250])

    add.mesh(lentyna_mesh)

def add_vaza():
    vertices, faces = add.load("vaza.off")
    vaza_mesh = [vertices, faces]

    # First apply zoom
    vaza_mesh = add.zoom(vaza_mesh, ZOOM)

    # Get the current center of the mesh
    center = add.center(vaza_mesh)
    vaza_mesh = add.rotateX(vaza_mesh, math.pi/2, center)

    # Move mesh so its center is at [0,0,0]
    vaza_mesh = add.move(vaza_mesh, [-center[0]+150, -center[1] - 115, -center[2]-270])

    add.mesh(vaza_mesh)


def add_sienos():
    # Floor dimensions from grindys.py
    grid_size = 20
    cell_size = 35
    total_size = grid_size * cell_size
    half_size = total_size / 2

    # Wall height
    wall_height = 300
    # Wall thickness
    wall_thickness = 10
    # Wall color (medium oak wood)
    wall_color = (172, 116, 73)

    # Floor is positioned at y = -160
    floor_y = -160
    wall_y = floor_y + (wall_height / 2)

    # Create four walls around the perimeter
    # North wall
    add.rectangle3D((0, wall_y, -half_size - wall_thickness / 2), (total_size, wall_height, wall_thickness), wall_color)

    # East wall
    add.rectangle3D((half_size + wall_thickness / 2, wall_y, 0), (wall_thickness, wall_height, total_size), wall_color)
    # West wall
    add.rectangle3D((-half_size - wall_thickness / 2, wall_y, 0), (wall_thickness, wall_height, total_size), wall_color)

def generate_everything():

    #sugeneruot visus failus, labai goofy, kad reik clearint kas karta, nes jie viska sudeda i pvz stalo faila lol
    add.clear()
    if not os.path.exists("grindys.off"):
        grindys.generate_grindys()
        add.clear()
    if not os.path.exists("stalas.off"):
        stalas.generate_stalas()
        add.clear()
    if not os.path.exists("kede.off"):
        kede.generate_kede()
        add.clear()
    if not os.path.exists("lentyna.off"):
        lentyna.generate_lentyna()
        add.clear()
    if not os.path.exists("vaza.off"):
        vaza.generate_vaza()
        add.clear()


    add_board()
    add_table()
    add_kede(1)
    add_kede(2)
    add_floor()
    add_lentyna()
    add_vaza()
    add_sienos()

    add.off("everything.off")


if __name__ == "__main__":
    generate_everything()
