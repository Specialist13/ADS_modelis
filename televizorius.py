import add
import math

def generate_televizorius():

    add.rectangle3D((0, 0, 0), (10, 90, 5), (0, 0, 0))
    add.rectangle3D((0, 0, 160), (10, 90, 5), (0, 0, 0))
    add.rectangle3D((0, -47.5, 80), (10, 5, 165), (0, 0, 0))
    add.rectangle3D((0, 47.5, 80), (10, 5, 165), (0, 0, 0))
    add.rectangle3D((2.5, 0, 80), (5, 90, 155), (0, 0, 0))
    add.rectangle3D((-2.5, 0, 80), (5, 90, 155), (255, 255, 255))
    add.rectangle3D((10, 0, 80), (10, 30, 50), (0, 0, 0))
    vertices, faces = add.load(f"letters/l.off")
    number_mesh = [vertices, faces]

    number_mesh = add.zoom(number_mesh, 10)
    center = add.center(number_mesh)

    number_mesh = add.rotateY(number_mesh, -math.pi / 2, center)

    number_mesh = add.move(number_mesh, [center[0]-10, -7.5 , center[2]+35])
    number_mesh = add.color(number_mesh, [23, 27, 64])
    add.mesh(number_mesh)

    vertices, faces = add.load(f"letters/r.off")
    number_mesh = [vertices, faces]

    number_mesh = add.zoom(number_mesh, 10)
    center = add.center(number_mesh)

    number_mesh = add.rotateY(number_mesh, -math.pi / 2, center)

    number_mesh = add.move(number_mesh, [center[0]-10, -3.75 , center[2]+80])
    number_mesh = add.color(number_mesh, [23, 27, 64])
    add.mesh(number_mesh)

    vertices, faces = add.load(f"letters/t.off")
    number_mesh = [vertices, faces]

    number_mesh = add.zoom(number_mesh, 10)
    center = add.center(number_mesh)

    number_mesh = add.rotateY(number_mesh, -math.pi / 2, center)

    number_mesh = add.move(number_mesh, [center[0]-10, 3.75 , center[2]+125])
    number_mesh = add.color(number_mesh, [23, 27, 64])
    add.mesh(number_mesh)

    add.off("televizorius.off")