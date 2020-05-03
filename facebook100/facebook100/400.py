import itertools
import operator
from networkx import nx
import matplotlib.pyplot as plt
import statistics
import community
import networkx as nx


G = nx.read_edgelist("30temple83Rel.txt")

totalcentra = nx.degree_centrality(G)
{k: v for k, v in sorted(totalcentra.items(), key=lambda item: item[1])}
for x in list(reversed(list(totalcentra)))[0:5]:
    print (totalcentra[x])
