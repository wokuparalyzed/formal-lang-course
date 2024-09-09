import pytest
import os
from project.graphutils import GraphData, create_and_save_two_cycles_graph, save_graph_to_file
import cfpq_data
import networkx as nx

def test_graph_data():
    graph_name = "travel"
    graph_data = GraphData(graph_name)

    assert graph_data.nodes > 0, "nodes count must be more then 0"
    assert graph_data.edges > 0, "edges count must be more then 0"

    assert isinstance(graph_data.labels, list), "labeles must be in list"
    assert len(graph_data.labels) > 0, "labels must not be empty"

def test_save_graph_to_file(tmpdir):
    graph = nx.complete_graph(5)
    output_path = tmpdir.join("test_graph.dot")

    save_graph_to_file(graph, output_path)

    assert os.path.exists(output_path), "DOT file was not created"

def test_create_and_save_two_cycles_graph(tmpdir):
    output_path = tmpdir.join("two_cycles.dot")

    create_and_save_two_cycles_graph(3, 4, ("a", "b"), output_path)

    assert os.path.exists(output_path), "File with 2 cycles was not created"

    with open(output_path, 'r') as f:
        dot_content = f.read()
        assert 'a' in dot_content and 'b' in dot_content, "labels 'a' and 'b' must be in file"
