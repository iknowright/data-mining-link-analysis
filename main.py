"""
graph_1.txt: 6 nodes, 5 edges
graph_2.txt: 5 nodes, 5 edges (a circle)
graph_3.txt: 4 nodes, 6 edges
graph_4.txt: 7 nodes, 18 edges (the example in Lecture3, p29)
graph_5.txt:  469 nodes, 1102 edges
graph_6.txt: 1228 nodes, 5220 edges
"""

import numpy as np
import argparse

# from page_rank import pagerank
from algorithm.pagerank import pagerank
from algorithm.hits import hits
from algorithm.simrank import get_simrank_matrix


if __name__ == "__main__":
    # create argument for weka
    ap = argparse.ArgumentParser()
    ap.add_argument("--algorithm", help="link-analysis algorithm [PageRank, HITS, SimRank]", required=True)
    ap.add_argument("--data", help="digraph data file", required=True)
    ap.add_argument("--node-length", help="node length", required=True)
    ap.add_argument("--damping-factor", help="damping factor for PageRank")
    ap.add_argument("--decay-factor", help="decay factor for SimRank")
    args = vars(ap.parse_args())

    matrix = np.zeros(tuple([int(args["node_length"])] * 2))
    try:
        with open(args["data"], "r") as file_in:
            lines = file_in.readlines()
            for line in lines:
                items = line.strip().split(",")
                matrix[int(items[0]) - 1][int(items[1]) - 1] = 1
    except Exception as error:
        print(error)

    # Determine algorithm
    if args["algorithm"] == "PageRank":
        if args.get("damping_factor"):
            rank = pagerank(matrix, int(args["damping_factor"]))
        else:
            rank = pagerank(matrix)
        print("PageRank:")
        print(rank)
    elif args["algorithm"] == "HITS":
        authorities, hubs = hits(matrix)
        print("Authorities:")
        print(authorities)
        print("Hubs:")
        print(hubs)
    elif args["algorithm"] == "SimRank":
        if args.get("decay-factor"):
            simrank = get_simrank_matrix(int(args["node_length"]), matrix, C=int(args["decay_factor"]))
        else:
            simrank = get_simrank_matrix(int(args["node_length"]), matrix)
        print("SimRank:")
        print(simrank)
