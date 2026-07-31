class node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def setleft(self, newleft):
        self.left = newleft
    
    def getleft(self):
        return self.left
    
    def setright(self, newright):
        self.right = newright
    
    def getright(self):
        return self.right

    def setdata(self, newdata):
        self.data = newdata

    def getdata(self):
        return self.data

    def __str__(self):
        return str(self.data)