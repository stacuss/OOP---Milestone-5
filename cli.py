from exam_center import ExamCenter
from person import Invigilator
from exam_material import ExamMaterial
from distribution import Distribution
from feedback import Feedback

exam_centers = []
feedback_list = []

def find_center_by_id(center_id):
    for center in exam_centers:
        if center.get_center_id() == center_id:
            return center
    return None

def add_exam_center():
    center_id = input("Enter Exam Center ID: ")
    location = input("Enter Exam Center Location: ")
    max_invigilators = int(input("Enter maximum number of invigilators for this center: "))
    new_center = ExamCenter(center_id, location, max_invigilators)
    exam_centers.append(new_center)
    print(f"Exam center {center_id} at {location} added successfully.")

def assign_invigilator_to_center():
    center_id = input("Enter Exam Center ID: ")
    center = find_center_by_id(center_id)
    if center:
        name = input("Enter Invigilator Name: ")
        id_number = input("Enter Invigilator ID Number: ")
        invigilator = Invigilator(name, id_number)
        try:
            center.assign_invigilator(invigilator)
            print(f"Invigilator {name} assigned to center {center_id}.")
        except ValueError as e:
            print(e)
    else:
        print("Exam center not found.")

def dispatch_exam_materials():
    center_id = input("Enter Exam Center ID: ")
    center = find_center_by_id(center_id)
    if center:
        material_type = input("Enter Material Type (Question Papers/Answer Sheets): ")
        quantity = int(input("Enter Quantity: "))
        material = ExamMaterial(material_type, quantity, center_id)
        distribution = Distribution()
        distribution.send_materials(material)
        center.receive_materials(material)
        print(f"{quantity} {material_type} sent to center {center_id}.")
    else:
        print("Exam center not found.")

def collect_feedback():
    invigilator_name = input("Enter Invigilator Name: ")
    center_id = input("Enter Exam Center ID: ")
    feedback_message = input("Enter Feedback Message: ")
    feedback = Feedback(invigilator_name, feedback_message, center_id)
    feedback_list.append(feedback)
    print("Feedback submitted successfully.")

def main_menu():
    print("\n--- UNEB Exam Management System ---")
    print("1. Add Exam Center")
    print("2. Assign Invigilator to Exam Center")
    print("3. Dispatch Exam Materials")
    print("4. Collect Feedback from Invigilators")
    print("5. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        add_exam_center()
    elif choice == "2":
        assign_invigilator_to_center()
    elif choice == "3":
        dispatch_exam_materials()
    elif choice == "4":
        collect_feedback()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice. Please try again.")

while True:
    main_menu()
