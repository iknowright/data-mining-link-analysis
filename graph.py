import numpy as np
import pygraphviz as pgv

if __name__ == "__main__":
    node_lengths = [6, 5, 4, 7, 469, 1228]

    for i in range(5):
        A = pgv.AGraph(directed=True)
        A.node_attr["shape"] = "circle"
        A.graph_attr["label"] = f"Graph {i + 1}"
        nodelist = [j + 1 for j in range(node_lengths[i])]
        A.add_nodes_from(nodelist)

        with open(f"data/graph_{i + 1}.txt", "r") as file_in:
            lines = file_in.readlines()
            for line in lines:
                items = line.strip().split(",")
                A.add_edge(items[0], items[1])

        A.layout(prog="dot")
        A.draw(f"graph/graph_{i + 1}.png")
