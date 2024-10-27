class Feedback:
    def __init__(self, invigilator_name, feedback_message, center_id):
        self.invigilator_name = invigilator_name
        self.feedback_message = feedback_message
        self.center_id = center_id

    def get_feedback_message(self):
        return self.feedback_message
