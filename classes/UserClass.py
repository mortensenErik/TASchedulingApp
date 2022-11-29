class User:

    def __init__(self, id, name, pw, address, phone, email, officeHours):
        self.name = name
        self.id = id
        self.pw = pw
        self.address = address
        self.phone = phone
        self.email = email
        self.officeHours = officeHours

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setOfficeHours(self, officeHours):
        self.officeHours = officeHours

    def getOfficeHours(self):
        return self.officeHours

