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


    @staticmethod
    def createUser(email, name, password, phone, address, role):
        if not email or not name or not password or not phone or not address or not role:
            raise ValueError("One of the value is null!")
        roles = ['TA', 'Instructor', 'INSTRUCTOR', 'ADMIN', 'admin']
        if role not in roles:
            raise ValueError("Invalid role")
        if '@' not in email:
            raise ValueError("Invalid email")
        if len(phone) > 12:
            raise ValueError("Invalid phone")
        if UserProfile.objects.filter(email=email):
            raise ValueError("Duplicate Email")
        UserProfile.objects.create(email=email, name=name, password=password, phone=phone, address=address,
                                   role=role)
        return True

    @staticmethod
    def deleteUser(email):
        if email:
            user = User.getUserByEmail(email)
            if user:
                user.delete()
            else:
                raise ValueError("No user with this email exists!")
        else:
            raise ValueError("No parameter provided!")

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



