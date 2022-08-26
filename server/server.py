from flask import Flask
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
            n.append(i)


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

    @app.get("/move/<source>/<target>")
    def move(source, target):
        print("Move from " + source + " to " + target)
        return 'Success: ' + target, 200

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
