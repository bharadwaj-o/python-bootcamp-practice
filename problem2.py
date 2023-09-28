import math
class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        print("Volume = ", math.pi * pow(self.radius,2) * self.height)

    def surface_area(self):
        print("Surface Area = ", 2*math.pi*self.radius*(self.radius+self.height))

c=Cylinder(2,3)
c.volume()
c.surface_area()