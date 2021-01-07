import numpy as np


def hits(adj_matrix, precision = 0.001):
    # init
    node_len = adj_matrix.shape[0]

    old_authorities = np.ones(node_len)
    old_hubs = np.ones(node_len)

    new_authorities = np.zeros(node_len)
    new_hubs = np.zeros(node_len)

    counter = 0
    while 1:
        counter+=1
        for i in range(node_len):
            # points to it
            for j in range(node_len):
                if adj_matrix[:, i][j]:
                    new_authorities[i] += old_hubs[j]

                if adj_matrix[i][j]:
                    new_hubs[i] += old_authorities[j]

        # normalization
        auth_sum = sum(new_authorities)
        hub_sum = sum(new_hubs)
        new_authorities = new_authorities / auth_sum
        new_hubs = new_hubs / hub_sum

        if (
            (np.absolute(new_authorities - old_authorities) < precision).all()
            and
            (np.absolute(new_hubs - old_hubs) < precision).all()
        ):
            break
        else:
            old_authorities = new_authorities.copy()
            old_hubs = new_hubs.copy()

    return new_authorities, new_hubs
