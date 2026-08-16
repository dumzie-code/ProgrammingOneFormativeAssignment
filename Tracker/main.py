from Assignment import Assignment
from Assignment import Homework
from Assignment import Exam
from grade_tracker import list_assignment
from grade_tracker import filter_by_Exam
from grade_tracker import filter_by_subject
from grade_tracker import filter_by_Homework
from grade_tracker import filter_by_duedate
from grade_tracker import overall_average
def show_menu():
    choice=0
    while choice <6:
        print("Welcome to your assignment/grade tracker")
        print("1.Add homework\n2.Add exam\n3.List Assignments\n4.Filter(by subject/Homework/exam/Due date\n5.Summary\n6.Exit\n")
    
        print()
        while True:
            try:
                choice = int(input("Select an action (1-6): "))
                print()
        
                if choice < 1 or choice > 6:
                    print("Invalid selection. Please choose an option from 1 to 6.")
                    continue
        
                break
        
            except ValueError:
                print("Invalid format. Please enter a number.")
        if choice==1:
            Homework.create_new()
        elif choice==2:
            Exam.create_new()
        elif choice==3:
            list_assignment()
        elif choice==4:
            print("1.Filter by subject\n2.Filter by Homework\n3.Filter by Exam\n4.Filter by Due date\n")
            enter=int(input("Select an action: "))
            print()
            if enter==1:
                filter_by_subject() 
            elif enter==2:
                filter_by_Homework()
            elif enter==3:
                filter_by_Exam()
            elif enter==4:
                filter_by_duedate()
   
        elif choice==5:
            overall_average()
            
        elif choice==6:
            exit
       
           
if __name__ == '__main__':
    show_menu()