import math
import matplotlib.pyplot as plt
import networkx as nx


def GraphProperties(G):
    nodes = G.nodes
    edges = G.edges

    degreedistribution = DegreeDistribution(G)
    averageDegree = AverageDegree(G)

    density = (2*len(edges)) / (len(nodes) *
                                (len(nodes)-1)) if len(nodes) > 1 else 0

    averageclusteringcoefficient = AverageClusteringCoefficient(G)
    # diameter=Diameter(G)

    print(f"Number of nodes = {len(nodes)}")
    print(f"Number of edges = {len(edges)}")
    print(f"Average Degree = {averageDegree}")
    print(f"Density from Manual Calculation = {density}")
    # print(f"Diameter from Manual Calculation: {diameter}")
    print(
        f"Clustering Coeffienent from Manual Calculation : {averageclusteringcoefficient}")

    PlotGraph(G)
    PlotXY(degreedistribution, "Degree Distribution of the Graph",
           "Degree(k)", "P(K)")


def DegreeDistribution(G):
    nodes = G.nodes()
    maxDegree = max(y for (x, y) in G.degree())
    degreeDistribution = [0 for _ in range(0, maxDegree+1)]
    for (x, y) in G.degree():
        degreeDistribution[y] += 1
    for i in range(0, len(degreeDistribution)):
        degreeDistribution[i] = round(degreeDistribution[i] / len(nodes), 2)

    return degreeDistribution


def PlotXY(data, title, xlabel, ylabel):
    plt.plot(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def AverageDegree(G):
    sum = 0
    nodes = G.nodes
    for node in G.degree():
        sum = sum+node[1]
    avg_degree = math.floor(sum/len(nodes))
    return avg_degree


def _nodes_connected(G, u, v):
    return u in G.neighbors(v)


def AverageClusteringCoefficient(G):
    nodes = G.nodes()
    s = 0
    for node in G.degree():
        k = node[1]
        e = 0

        neighbors = list(G.neighbors(node[0]))

        for i in neighbors:
            for j in neighbors:
                if (_nodes_connected(G, i, j)):
                    e = e+1
        e = e/2
        c = (2*e)/(k*(k-1)) if k > 1 else 0
        s = s+c
    avg_clustering_coefficient = s/len(nodes)
    return avg_clustering_coefficient


def Diameter(G):
    if (nx.is_connected(G) == False):
        return -1
    nodes = G.nodes
    nodes = list(nodes)
    s = 0
    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            if i == j:
                continue
            distance = nx.shortest_path_length(
                G, source=nodes[i], target=nodes[j])
            if distance > s:
                s = distance
    return s


def PlotGraph(G):
    nx.draw_random(G, with_labels=False)
    plt.show()
