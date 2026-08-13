from Add_assignment import Assignment
from Add_assignment import Homework
from Add_assignment import Exam
from list_assignment import list_assignment
from Filter_assignment import filter_by_Exam
from Filter_assignment import filter_by_subject
from Filter_assignment import filter_by_Homework
from summary import overall_average
def welcome():
    choice=0
    while choice <6:
        print("1.Add homework\n2.Add exam\n3.List Assignments\n4.Filter\n5.Summary\n6.Exit\n")
        choice=int(input("Select an action: "))
        print()
        if choice==1:
            Homework.create_new()
        if choice==2:
            Exam.create_new()
        if choice==3:
            list_assignment()
        if choice==4:
            print("1.Filter by subject\n2.Filter by Homework\n3.Filter by Exam\n4.Filter by Due date\n")
            enter=int(input("Select an action: "))
            print()
            if enter==1:
                filter_by_subject() 
            elif enter==2:
                filter_by_Homework()
            elif enter==3:
                filter_by_Exam()
            
        if choice==5:
            overall_average()
        else: 
            pass
welcome()