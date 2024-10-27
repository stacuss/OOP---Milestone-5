import unittest
from exam_center import ExamCenter
from person import Invigilator
from exam_material import ExamMaterial
from feedback import Feedback

class TestExamManagementSystem(unittest.TestCase):
    
    def test_add_exam_center(self):
        center = ExamCenter("C003", "Mbarara", 3)
        self.assertEqual(center.get_center_id(), "C003")
        self.assertEqual(center.get_location(), "Mbarara")
        self.assertEqual(center.get_max_invigilators(), 3)
    
    def test_assign_invigilator(self):
        center = ExamCenter("C001", "Kampala", 2)
        invigilator = Invigilator("John Doe", "ID123")
        center.assign_invigilator(invigilator)
        self.assertEqual(len(center.get_invigilators()), 1)

    def test_over_assign_invigilator(self):
        center = ExamCenter("C002", "Gulu", 1)
        invigilator1 = Invigilator("Jane Doe", "ID124")
        invigilator2 = Invigilator("Alex Smith", "ID125")
        center.assign_invigilator(invigilator1)
        with self.assertRaises(ValueError):
            center.assign_invigilator(invigilator2)

    def test_dispatch_material(self):
        center = ExamCenter("C004", "Entebbe", 3)
        material = ExamMaterial("Question Papers", 100, "C004")
        center.receive_materials(material)
        self.assertIn(material, center.get_materials())
    
    def test_invalid_center_id(self):
        self.assertIsNone(find_center_by_id("InvalidID"))

if __name__ == '__main__':
    unittest.main()
