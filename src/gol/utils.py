from typing import List, Tuple

import itertools


def get_neighbors_1dim(x: int, xmax: int) -> List[int]:
    neighbors = [x]
    if x > 0:
        neighbors.insert(0, x - 1)
    if x < xmax - 1:
        neighbors.append(x + 1)
    return neighbors


def get_neighbors(pos: Tuple[int, int], nrow: int, ncol: int) -> List[int]:
    nb_x = get_neighbors_1dim(pos[0], nrow)
    nb_y = get_neighbors_1dim(pos[1], ncol)
    nb_list = list(itertools.product(nb_x, nb_y))
    nb_list.remove(pos)
    return [i * ncol + j for (i, j) in nb_list]
