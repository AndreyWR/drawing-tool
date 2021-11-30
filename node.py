

class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def setX(self, nx):
        self.x = nx


    def setY(self, ny):
        self.y = ny


    def setZ(self, nz):
        self.z = nz


    def getX(self):
        return self.x


    def getY(self):
        return self.y


    def getZ(self):
        return self.z


    def divideByNorm(self):
        norm = sqrt((self.x*self.x) + (self.y*self.y) + (self.z*self.z))
        self.setX(self.x/norm)
        self.setY(self.y/norm)
        self.setZ(self.z/norm)
