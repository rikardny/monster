from flask import Flask
from helper import *
import networkx as nx
import matplotlib.pyplot as plt
import json

app = Flask(__name__)

def createGraph(file):
    g = nx.Graph()
    n, l, j = [], [], []

    with open (file, "r") as json_file:
        data = json.load(json_file)
        nodes = data["nodes"]
        edges = data["edges"]

        for i in nodes:
            print(nodes[i])
            # n.append(i, tuple(nodes[i]))


        for i in edges:
            if i[0] == "l":
                l.append(tuple(i[1:3]))
            if i[0] == "j":
                j.append(tuple(i[1:3]))

    g.add_nodes_from(n)
    g.add_edges_from(l, type="line")
    g.add_edges_from(j, type="joint")

    return g

def main():
    g = createGraph("../graph.json")
    r = Robot()

    @app.get("/test")
    def test():
        print("hello")
        print("hello")
        # status = r.jmove(0,35,-125,0,0)
        # status = r.jmove(0,45,-135,0,0)
        return "robot moves: " + str(status), 200

    @app.get("/activate")
    def activate():
        status = r.activate()
        print(status)
        return str(status), 200

    @app.get("/halt")
    def halt():
        status = r.halt()
        print(status)
        return "Robot stopped: " + str(status), 200

    @app.get("/print")
    def print():
        return str(g.nodes) + "hello", 200

    @app.get("/draw")
    def draw():
        nx.draw(g, with_labels=True)
        plt.show()
        plt.savefig("graph.png", format="PNG")
        plt.close()
        return 'Success', 200

    app.run(debug=True)

if __name__ == "__main__":
    main()
