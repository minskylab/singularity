from markov import new_markov_chain_graph, walk_markov_chain
import networkx as nx
import matplotlib.pyplot as plt

chain = new_markov_chain_graph([1, 0], [0.1, 0.2, 0.3, 0.4])
nx.draw_networkx(chain)
plt.savefig("filename.png")

print(nx.attr_matrix(chain, edge_attr="w", rc_order=chain.nodes()))
print([(n, nbrdict) for n, nbrdict in chain.adjacency()])

initial_string = ""
for i in walk_markov_chain(chain, steps=100, debug=True):
    initial_string += str(i)

print(initial_string)
