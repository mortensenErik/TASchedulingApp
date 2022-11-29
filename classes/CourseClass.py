class Course:

    def __init__(self, id, name, instructor, number, sections):
        self.id = id
        self.number = number
        self.name = name
        self.sections = sections
        self.instructor = instructor


    def setInstructor(self, instructor):
        self.instructor = instructor

    def getInstructor(self):
        return self.instructor

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    #adds a section
    def addSection(self):
        pass

    #removes a section
    def removeSection(self):
        pass

    def getSections(self):
        return self.sections

