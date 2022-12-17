from app.models import *


class User:

    @staticmethod
    def getUserByEmail(email):
        if email:
            print("email exists!")
            print(UserProfile.objects.filter(email=email).exists())
            if UserProfile.objects.filter(email=email).exists():
                return UserProfile.objects.get(email=email)
            else:
                return None
        raise TypeError("No parameter provided!")


    @staticmethod
    def createUser(email, name, password, phone, address, role):
        UserProfile.objects.create(email=email, name=name, password=password, phone=phone, address=address,
                                   role=role)
        return True

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



