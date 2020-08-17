class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__friends = []

    def know(self, other_person):
        if other_person in self.__friends:
            return
        self.__friends.append(other_person)
        other_person.know(self)

    def is_known(self, other_person):
        if other_person in self.__friends:
            return True
        return False


