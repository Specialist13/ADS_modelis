import connect4board
import grindys
import stalas
import add
import os

ZOOM = 1
board_center = [0, 0, 0]

def add_board():
    #nedarau checks ar egzistuoja, nes sita callina connect4.py, per kuri vyksta zaidimas
    vertices, faces = add.load("board.off")
    board_mesh = [vertices, faces]

    board_mesh = add.zoom(board_mesh, ZOOM)

    # Get the current center of the mesh
    center = add.center(board_mesh)
    global board_center
    board_center = center

    # Move mesh so its center is at [0,0,0]
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

def generate_everything():

    #sugeneruot visus failus, labai goofy, kad reik clearint kas karta, nes jie viska sudeda i pvz stalo faila lol
    add.clear()
    if not os.path.exists("grindys.off"):
        grindys.generate_grindys()
    add.clear()
    if not os.path.exists("stalas.off"):
        stalas.generate_stalas()
    add.clear()

    add_board()
    add_table()
    add_floor()

    add.off("everything.off")


if __name__ == "__main__":
    generate_everything()
