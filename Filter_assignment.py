from Add_assignment import Assignment
from Add_assignment import Homework
from Add_assignment import Exam


def filter_by_subject():
    pass
    
    
def filter_by_Exam ():
    for assignment in Assignment.assignment:
        if assignment.type==Exam:
            print (assignment)
   
filter_by_Exam()

    
def filter_by_duedate():
    pass