class Distribution:
    def __init__(self):
        self.materials_sent = []

    def send_materials(self, material):
        material.distribute_material()
        self.materials_sent.append(material)

    def collect_materials(self, center_id):
        return [m for m in self.materials_sent if m.center_id == center_id and m.distributed]
