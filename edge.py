from node import *

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def setNode1(self, node1):
        self.node1 = node1


    def setNode2(self, node2):
        self.node2 = node2


    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node2
