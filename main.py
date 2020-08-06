import networkx as nx
import matplotlib.pyplot as plt
import cellpylib as cpl
from markov import new_markov_chain_graph, walk_markov_chain
from ca import fill_board

chain = new_markov_chain_graph([0, 1], [0.1, 0.2, 0.3, 0.4])

nx.draw_networkx(chain)

plt.savefig("filename.png")

print(nx.attr_matrix(chain, edge_attr="w", rc_order=chain.nodes()))

initial_state = []
for i in walk_markov_chain(chain, steps=100):
    initial_state.append(i)


cellular_automaton = cpl.init_simple2d(100, 100)

fill_board(cellular_automaton, initial_state, 5, 5, 10, 10)

cellular_automaton = cpl.evolve2d(
    cellular_automaton,
    timesteps=300,
    neighbourhood='Moore',
    apply_rule=cpl.game_of_life_rule,
)

cpl.plot2d_animate(cellular_automaton)
