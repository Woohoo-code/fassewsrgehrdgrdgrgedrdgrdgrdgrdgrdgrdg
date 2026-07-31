from node import node
class tree:
    def __init__(self, head):
        self.head = head
    def addnode(self, data):
        temp = self.head
        added = False
        while added == False:
            if data >= temp.getdata():
                if temp.getright() == None:
                    data = node(data)
                    temp.setright(data)
                    added = True
                temp = temp.getright()
            elif data < temp.getdata():
                if temp.getleft() == None:
                    data = node(data)
                    temp.setleft(data)
                    added = True
                temp = temp.getleft()
            
    

    def printtreemech(self, node):
        if node.getdata() != None:
            print(node.getdata())
        if node.getleft() != None:
            param = node.getleft()
            self.printtreemech(param)
        if node.getright() != None:
            param = node.getright()
            self.printtreemech(param)
        

    def printtree(self):
        self.printtreemech(self.head)
    
    def removenode(self, targetvalue):
        temp = self.head
        if targetvalue == self.head.getdata():
            return "Cant remove head node"
        removed = False
        while removed == False:
            print(f" temp is {temp.getdata()}", f"target value is {targetvalue}")
            if targetvalue >= temp.getdata():
                    if temp.getright() != None:
                        if temp.getright().getdata() == targetvalue:
                            if temp.getright().getright() == None and temp.getright().getleft()  == None:
                                temp.getright().setright(None)
                                temp.getright().setleft(None)
                                temp.getright().setdata(None)
                                removed = True    
                            elif temp.getright().getleft() != None and temp.getright().getright() == None:
                                temp.setleft(temp.getright().getleft())
                                temp.setright(temp.getright().getrigyht()) 
                                removed = True    
                            elif temp.getright().getright() != None and temp.getright().getleft() == None:
                                temp.setright(temp.getright().getright())
                                temp.setleft(temp.getleft())
                                removed = True 
                            elif temp.getright().getleft() != None and temp.getright().getright() != None:
                                temp2 = temp.getright().getright()
                                while temp2.getleft() != None:
                                    temp2 = temp2.getleft()
                                temp3 = temp.getright()
                                self.removenode(temp2.getdata())
                                self.replace(temp3.getdata(), temp2.getdata())
                                
                                removed = True
                        temp = temp.getright()

            elif targetvalue < temp.getdata():
                    if temp.getleft() != None:
                        if temp.getleft().getdata() == targetvalue:
                            if temp.getleft().getright() == None and temp.getleft().getleft()  == None:
                                temp.getleft().setright(None)
                                temp.getleft().setleft(None)
                                temp.getleft().setdata(None)
                                removed = True                
                            elif temp.getleft().getright() != None and temp.getleft().getleft() == None:
                                temp.setleft(temp.getleft().getright())
                                temp.setright(temp.getright())
                                removed = True 
                            elif temp.getleft().getleft() != None and temp.getleft().getright() == None:
                                temp.setleft(temp.getleft().getleft())
                                temp.setright(temp.getright())
                                removed = True 
                            elif temp.getleft().getright() != None and temp.getleft().getleft() != None:  
                                temp2 = temp.getleft().getright()
                                while temp2.getright() != None:
                                    temp2 = temp2.getright()
                                temp3 = temp.getleft()
                                self.removenode(temp2.getdata())
                                self.replace(temp3.getdata(), temp2.getdata())
                                removed = True
                        temp = temp.getleft()

    def replace(self, targetvalue, newvalue):
        
        temp = self.head
        removed = False
        while removed == False:
            if targetvalue >= temp.getdata():
                if temp.getdata() == targetvalue:
                    temp.setleft(temp.getleft)
                    temp.setright(temp.getright())
                    temp.setdata(newvalue)
                    removed = True
                temp = temp.getright()
            elif targetvalue < temp.getdata():

                if temp.getdata() == targetvalue:
                    temp.setleft(temp.getleft)
                    temp.setright(temp.getright())
                    temp.setdata(newvalue)
                    removed = True
                temp = temp.getleft()

    def getnodemech(self, value):
        temp = self.head
        found = False
        while found == False:
            if value >= temp.getdata():
                if temp.getdata() == value:
                    return True
                if value > temp.getdata() and temp.getright() == None:
                    return False
                elif value < temp.getdata() and temp.getleft() == None:
                    return False
                elif value < temp.getdata() and temp.getleft() != None:
                    temp = temp.getleft()
                elif value > temp.getdata() and temp.getright() != None:
                    temp = temp.getright()
                
            elif value < temp.getdata():
                if temp.getdata() == value:
                   return True
                if value > temp.getdata() and temp.getright() == None:
                    return False
                elif value < temp.getdata() and temp.getleft() == None:
                    return False
                elif value < temp.getdata() and temp.getleft() != None:
                    temp = temp.getleft()        
                elif value > temp.getdata() and temp.getright() != None:
                    temp = temp.getright()
                

    def getnode(self, value):
        return self.getnodemech(value)

            

    def __str__(self):
        return str(self.head)      





teerr = tree(node(50))
teerr.addnode(10)
teerr.addnode(5)
teerr.addnode(20)
teerr.addnode(30)
teerr.addnode(60)
teerr.addnode(40)
teerr.addnode(200)
teerr.addnode(51)
teerr.addnode(52)



print("\n")
teerr.printtree()
teerr.removenode(51)
print("\n")

teerr.printtree()

