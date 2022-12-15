from enum import IntEnum
from typing import List, Optional

import numpy as np

from gol.core.utils import get_neighbors


class State(IntEnum):
    alive = 1
    dead = 0

    def __repr__(self) -> str:
        return str(self.name)


class Cell:
    def __init__(self, state: State, row: int, col: int):
        self.state = state
        self.row = row
        self.col = col
        self.neighbors: List[Cell] = []

    def set_neighbors(self, neighbors: List):
        self.neighbors = neighbors

    def __int__(self) -> int:
        return int(self.state)


def get_state_change(cell: Cell) -> Optional[State]:
    nb_alive = np.sum(np.array([nb.state for nb in cell.neighbors], dtype=int))
    if cell.state == State.alive and (nb_alive < 2 or nb_alive > 4):
        return State.dead
    elif cell.state == State.dead and nb_alive == 3:
        return State.alive
    return None


class Grid:
    def __init__(self, nrow: int, ncol: int):
        self.nrow = nrow
        self.ncol = ncol
        self.cells = {i * ncol + j: Cell(State.dead, row=i, col=j) for i in range(nrow) for j in range(ncol)}
        self._setup_neighbors()

    @property
    def grid(self):
        return np.array([[self.cells[i * self.ncol + j] for j in range(self.ncol)] for i in range(self.nrow)],
                        dtype=int)

    def _setup_neighbors(self):
        for cell in self.cells.values():
            nb = [self.cells[nb_idx] for nb_idx in get_neighbors((cell.row, cell.col), self.nrow, self.ncol)]
            cell.set_neighbors(nb)

    def seed(self, n: int):
        self.alive_idx = np.random.choice(self.nrow * self.ncol, size=n, replace=False)
        self.reset()

    def reset(self):
        for idx in self.alive_idx:
            self.cells[idx].state = State.alive

    def update(self):
        # updating is synced: first check and then update
        new_states = {idx: new_state for idx, cell in self.cells.items() if
                      (new_state := get_state_change(cell)) is not None}
        for idx, new_state in new_states.items():
            self.cells[idx].state = new_state
