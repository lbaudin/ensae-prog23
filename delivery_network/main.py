from graph import Graph, graph_from_file


#data_path = "input/"
#file_name = "network.01.in"

#g = graph_from_file(data_path + file_name)
#print(g)

g = Graph([1])

g.add_edge(2, 1, 18)

print(g)