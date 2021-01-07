import numpy as np


def get_parents(node, adj_matrix):
    return np.where(adj_matrix.T[node] > 0)[0]


def simrank(nodes, adj_matrix, C=0.5, level=1):
    nodes_parents = [get_parents(node, adj_matrix) for node in nodes]
    if len(nodes_parents[0]) == 0 or len(nodes_parents[1]) == 0 or C ** level < 0.01:
        return 0
    else:
        total = 0
        for a_parent in nodes_parents[0]:
            for b_parent in nodes_parents[1]:
                if a_parent == b_parent:
                    total += 1
                else:
                    compare_nodes = (a_parent, b_parent)
                    total += simrank(compare_nodes, adj_matrix, C, level + 1)

        return (C / (len(nodes_parents[0]) * len(nodes_parents[1]))) * total


def get_simrank_matrix(n, adj_matrix):
    simrank_matrix = np.zeros(adj_matrix.shape)
    for i in range(n):
        for j in range(n):
            simrank_matrix[i][j] = simrank((i, j), adj_matrix)
    return simrank_matrix
