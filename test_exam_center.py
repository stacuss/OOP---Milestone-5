import unittest
from exam_center import ExamCenter
from person import Invigilator

class TestExamCenter(unittest.TestCase):
    
    def test_add_invigilator(self):
        center = ExamCenter("C001", "Kampala", 2)
        invigilator = Invigilator("Alice", "ID001")
        center.assign_invigilator(invigilator)
        self.assertEqual(len(center.get_invigilators()), 1)

    def test_assign_invigilator_limit(self):
        center = ExamCenter("C002", "Entebbe", 1)
        invigilator1 = Invigilator("John", "ID002")
        invigilator2 = Invigilator("Jane", "ID003")
        center.assign_invigilator(invigilator1)
        with self.assertRaises(ValueError):
            center.assign_invigilator(invigilator2)

    def test_receive_materials(self):
        center = ExamCenter("C003", "Mbarara", 3)
        from exam_material import ExamMaterial
        material = ExamMaterial("Question Papers", 100, "C003")
        center.receive_materials(material)
        self.assertIn(material, center.get_materials())

if __name__ == '__main__':
    unittest.main()
