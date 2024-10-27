import unittest
from person import Person, Invigilator
from exam_center import ExamCenter

class TestPerson(unittest.TestCase):
    
    def test_person_attributes(self):
        person = Person("Alice", "ID001")
        self.assertEqual(person.get_name(), "Alice")
        self.assertEqual(person.get_id_number(), "ID001")

    def test_invigilator_assignment(self):
        center = ExamCenter("C001", "Kampala", 2)
        invigilator = Invigilator("Bob", "ID002")
        invigilator.assign_to_center(center)
        self.assertEqual(invigilator.get_assigned_center(), center)

if __name__ == '__main__':
    unittest.main()
