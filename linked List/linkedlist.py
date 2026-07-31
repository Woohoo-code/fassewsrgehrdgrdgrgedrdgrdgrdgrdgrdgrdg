class node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
    def getvalue(self):
        return self.value
    def setvalue(self,value):
        self.value = value
    def getnext(self):
        return self.next
    def setnext(self, next):
        self.next = next
    def __str__(self):
        return str(self.value)
class linkedlist:
    def __init__(self, head):
        self.head = head
        
    def addvalue(self, value):
        noder2 = node(value)
        targetnode = self.head
        while targetnode.getnext() != None:
            targetnode = targetnode.getnext()
        targetnode.setnext(noder2)

    def printlist(self):
        targetnode = self.head
        while targetnode != None:
            print(targetnode)
            targetnode = targetnode.getnext()
    def removevalue(self, values):
        if values == self.head.getvalue():
            self.head = self.head.getnext()
            return
        targetnode = self.head
        while targetnode.getnext().getvalue() != values:
            targetnode = targetnode.getnext()   
        targetnode.setnext(targetnode.getnext().getnext())
    def insert(self, value, index):
        if index == 0: 
            temp = self.head
            newnode = node(value)
            self.head = newnode
            self.head.setnext(temp)

            return
        targetnode = self.head
        for i in range(index-1):
            targetnode = targetnode.getnext()
        newnode = node(value, targetnode.getnext())
        targetnode.setnext(newnode)
    def pops(self):
        targetnode = self.head
        
        while targetnode.getnext().getnext() != None:
            targetnode = targetnode.getnext()
        ret = targetnode.getnext()
        targetnode.setnext(None)
        return ret



noderdudethingimigigithegreat5200000000000 = node(1)
noderdudethingimigigithegreat5200000000001 = linkedlist(noderdudethingimigigithegreat5200000000000)
noderdudethingimigigithegreat5200000000001.addvalue(5)
noderdudethingimigigithegreat5200000000001.addvalue(600)
noderdudethingimigigithegreat5200000000001.addvalue(57)
noderdudethingimigigithegreat5200000000001.printlist()
noderdudethingimigigithegreat5200000000001.pops()
noderdudethingimigigithegreat5200000000001.printlist()
