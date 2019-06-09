from troversolve import TroverButtonSolver as tbp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

state = 0b111111111
trover_solver = tbp()
solutions = trover_solver.find_all_states(state)

#We want grid to be 32x16 for a total of 512 squares
grid = []
for row in range(0, 16):
    grid.append(solutions[row*32:(row+1)*32])

harvest = np.array(grid)

fig, ax = plt.subplots()
im = ax.imshow(harvest, cmap='jet')

plt.savefig("map.png", dpi=300)

