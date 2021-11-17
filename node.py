

class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def setX(self, nx):
        self.x = nx


    def setY(self, ny):
        self.y = ny


    def setZ(self, nz):
        self.z = nz


    def divideByNorm(self):
        norm = sqrt((self.x*self.x) + (self.y*self.y) + (self.z*self.z))
        self.setX(self.x/norm)
        self.setY(self.y/norm)
        self.setZ(self.z/norm)
