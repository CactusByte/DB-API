class Athlete:
    def __init__(self, id=None, name=None, age=None, gender=None, height=None, weight=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "gender": self.gender
        }
