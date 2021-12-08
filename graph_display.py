# %%
from networkx.readwrite import edgelist
from pyvis.network import Network
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt


# df = pd.read_csv("nodes_Edges_Men.csv")
# df = pd.read_csv("nodes_Edges_Women.csv")
df = pd.read_csv("topcomsWomen.csv")
# df = pd.read_csv("topcomsMen.csv")


# load pandas df as networkx graph
G = nx.from_pandas_edgelist(df,
                            source='Source',
                            target='Target',
                            edge_attr='weight')
print("No of unique characters:", len(G.nodes))
print("No of connections:", len(G.edges))

# G = nx.Graph()

# G.add_edge("a", "b", weight=0.6)
# G.add_edge("a", "c", weight=0.2)
# G.add_edge("c", "d", weight=0.1)
# G.add_edge("c", "e", weight=0.7)
# G.add_edge("c", "f", weight=0.9)
# G.add_edge("a", "d", weight=0.3)

# elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 700]
# esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 700]

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 1000]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 1000]

# # create vis network
# net = Network(notebook=True, width=1000, height=600)
# # load the networkx graph
# net.from_nx(G)
# # show
# net.show("example.html")

plt.figure(figsize=(20, 20))


# nx.draw_circular(G, edgelist=esmall, width=0.5, with_labels=True, font_size=25,
#                  font_color="#ff0000", edge_color="#fff", node_color="#fff")

# nx.draw_circular(G, edgelist=elarge, width=2.5, with_labels=True, font_size=25,
#                  font_color="#ff0000", node_color="#fff")

nx.draw_circular(G, edgelist=esmall, width=0.5, with_labels=True, font_size=26,
                 font_color="#000", edge_color="#ff0000", node_color="#fff")

nx.draw_circular(G, edgelist=elarge, width=2.5, with_labels=True, font_size=26,
                 font_color="#000", edge_color="#ff0000", node_color="#fff")

plt.show()
# plt.savefig("plot_males.png", dpi=1000)
# plt.savefig("plot.pdf")
# nx.draw_circular(G, with_labels=True)
# , font_family="sans-serif"
# graphs_viz_options = [nx.draw, nx.draw_networkx, nx.draw_circular,
#                       nx.draw_kamada_kawai, nx.draw_random, nx.draw_shell, nx.draw_spring]

# # plot graph option
# selected_graph_option = 0

# # plot
# mplt = plt.figure(figsize=(8, 6), dpi=100)
# graphs_viz_options[selected_graph_option](G)

# %%
