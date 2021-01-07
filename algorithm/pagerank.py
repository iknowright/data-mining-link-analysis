import numpy as np


def pagerank(adj_matrix, num_iterations: int = 100, d: float = 0.85):
    # init
    n = adj_matrix.shape[0]

    for i in range(n):
        pointout_sum = sum(adj_matrix[i])
        # it points to
        for j in range(n):
            if adj_matrix[i][j]:
                adj_matrix[i][j] /= pointout_sum

    l = adj_matrix.T
    r = np.ones(n) / n

    for i in range(num_iterations):
        r = d * (r @ l) + (1 - d) / n

    return r