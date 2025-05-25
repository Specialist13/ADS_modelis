import math
import add

#as tng noriu miego tiks ir tokia
def generate_sofa():
    color = (226, 206, 182)
    color2 = (68, 44, 39)

    leg_height = 20
    leg_radius = 5
    add.cylinder((0, 0, 0), (0, leg_height, 0), leg_radius, 20, color2)
    add.cylinder((0, 0, 100), (0, leg_height, 100), leg_radius, 20, color2)
    add.cylinder((50, 0, 0), (50, leg_height, 0), leg_radius, 20, color2)
    add.cylinder((50, 0, 100), (50, leg_height, 100), leg_radius, 20, color2)

    add.rectangle3D((25, leg_height, 50), (65, 20, 100), color)

    add.rectangle3D((25, leg_height + 10, -5), (75, 30, 10), color2)
    add.rectangle3D((25, leg_height + 10, 105), (75, 30, 10), color2)
    add.rectangle3D((60, leg_height + 20, 50), (10, 50, 100), color)

    add.off("sofa.off")

if __name__ == "__main__":
    generate_sofa()
