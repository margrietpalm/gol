import pytest

import gol.core.utils as utils


@pytest.mark.parametrize('x, expected', [(0, [0, 1]), (1, [0, 1, 2]), (2, [1, 2])])
def test_get_neighbors_1dim(x, expected):
    assert utils.get_neighbors_1dim(x, 3) == expected


def test_get_neighbors():
    pos = (1, 1)
    nb = utils.get_neighbors(pos, nrow=3, ncol=3)
    assert pos not in nb
    assert len(nb) == 8
