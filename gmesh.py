import add, random, math


def gen_gmesh():
    all_meshes = []

    for i in range(20):
        offset_x = random.randint(-30, 30)
        offset_z = random.randint(-30, 30)

        # Load and process individual flower
        vertices, faces = add.load("gele.off")
        gele_mesh = [vertices, faces]
        gele_mesh = add.color(gele_mesh, (random.randint(0, 60), random.randint(150, 255), random.randint(0, 60)))

        # Get the current center of the mesh
        center = add.center(gele_mesh)
        gele_mesh = add.rotateY(gele_mesh, math.pi / 2 * random.uniform(0, 1), center)

        # Move to new position using both offsets
        gele_mesh = add.move(gele_mesh, [-center[0] + offset_x, -center[1], -center[2] + offset_z])

        # Collect meshes instead of saving immediately
        all_meshes.append(gele_mesh)

    # Merge all flower meshes
    merged_mesh = add.merge(all_meshes)

    # Add the merged mesh to the scene
    add.mesh(merged_mesh)

    # Save to file once at the end
    add.off("gmesh.off")