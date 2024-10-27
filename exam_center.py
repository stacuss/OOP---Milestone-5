class ExamCenter:
    def __init__(self, center_id, location, max_invigilators):
        self.__center_id = center_id
        self.__location = location
        self.__invigilators = []
        self.__materials_received = []
        self.__max_invigilators = max_invigilators

    def get_center_id(self):
        return self.__center_id

    def get_location(self):
        return self.__location

    def get_invigilators(self):
        return self.__invigilators

    def get_materials(self):
        return self.__materials_received

    def assign_invigilator(self, invigilator):
        if len(self.__invigilators) >= self.__max_invigilators:
            raise ValueError(f"Cannot assign more than {self.__max_invigilators} invigilators to center {self.__center_id}")
        self.__invigilators.append(invigilator)
        invigilator.assign_to_center(self)

    def receive_materials(self, material):
        self.__materials_received.append(material)
