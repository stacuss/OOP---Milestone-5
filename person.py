class Person:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number


class Invigilator(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self.__assigned_center = None

    def assign_to_center(self, center):
        self.__assigned_center = center

    def get_assigned_center(self):
        return self.__assigned_center
