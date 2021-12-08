from pyvis.network import Network
import csv

# Add nodes
net = Network(notebook=True)
# net.add_node(1, label="Alex")
# net.add_node(2, label="Cathy")
# net.show("nodes.html")

# Add a list of nodes
# net = Network(notebook=True)
# net.add_nodes([1, 2], label=["Alex", "Carthy"])
# net.show("list_of_nodes.html")

# net.add_nodes(
#     [3, 4, 5, 6],
#     label=["Michael", "Ben", "Oliver", "Olivia"],
#     color=["#3da831", "#9a31a8", "#3155a8", "#eb4034"],
# )
# net.show("list_of_nodes_with_color.html")

# # Add edges
net = Network(notebook=True)

net.add_nodes(
    [1, 2, 3, 4, 5, 6],
    label=["Alex", "Cathy", "Michael", "Ben", "Oliver", "Olivia"],
    color=["#00bfff", "#ffc0cb", "#3da831", "#9a31a8", "#3155a8", "#eb4034"],
)
net.add_edge(1, 5)
net.add_edges([(2, 5), (3, 4), (1, 6), (2, 6), (3, 5)])
net.show("edges.html")

# # Edges with Weights
# net = Network(notebook=True)

# net.add_nodes(
#     [1, 2, 3, 4, 5, 6],
#     label=["Alex", "Cathy", "Michael", "Ben", "Oliver", "Olivia"],
#     color=["#00bfff", "#ffc0cb", "#3da831", "#9a31a8", "#3155a8", "#eb4034"],
# )

# net.add_edge(1, 5, value=2)
# net.add_edges([(2, 5, 5), (3, 4, 2), (1, 6), (2, 6), (3, 5)])

# net.show("edges_with_weights.html")

# # Edges with Repulsion


def add_repulsion(node_distance: int, spring_length: int):
    net = Network(notebook=True)
    net.width = '1900px'
    net.height = '1080px'

    with open('nodes_Edges.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        nodenum = []
        label = []
        edges = []

        for row in csv_reader:
            s_source = row['Source']
            s_target = row['Target']
            s_weight = row['weight']

            if s_source not in label:
                nodenum.append(len(label))
                label.append(s_source)
            if s_target not in label:
                nodenum.append(len(label))
                label.append(s_target)

            pos_1 = label.index(s_source)
            pos_2 = label.index(s_target)
            pos_3 = int(s_weight)

            edges.append((pos_1, pos_2, pos_3))

        print(nodenum, label, edges)

        net.add_nodes(
            nodenum,
            label=label,
            # color=["#00bfff", "#ffc0cb", "#3da831",
            #        "#9a31a8", "#3155a8", "#eb4034"],
        )

    # net.add_edge(1, 5, value=2)
    net.add_edges(edges)

    net.repulsion(node_distance=node_distance)
    # net.

    # net.show(f"distance_{node_distance}_spring_length_{spring_length}.html")

    return net


# net = add_repulsion(node_distance=100, spring_length=500)
# net.show("distance_100_spring_length_200.html")

# net = add_repulsion(node_distance=100, spring_length=1000)
# net.show(f"distance_100_spring_length_1000.html")

net = add_repulsion(node_distance=100, spring_length=500)
net.show(f"distance_500_spring_length_200.html")
