import unittest
from exam_material import ExamMaterial

class TestExamMaterial(unittest.TestCase):
    
    def test_material_creation(self):
        material = ExamMaterial("Answer Sheets", 200, "C001")
        self.assertEqual(material.material_type, "Answer Sheets")
        self.assertEqual(material.quantity, 200)
        self.assertEqual(material.center_id, "C001")
        self.assertFalse(material.distributed)

    def test_distribute_material(self):
        material = ExamMaterial("Question Papers", 100, "C002")
        material.distribute_material()
        self.assertTrue(material.distributed)

if __name__ == '__main__':
    unittest.main()
