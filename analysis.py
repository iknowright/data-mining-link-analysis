"""
graph_1.txt: 6 nodes, 5 edges
graph_2.txt: 5 nodes, 5 edges (a circle)
graph_3.txt: 4 nodes, 6 edges
graph_4.txt: 7 nodes, 18 edges (the example in Lecture3, p29)
graph_5.txt:  469 nodes, 1102 edges
graph_6.txt: 1228 nodes, 5220 edges
"""

import numpy as np

# from page_rank import pagerank
from pagerank import pagerank
from hits import hits
from simrank import get_simrank_matrix


if __name__ == "__main__":
    node_lengths = [6, 5, 4, 7, 469, 1228]

    for i in range(5):
        # create numpy matrix
        matrix = np.zeros(tuple([node_lengths[i]] * 2))

        with open(f"data/graph_{i + 1}.txt", "r") as file_in:
            lines = file_in.readlines()
            for line in lines:
                items = line.strip().split(",")
                matrix[int(items[0]) - 1][int(items[1]) - 1] = 1

        # doing PageRank
        rank = pagerank(matrix)
        np.savetxt(f"output/graph_{i + 1}_PageRank.txt", rank, newline=" ", fmt="%.8g")

        # doing HITS
        authorities, hubs = hits(matrix)
        np.savetxt(f"output/graph_{i + 1}_HITS_authority.txt", authorities, newline=" ", fmt="%.8g")
        np.savetxt(f"output/graph_{i + 1}_HITS_hub.txt", hubs, newline=" ", fmt="%.8g")

        # doing SimRank on graph 1, 2, 3, 4 only
        if i <= 3:
            simrank = get_simrank_matrix(node_lengths[i], matrix)
            np.savetxt(f"output/graph_{i + 1}_SimRank.txt", simrank, newline="\n", delimiter=" ", fmt="%.8g")
