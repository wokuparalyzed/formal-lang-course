import cfpq_data
from typing import Tuple
import networkx as nx
import pydot


class GraphData:

    def __init__(self, name):
        csv_path = cfpq_data.download(name)
        self.graph = cfpq_data.graph_from_csv(csv_path)

    @property
    def nodes(self):
        return self.graph.number_of_nodes()

    @property
    def edges(self):
        return self.graph.number_of_edges()

    @property
    def labels(self):
        return cfpq_data.get_sorted_labels(self.graph)

def save_graph_to_file(graph, output_path):
    dot_data = nx.nx_pydot.to_pydot(graph).to_string()
    (dot_graph,) = pydot.graph_from_dot_data(dot_data)
    dot_graph.write(output_path)


def create_and_save_two_cycles_graph(n, m, labels: Tuple[str, str], output_path):
        graph = cfpq_data.labeled_two_cycles_graph(n, m, labels=labels)
        save_graph_to_file(graph=graph, output_path=output_path)
