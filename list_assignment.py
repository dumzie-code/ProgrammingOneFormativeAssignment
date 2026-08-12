from Add_assignment import Assignment
def list_assignment():
    for assignment in Assignment.assignment:
        print(f"Summary of {assignment.subject}:{assignment.title}")
        print(f"Subject:{assignment.subject}")
        print(f"Score:{assignment.score}/{assignment.max_score}")  
        print(f"Due date:{assignment.due_date}")
        print(f"Type:{assignment.type}")
        print()
list_assignment()