class student:
    def __init__(self, name=[]):
        self.name = name
        self.weeks = {}
    def enrolled(self, weeks=[]):
        for i in range(len(self.name)):
            self.weeks[self.name[i]] = weeks[i]
        return self.weeks
    def out(self):
        print(self.weeks)
    def sameweek(self, week="A"):
        week = week.capitalize()
        studentsthere = []
        for name in self.weeks:
            for value in self.weeks[name]:
                if week in value:
                    studentsthere.append(name)
        if studentsthere == []:
            return "None"
        else:
            return studentsthere
    

                


stud = student(["Benjini","Greedy","Benji"])
stud.enrolled([["A","B","C"],["A"],["D"]])
print(stud.sameweek("C"))
