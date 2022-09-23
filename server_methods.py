@app.get("/move/<source>/<target>")
def move(source, target):
    help()
    return "Successawfeawef", 200
    nx.shortest_path(g, source=source, target=target)

@app.get("/test")
def test():
    status = r.jmove(0,0,0,0,0)
    status = r.jmove(0,45,0,0,0)
    return "robot moves: " + str(status), 200

@app.get("/activate")
def activate():
    status = r.activate()
    print(status)
    return str(status), 200

@app.get("/node/<target>")
def node(target):
    print("help")
    return "Coordinates are: " + str(g.nodes("coordinates")[target]), 200

@app.get("/halt")
def halt():
    status = r.halt()
    print(status)
    return "Robot stopped: " + str(status), 200

@app.get("/print")
def print():
    return str(g.nodes)

@app.get("/draw")
def draw():
    nx.draw(g, with_labels=True)
    plt.show()
    plt.savefig("graph.png", format="PNG")
    plt.close()
    return 'Success', 200

