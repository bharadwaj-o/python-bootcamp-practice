import math
class Line:
    def __init__(self,coor1=(0,0),coor2=(0,0)):
        self.coor1=coor1
        self.coor2=coor2

    def distance(self):
        print(math.sqrt(pow(self.coor1[0]-self.coor2[0],2) + pow(self.coor1[1]-self.coor2[1],2)))
        
    def slope(self):
        print((self.coor1[1]-self.coor2[1])/(self.coor1[0]-self.coor2[0]))

li=Line((3,2),(8,10))
li.distance()
li.slope()