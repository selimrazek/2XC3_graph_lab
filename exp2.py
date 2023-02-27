import matplotlib.pyplot as plt

from graph import is_connected, create_random_graph, has_cycle

experiments = 500
nodes = 100
edges = 200

chance_of_connection = []
edge = []

for j in range(1, edges):
    connected = 0
    for _ in range(experiments):
        G = create_random_graph(nodes, j)
        if is_connected(G):
            connected += 1
    chance_of_connection.append(connected/experiments * 100)
    edge.append(j)


plt.plot(edge, chance_of_connection, label = "Chance of Connection")
plt.xlabel("Number of edges")
plt.ylabel("Chance of connection in percentage")
plt.legend()
plt.show()
print("done!")