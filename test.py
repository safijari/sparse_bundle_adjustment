from sba_cpp import SPA2d, Node2d
import numpy as np

s = SPA2d()

"""
Test prep

start at x = 0, y = 0, yaw = 0 (0, 0, 0, 0)
start at x = 1, y = 1, yaw = 0 (1, 1.1, 1.1, 0)
start at x = 0, y = 1, yaw = 0 (2, 0.1, 1.1, 0)
"""

# x, y, yaw, node_id
s.add_node(0, 0, 0, 0)
s.add_node(1.1, 1.1, 0, 1)
s.add_node(0.1, 1.1, 0, 2)

# inverse of covariance
precision_matrix = np.identity(3)

# from_node_id, to_node_id, xdiff, ydiff, yawdiff, precision matrix
s.add_constraint(0, 1, 1.1, 1.1, 0, precision_matrix.tolist())
s.add_constraint(1, 2, -1.1, 0.1, 0, precision_matrix.tolist())
s.add_constraint(2, 0, -0.1, -1.1, 0, precision_matrix.tolist())

# the parameters below are
# max iterations, diagonal augmentation for LM
# use CSparse (set to True for the really fast version)
# initial tolerance for CG
# max iterations for some step in LM
s.compute(100, 1.0e-4, True, 1.0e-8, 50)

# The above values are defaults in the original c++ code and they work
# well there

for n in s.nodes:
    print(n.x, n.y, n.yaw)
