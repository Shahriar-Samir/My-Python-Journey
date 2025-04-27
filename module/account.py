class Account:
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
    def showAccount(self):
        print(f"Name:{self.name}\nEmail:{self.email}\nAge:{self.age}")