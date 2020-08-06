import numpy as np
from typing import Iterator, Tuple, List
import networkx as nx


##############################
# full functional approach
##############################

# return: value, next_state
def markov_chain(alphabet: List[any], probs: List[float], current_state: int = 0) -> Tuple[any, int]:
    alphabet_length = len(alphabet)

    if current_state >= len(probs) - 1:
        current_state = 0

    if np.random.random() < probs[current_state]:  # positive
        next_state = current_state + 1
    else:  # negative
        next_state = current_state

    return alphabet[next_state % alphabet_length], next_state


def binary_markov_chain(probs: List[float], current_state: int = 0) -> Tuple[any, int]:
    return markov_chain([0, 1], probs, current_state)


####################
# graph approach
####################


def new_markov_chain_graph(alphabet: List[any], probs: List[float]) -> nx.DiGraph:
    g = nx.DiGraph()
    alphabet_size = len(alphabet)

    for i in range(len(probs)):
        s = alphabet[i % alphabet_size]
        g.add_node(i, value=s)

    total_nodes = g.nodes()
    for n in total_nodes:
        self_w = 1 - probs[n]
        next_w = probs[n]
        g.add_edge(n, n, w=self_w)
        g.add_edge(n, n+1 if n < len(total_nodes)-1 else 0, w=next_w)

    return g


def walk_markov_chain(chain: nx.DiGraph, steps: int = 10, debug=False) -> Iterator:
    current_state = list(chain.nodes())[0]
    for s in range(steps):
        next_state = 0
        if current_state < len(chain.nodes()) - 1:
            next_state = current_state + 1

        if debug:
            print(f"step: {s} | current_state: {current_state}")

        prob_to_next = chain.adj[current_state][next_state]["w"]
        if np.random.random() < prob_to_next:
            current_state = next_state

        val = chain.nodes[current_state]["value"]
        yield val
