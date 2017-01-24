
import networkx as nx

def get_second_neighbors(graph, node):
    neighbor_list = [graph.neighbors(n) for n in graph.neighbors(node)]

    second_neighbor_list = []
    for n_list in neighbor_list:
        for n in n_list:
            second_neighbor_list.append(n)
    return second_neighbor_list

def rcompose(relation):
    g = nx.DiGraph(relation)
    r2 = {}

    for key in relation:
        r2[key] = []

    for key in relation:
        
        #get neighbors
        neighbors = g.neighbors(key)

        #add second level neighbors 
        r2[key].extend(get_second_neighbors(g,key))
        
        #remove duplicates
        r2[key] = list(set(r2[key]))

    return r2

#print rcompose({0:[1], 1:[2], 2:[]})
print rcompose({0:[0,1], 1:[0], 2:[1]})
print rcompose({'a':['a'], 'b':['b', 'c'], 'c':['c', 'd'], 'd':['a']}) 
