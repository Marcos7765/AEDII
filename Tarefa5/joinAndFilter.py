import networkx as nx
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file1", type=str, help="File to the graph to merge (if there's any other graph file passed) and filter")
parser.add_argument("files", type=str, help="Other graphs to merge in and filter", nargs='*')
args = parser.parse_args()

files = args.files
files = [args.file1] + args.files
for file in files: 
    if not file.endswith(".graphml"):
        print("Files must end on .graphml (and be on graphml format too)")
        print(f"files: {files}")
        exit()

graphs = [nx.read_graphml(file) for file in files]

for i in range(len(files)):
    print(f"original graph: {files[i]} \n\tvertices: {nx.number_of_nodes(graphs[i])} \tedges:{nx.number_of_edges(graphs[i])}")

print(80*"-")

fused_graph:nx.Graph = nx.compose_all(graphs)

fused_graph_unfiltered = (nx.number_of_nodes(fused_graph), nx.number_of_edges(fused_graph))
print(f"fused graph \n\tvertices: {fused_graph_unfiltered[0]} \tedges:{fused_graph_unfiltered[1]}")

fused_graph.remove_edges_from(nx.selfloop_edges(fused_graph))

duplicates = [(node, node + "s") for node in fused_graph if node + "s" in fused_graph]
for dup in duplicates: fused_graph = nx.contracted_nodes(fused_graph, *dup, self_loops=False)

duplicates = [(x, y) for x, y in [(node, node.replace("-", " ")) for node in fused_graph] if x != y and y in fused_graph]
for dup in duplicates: fused_graph = nx.contracted_nodes(fused_graph, *dup, self_loops=False)

nx.set_node_attributes(fused_graph, 0,"contraction")
nx.set_edge_attributes(fused_graph, 0,"contraction")

print(f"fused graph (deduped) \n\tvertices: {nx.number_of_nodes(fused_graph)} \tedges:{nx.number_of_edges(fused_graph)}")

nx.write_graphml(fused_graph, f"fused_graph.graphml")

core = [node for node, deg in dict(fused_graph.degree()).items() if deg >= 2]

truncated_graph = nx.subgraph(fused_graph, core)

print(f"fused graph (truncated, deduped) \n\tvertices: {nx.number_of_nodes(truncated_graph)} \tedges:{nx.number_of_edges(truncated_graph)}")
nx.write_graphml(truncated_graph, f"fused_graph_truncated.graphml")

print(80*"-")
print("Fused graph filter stats:")
print("Nodes removed: {:.2f}%".format(100*(1 - nx.number_of_nodes(truncated_graph)/fused_graph_unfiltered[0])))
print("Edges removed: {:.2f}%".format(100*(1 - nx.number_of_edges(truncated_graph)/fused_graph_unfiltered[1])))
print("Edges per nodes: {:.2f}".format(nx.number_of_edges(truncated_graph)/nx.number_of_nodes(truncated_graph)))