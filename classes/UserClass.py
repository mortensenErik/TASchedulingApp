from app.models import *


class User:

    @staticmethod
    def getUserByEmail(email):
        if email:
            if UserProfile.objects.filter(email=email).exists():
                return UserProfile.objects.get(email=email)
            else:
                return None
        #raise TypeError("No parameter provided!")

    @staticmethod
    def createUser(id,email, name, password, phone, address, role):
        if User.getUserByEmail(email) is None:
            UserProfile.objects.create(id=id,email=email, name=name, password=password,phone=phone, address=address,role=role)
            return True
        else:
            return False

    @staticmethod
    def deleteUser(email):
        if email:
            User.getUserByEmail(email).delete()
        else:
            raise TypeError("No parameter provided!")

    @staticmethod
    def editProfileInfo(email, name, phone, address):
        if email:
            current_user = User.getUserByEmail(email)
            if current_user:
                current_user.email = email
                current_user.name = name
                current_user.phone = phone
                current_user.address = address

                current_user.save()
            else:
                raise ValueError("This user does not exist!")
        else:
            raise TypeError("Must provide valid email!")





