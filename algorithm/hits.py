import numpy as np
from algorithm.decorator import execution_timer


@execution_timer
def hits(adj_matrix, precision=0.001):
    # init
    node_len = adj_matrix.shape[0]

    old_authorities = np.ones(node_len)
    old_hubs = np.ones(node_len)

    new_authorities = np.zeros(node_len)
    new_hubs = np.zeros(node_len)

    while 1:
        for i in range(node_len):
            for j in range(node_len):
                # points to it
                if adj_matrix[:, i][j]:
                    new_authorities[i] += old_hubs[j]

                # it points to
                if adj_matrix[i][j]:
                    new_hubs[i] += old_authorities[j]

        # normalization
        auth_sum = sum(new_authorities)
        hub_sum = sum(new_hubs)
        new_authorities = new_authorities / auth_sum
        new_hubs = new_hubs / hub_sum

        # check for convergence, if not, continue doing
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
