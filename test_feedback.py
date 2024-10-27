import unittest
from feedback import Feedback

class TestFeedback(unittest.TestCase):
    
    def test_feedback_creation(self):
        feedback = Feedback("Alice", "Materials arrived late", "C001")
        self.assertEqual(feedback.invigilator_name, "Alice")
        self.assertEqual(feedback.feedback_message, "Materials arrived late")
        self.assertEqual(feedback.center_id, "C001")

    def test_get_feedback_message(self):
        feedback = Feedback("Bob", "Center lacked materials", "C002")
        self.assertEqual(feedback.get_feedback_message(), "Center lacked materials")

if __name__ == '__main__':
    unittest.main()
