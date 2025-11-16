
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

people = {
    "Stephen": ["Ama", "Kojo"],
    "Ama": ["Kojo", "Yaw"],
    "Kojo": ["Yaw"],
    "Yaw": [],
    "Dora": []
}

for person, connections in people.items():
    for c in connections:
        G.add_edge(person, c)
    if not connections:
        G.add_node(person)

plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=800, font_size=10)
plt.savefig("network_visualization.png", dpi=300, bbox_inches="tight")
plt.close()
