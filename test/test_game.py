import pytest

import numpy as np

import gol.game as game


class TestCell:
    cell_dead = game.Cell(game.State.dead, row=1, col=0)
    cell_alive = game.Cell(game.State.alive, row=1, col=2)

    def test_int_cast(self):
        assert int(self.cell_alive) == 1
        assert int(self.cell_dead) == 0

    def test_set_neighbors(self):
        cell = game.Cell(game.State.alive, row=1, col=1)
        nb = [self.cell_alive, self.cell_dead]
        assert cell.neighbors == []
        cell.set_neighbors(nb)
        assert cell.neighbors == nb


class TestGrid:

    def test_seed(self):
        grid = game.Grid(nrow=3, ncol=3)
        grid.seed(3)
        assert sum([cell.state for cell in grid.cells.values()])

    def test_grid_init(self):
        grid = game.Grid(nrow=3, ncol=3)
        np.testing.assert_array_equal(grid.grid, np.zeros((3, 3)))

    def test_grid_with_living(self):
        grid = game.Grid(nrow=3, ncol=3)
        grid.cells[0].state = game.State.alive
        expected = np.zeros((3, 3))
        expected[0, 0] = 1
        np.testing.assert_array_equal(grid.grid, expected)


@pytest.mark.parametrize('nof_nb_alive, expected',
                         [(nb, game.State.dead if (nb < 2 or nb > 4) else None) for nb in range(8)])
def test_get_state_change_from_alive(nof_nb_alive, expected):
    nb_alive = [game.Cell(game.State.alive, row=0, col=0) for _ in range(nof_nb_alive)]
    nb_dead = [game.Cell(game.State.dead, row=0, col=0) for _ in range(8 - nof_nb_alive)]
    cell = game.Cell(game.State.alive, row=0, col=0)
    cell.set_neighbors(nb_alive + nb_dead)
    assert game.get_state_change(cell) == expected
