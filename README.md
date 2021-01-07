# Data Mining - Link Analysis
Analysis of 4 major link-analysis algorithm including implementation and visualization.

## Features
Algorithms used in this project
* [PageRank](https://zh.wikipedia.org/wiki/PageRank)
* [HITS](https://en.wikipedia.org/wiki/HITS_algorithm)
* [SimRank](https://zh.wikipedia.org/wiki/SimRank)

## Getting Started

### Prerequisites
* Python 3
* graphviz (for graph visualization)

### Setup environment

1. install dependencies
```
sudo apt-get install graphviz graphviz-dev
```

2. For this project, use pipenv to install python packages
```
pipenv install
```

### Calculating on your graph
```=bash
python main.py --help
usage: main.py [-h] --algorithm ALGORITHM --data DATA --node-length
               NODE_LENGTH [--damping-factor DAMPING_FACTOR]
               [--decay-factor DECAY_FACTOR]

optional arguments:
  -h, --help            show this help message and exit
  --algorithm ALGORITHM
                        link-analysis algorithm [PageRank, HITS, SimRank]
  --data DATA           digraph data file
  --node-length NODE_LENGTH
                        node length
  --damping-factor DAMPING_FACTOR
                        damping factor for PageRank
  --decay-factor DECAY_FACTOR
                        decay factor for SimRank
```

### Analysis

Analysis on this project may refer [this](https://nbviewer.jupyter.org/github/iknowright/data-mining-link-analysis/blob/master/report.ipynb) notebook

### Contributors
* Chai-Shi, Chang
