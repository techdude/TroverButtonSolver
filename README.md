# TroverButtonSolver
A short solver that allows you to solve the 3x3 button grid puzzles in Trover Saves the Universe. The solver is written in Python, and allows getting lists of all button presses to solve a puzzle, provided that the current state exists in the solution space. [Here is a video](https://www.youtube.com/watch?v=qhGqmsU4iM4) showing the code in action

**Spoiler Alert:**
*The starting state given in the game means that no solution actually exists, and that is intentional. This code is merely here for educational purposes, and to show the solution space.*

## Usage
**To create a solver object:**
```python
solver = TroverButtonSolver()
```

**To find all possible solvable states from a given starting state:**
```python
solutions = solver.find_all_states(state)
```
This returns a boolean list where the index is the binary state value, and the value is `True` if the value exists in the solution space.

**To find a particular solution:**
```python
solution = solver.find_solution(state, initial_state)
```
This returns a list of which button presses are needed to solve the puzzle, if the solution exists.

**Order of buttons and functions**
**0**|**1**|**2**
**3**|**4**|**5**
**6**|**7**|**8**

## Plotting
There is a plotting example shown in `troverplot.py` that will plot areas in red that are solvable, and areas in blue that are unsolvable. This file requires matplotlib and numpy (I recommend installing [SciPy](https://www.scipy.org/) which includes them both).
