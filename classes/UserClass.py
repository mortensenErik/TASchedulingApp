from app.models import UserProfile


class User:

    def doesUserExist(username):
        user = UserProfile.objects.get(username=username)
        if user is not None:
            return True
        return False
