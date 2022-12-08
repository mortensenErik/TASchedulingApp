from app.models import Course


class CourseClass:

    @staticmethod
    def getCourseById(CourseId):
        if CourseId:
            if Course.objects.filter(CourseId=CourseId).exists():
                return Course.objects.get(CourseId=CourseId)
            else:
                return None
        raise TypeError("No parameter provided!")
    
    def createCourse(CourseId, name, number, subject):
        print('in createCourse')
        if CourseClass.getCourseById(CourseId=CourseId) is None:
            Course.objects.create(CourseId=CourseId, name=name, number=number, subject=subject)
            return True
        else:
            print("Unable to create course, already exists.")
            return False
        
    def deleteCourse(CourseId):
        print('in deleteCourse')
        if CourseId:
            Course.objects.filter(CourseId=CourseId).delete()
            return True
        else:
            print("Unable to delete course, does not already exist before deletion.")
            return False
        
        
     

