class ExamMaterial:
    def __init__(self, material_type, quantity, center_id):
        self.material_type = material_type
        self.quantity = quantity
        self.center_id = center_id
        self.distributed = False

    def distribute_material(self):
        self.distributed = True
