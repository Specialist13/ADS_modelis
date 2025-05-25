import add
import math
import random

def generate_gele():

    def rotate_xyz(x, y, z, rot_x, rot_y, rot_z):
        # Rotate Z first
        x1 = x * math.cos(rot_z) - y * math.sin(rot_z)
        y1 = x * math.sin(rot_z) + y * math.cos(rot_z)
        z1 = z

        # Then rotate around X
        y2 = y1 * math.cos(rot_x) - z1 * math.sin(rot_x)
        z2 = y1 * math.sin(rot_x) + z1 * math.cos(rot_x)
        x2 = x1

        # Then rotate around Y
        x3 = x2 * math.cos(rot_y) + z2 * math.sin(rot_y)
        z3 = -x2 * math.sin(rot_y) + z2 * math.cos(rot_y)
        y3 = y2

        return x3, y3, z3



    def sudelioti_lapus():
        # Random position
        offset_x = 0
        if random.random() < 0.5:
            offset_x = random.uniform(-6, -3)
        else:
            offset_x = random.uniform(3, 6)


        offset_y = random.uniform(10, 80)
        offset_z = random.uniform(-1, 1)

        # Random rotations
        rot_x = random.uniform(-math.pi / 6, math.pi / 6)  # tilt forward/back
        rot_y = random.uniform(-math.pi / 6, math.pi / 6)  # tilt side to side
        rot_z = random.uniform(0, 2 * math.pi)             # rotation in XY

        # Random shape
        rx = random.uniform(3, 5)
        ry = random.uniform(2, 3)

        def lapai(u, v):
            angle = u
            radius = v

            # Base oval in XY plane
            x = rx * radius * math.cos(angle)
            y = ry * radius * math.sin(angle)
            z = 0

            # Apply 3D rotation
            x_rot, y_rot, z_rot = rotate_xyz(x, y, z, rot_x, rot_y, rot_z)

            # Apply final position
            return (
                x_rot + offset_x,
                y_rot + offset_y,
                z_rot + offset_z
            )

        add.parametric(lapai, 0, 2 * math.pi, 15, 0, 1, 1, (0, 200, 0))


    for i in range(50):
        sudelioti_lapus()

    add.cylinder((0, 0, 0), (0, 80, 0), 3, 50, (0, 230, 0))

    add.off("gele.off")
