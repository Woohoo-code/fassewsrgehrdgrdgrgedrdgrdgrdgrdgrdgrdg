class stack:
    def __init__(self, top=None):
        self.top = top
        self.others = []
    def add(self, newvalue):
        temp = self.top
        self.top = newvalue
        self.others.append(temp)
    def pop(self):
        if self.top != None and self.others != []:
            temp = self.top
            self.top = self.others.pop()
            return temp
        else:
            return 0
    def getlen(self):
        return len(self.others)
    def peek(self):
        return self.top
    def __str__(self):
        return str(self.top)

