import unittest
from distribution import Distribution
from exam_material import ExamMaterial

class TestDistribution(unittest.TestCase):
    
    def test_send_materials(self):
        distribution = Distribution()
        material = ExamMaterial("Answer Sheets", 200, "C003")
        distribution.send_materials(material)
        self.assertTrue(material.distributed)
        self.assertIn(material, distribution.materials_sent)

    def test_collect_materials(self):
        distribution = Distribution()
        material = ExamMaterial("Question Papers", 100, "C004")
        distribution.send_materials(material)
        collected = distribution.collect_materials("C004")
        self.assertIn(material, collected)

if __name__ == '__main__':
    unittest.main()
