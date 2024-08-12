class Person:
    def __init__(self , first_name , last_name , age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def getString(self):
        return f"Name: {self.first_name} {self.last_name}  Age:{self.age}"
    


my_persona = Person("Maurice", "Smith" , "32")
print(my_persona.getString())