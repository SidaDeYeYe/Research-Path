import itertools
import operator
from coreNumber import*
from networkx import nx
import matplotlib.pyplot as plt
import statistics
import community
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms.community.centrality import girvan_newman

def average_clustering(G, trials=1000):
    n = len(G) 
    triangles = 0
    nodes = G.nodes() 
    for i in [int(random.random() * n) for i in range(trials)]: 
        nbrs = list(G[nodes[i]]) 
        if len(nbrs) < 2: 
            continue
        u, v = random.sample(nbrs, 2) 
        if u in G[v]: 
            triangles += 1
    return triangles / float(trials)


G = nx.read_edgelist("30temple83Rel.txt")

print("number of nodes: %d" % G.number_of_nodes())
print("number of edges: %d" % G.number_of_edges())
print("The graph is directed? ", nx.is_directed(G))
if nx.is_connected(G):
    print("The graph is connected?", nx.is_connected(G))
    print("diamater is ", nx.diameter(G))
else:
    print("The graph is not connected")


p = sum(list(nx.triangles(G).values()))
print("number of triangles",p)
print("average clustering")
cc = nx.average_clustering(G)
print("clustering is ", cc)
c = nx.clustering(G)
print("median is ",statistics.median(c.values()))
len1 = len(c) * 0.35
Newc = dict(sorted(c.items(), key=operator.itemgetter(1), reverse=True)[:int(len1)])
total35 = 0
count = 0

print("35 median is ", statistics.median(Newc.values()))
for value in Newc.values():
    total35 = total35 + value
    count = count + 1
ave35 = total35/count
print("35 average = ", ave35)

len5 = len(c) * 0.5
New5 = dict(sorted(c.items(), key=operator.itemgetter(1), reverse=True)[:int(len5)])
print(type(New5))
total50 = 0
count50 = 0

print("50 median is ", statistics.median(New5.values()))
for value in New5.values():
    total50 = total50 + value
    count50 = count50 + 1
ave50 = total50/count50
print("50 average = ", ave50)

newG =  G.remove_edges_from(nx.selfloop_edges(G))
# for core nunmber
print("for core number")
nx.core_number(G)

print("over median is ", statistics.median(nx.core_number(G).values()))
total = 0
count = 0
for value in nx.core_number(G).values():
    total = total + value
    count = count + 1
ave = total/count
print("core number average = ", ave)
#core number 35 
'''lena35 = len(G) * 0.35
newA35 = dict(sorted(G.items(), key=operator.itemgetter(1), reverse=True)[:int(lena35)])
totalc35 = 0
countc35 = 0
print("35 core number median is ", statistics.median((nx.core_number(G)35).values()))
for value in newA35.values():
    totalc35 = totalc35 + value
    countc35 = countc35 + 1
avec35 = totalc35/countc35
print("core number 35 average = ", avec35)
#core number 50
lena50 = len(G) * 0.5
newA50 = dict(sorted(newA.items(), key=operator.itemgetter(1), reverse=True)[:int(lena50)])
totalc50 = 0
countc50 = 0
print("50 core number median is ", statistics.median(newA50.values()))
for value in newA50.values():
    totalc50 = totalc50 + value
    countc50 = countc50 + 1
avec50 = totalc50/countc50
print("core number 50 average = ", avec50)'''


'''print("number of triangle")
ccc = len(nx.triangles(G))
print(ccc)
print("commuinty")
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
print(sorted(map(sorted, next_level_communities)))'''


# csvfile = StringIO.StringIO(data)
# reader = csv.DictReader(csvfile)
# nodes = []
# for row in reader:
#     nodes.append(row['Datetime'])
#     G.add_node(row['Datetime'])
#     if row['ColA'] != '':
#         G.add_edge(row['Datetime'],row['ColA'])
#     if row['ColC'] != '':
#         G.add_edge(row['Datetime'],row['ColC'])
# print G.edges()
# B = bipartite.projected_graph(G, nodes)
# print B.edges()
#csv_file = pd.read_csv("soc-sign-bitcoinalpha.csv", names=["source", "target", "rating", "time"])

#G = nx.from_pandas_edgelist(csv_file, edge_attr=["rating", "time"])
#print("Is the graph multigraph: %d" % G.is_multigraph())

print("Average shortest path")
edges = np.array(G.edges())[:1000]
edges = edges[np.random.permutation(len(edges))].tolist()
nodes1, nodes2 = zip(*edges)
nodes = list(set(list(nodes1) + list(nodes2)))
random_subgraph = G.subgraph(nodes)
plt.figure(figsize=(20, 20))

avg = []
for graph in list(nx.connected_components(random_subgraph)):
    c = nx.average_shortest_path_length(random_subgraph.subgraph(graph))
    print(c)
    avg.append(c)

print("Avg: {}".format(sum(avg) / len(avg)))


print("for community")
#find modularity
part = community.best_partition(G)
#print("community.best_partition ", partition)

res = set(v for k,v in part.items())      
# printing result  
print("numbers of communities ", len(res))

dic ={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0}
for k,v in part.items():
    for i in range(0,len(res)+1):
        if v == i:
            dic[i] = dic.get(i, 0) + 1
p = max(dic, key=dic.get)
print("the largest community is community ",p," with number of nodes:", dic[p])