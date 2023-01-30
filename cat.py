''' Конструктор Cat, который принимает из словаря значения name,gender, age '''
class Cat:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, animal_dict):
        self.name = animal_dict.get("name")
        self.gender = animal_dict.get("gender")
        self.age = animal_dict.get("age")

