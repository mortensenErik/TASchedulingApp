from app.models import *


class User:

    @staticmethod
    def getUserByEmail(email=None):
        if email is not None:
            if UserProfile.objects.filter(email=email).exists():
                return UserProfile.objects.get(email=email)
            else:
                return None
        raise TypeError("No parameter provided!")

    def getTaAssignments(user):
        result = []
        for section in Section.objects.all():
            if section.faculty.id == user.id:
                result.append(section)
        return result




