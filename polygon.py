
class Polygon:
    def __init__(self):
        self.edges = []
        self.numedge = 0


    def setEdge(self, ed):
        self.edges.append(ed)
        self.numedge += 1

    def getEdge(self):
        return self.edges
