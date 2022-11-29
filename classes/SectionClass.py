

class Section:

    def __init__(self, id, number, course, teacher, typeOfSection):
        self.id = id
        self.number = number
        self.course = course
        self.teacher = teacher
        self.typeOfSection = typeOfSection

    def setTeacher(self, teacher):
        self.teacher = teacher

    def getTeacher(self, teacher):
        return teacher


