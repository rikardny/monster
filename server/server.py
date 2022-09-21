from flask import Flask, request
from dorna2 import Dorna
from helper import *
import matplotlib.pyplot as plt
import networkx as nx
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
            n.append(tuple((i, {"coordinates": nodes[i]})))

        for i in edges:
            if i[0] == "l":
                l.append(tuple(i[1:3]))
            if i[0] == "j":
                j.append(tuple(i[1:3]))

    g.add_nodes_from(n)
    g.add_edges_from(l, type="line")
    g.add_edges_from(j, type="joint")

    return g


def closestNode(graph, j0, j1, j2):
    minimum = 999999
    node = None

    for x in graph:
        i0, i1, i2, *_ = graph.nodes[x]["coordinates"]
        distance = (i0-j0)**2 + (i1-j1)**2 + (i2-j2)**2
        if distance < minimum:
            minimum = distance
            node = x
    return node


def shortestPath(graph, robot, source, target):
    string = ""
    path = nx.shortest_path(graph, source=source, target=target)
    for x in path:
        j0, j1, j2, j3, j4 = graph.nodes[x]["coordinates"]
        robot.jmove(j0=j0, j1=j1, j2=j2, j3=j3, j4=j4)
        string += x + ", "
    return string

def main(file):
    g = createGraph("../graph.json")

    with open(file) as json_file:
        arg = json.load(json_file)

    r = Dorna()
    r.connect(arg["ip"], arg["port"])

    if r.get_motor() == 0:
        status = r.set_motor(1)
    else:
        status = "Motors are already on"
    print(status)

    @app.get("/move")
    def move():
        source = request.args.get("source")
        target = request.args.get("target")
        if target not in g:
            return "Target not found", 400
        if not source:
            print(r.get_all_joint())
            j0, j1, j2, *_ = r.get_all_joint()
            source = closestNode(g, j0, j1, j2)

        string = shortestPath(g, r, source, target)

        return "Moving through " + string, 200

    @app.get("/pickup")
    def pickup():
        prepare(r)
        status = r.jmove(rel=1, z=-20)
        grip(r)
        status = r.jmove(rel=1, z=20)
        print(status)
        return "Success!", 200

    @app.get("/halt")
    def halt():
        status = r.halt()
        print(status)
        return "Robot stopped: " + str(status), 200

    @app.get("/poweroff")
    def poweroff():
        j0, j1, j2, *_ = r.get_all_joint()
        source = closestNode(g, j0, j1, j2)
        shortestPath(g, r, source, "0")
        r.set_motor(0)
        r.close()
        return "Robot turned off!", 200

    app.run(debug=True)


if __name__ == "__main__":
    main("config.json")
