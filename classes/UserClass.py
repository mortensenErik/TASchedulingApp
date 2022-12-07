from app.models import UserProfile


class User:

    @staticmethod
    def getUserByEmail(email=None):
        if email is not None:
            if UserProfile.objects.filter(email=email).exists():
                return UserProfile.objects.get(email=email)
            else:
                return None
        raise TypeError("No parameter provided!")

    def getTAAssignments(user):
        pass


