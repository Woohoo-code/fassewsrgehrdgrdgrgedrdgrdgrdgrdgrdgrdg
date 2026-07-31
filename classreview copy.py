class point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def dist(self,second):
        distx = abs(self.x-second.x)
        disty = abs(self.y-second.y)
        return distx,disty
        




p = point(1,2)
t = point(2,3)
o = t.dist(p)
print(o)
