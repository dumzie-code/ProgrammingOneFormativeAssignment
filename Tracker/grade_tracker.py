
from Assignment import Assignment
from Assignment import Homework
from Assignment import Exam
from datetime import datetime

class Grade_tracker():
    def __init__(self):
        pass
  #add assignment      
    def add_Assignment(self):
            Assignment.number_of_Assignment+=1
            print("Assignment added successfully")
            Assignment.assignment.append(self)
            print()
        
    
#FILTERING FUNCTIONS
#Filter by subject
    def filter_by_subject(self):
        subject=input('Enter a subject: ')
        found=False
    
        for assignment in Assignment.assignment:
            if assignment.subject==subject.lower().strip():
           
                if not found:
                    print(f"Filtered by {subject}\n")

                found = True

                print( f"Summary of {assignment.subject}: {assignment.title}\n"
                       f"Subject: {assignment.subject}\n"
                       f"Score: {assignment.score}/{assignment.max_score}\n"
                       f"Due date: {assignment.due_date}\n"
                       f"Type: {assignment.type}\n")
    
        if not found:
            print(f"Filtered by {subject}\n"
                "No assignments found under this subject\n")
        
    
    print()
                           
            
#filter by Exam
    def filter_by_Exam (self):
        found=False
   
        for assignment in Assignment.assignment:
            if assignment.type=="Exam":
                if not found:
                    print("Filtered by Exam\n")
                found=True
                print(f"Summary of {assignment.subject}: {assignment.title}\n"
                    f"Subject: {assignment.subject}\n"
                    f"Score: {assignment.score}/{assignment.max_score}\n"
                    f"Due date: {assignment.due_date}\n"
                    f"Type: {assignment.type}\n")
            
     
        if not found:
            print("Filtered by Exam\n""No assignments found under this type\n")

        print()
                           
   
#filter by homework          
    def filter_by_Homework(self):
        found=False
        for assignment in Assignment.assignment:
            if assignment.type=="Homework":
                found=True
                print(f"Filtered by Homework\n"
                    f"Summary of {assignment.subject}: {assignment.title}\n"
                    f"Subject: {assignment.subject}\n"
                    f"Score: {assignment.score}/{assignment.max_score}\n"
                    f"Due date: {assignment.due_date}\n"
                    f"Type: {assignment.type}\n")
        
        if not found:
            print("Filtered by Homework\n""No assignments found under this type\n")
            print()
        
    #Filter by Due date                      

    def filter_by_duedate(self):
        month = int(input('Enter a month(01-12): '))
        found = False

        for assignment in Assignment.assignment:

            if assignment.due_date is not None:

                if assignment.due_date.month == month:

                    if not found:
                        print(f"Filtered by month {month}\n")

                    found = True

                    print(
                        f"Summary of {assignment.subject}: {assignment.title}\n"
                        f"Subject: {assignment.subject}\n"
                        f"Score: {assignment.score}/{assignment.max_score}\n"
                        f"Due date: {assignment.due_date}\n"
                        f"Type: {assignment.type}\n" )

        if not found:
            print("No assignments found for this month")

    print()
    #LISTING ASSIGNMENTS            
    def list_assignment(self):
        if Assignment.number_of_Assignment == 0:
            print("No assignments have been added yet.")


        print("Below is the list of all assignments\n")
        for assignment in Assignment.assignment:
            print(f"Summary of {assignment.subject}:{assignment.title}")
            print(f"Subject:{assignment.subject}")
            print(f"Title:{assignment.title}")
            print(f"Score:{assignment.score}/{assignment.max_score}")  
            print(f"Due date:{assignment.due_date}")
            print(f"Type:{assignment.type}")
            print()

    #GRADE SUMMARY
    #Calculating overall average
    def overall_average(self):
        if Assignment.number_of_Assignment==0:
            print("There is no summary to show. Please add an assignment first")
        for assignment in Assignment.assignment:
            if assignment.score==None:
                print("There is no summary to show for the assignnments added")
            
        # Overall average
        total_grade=0
        grade=0
        if Assignment.number_of_Assignment==0:
            return 0
        for assignment in Assignment.assignment:
            if assignment.score==None:
                return None
            total_grade= total_grade+assignment.calculate_percent()
            average=total_grade/Assignment.number_of_Assignment
        print(f"Your overall average grade is {average}")
        if float(average < 50):
            #grade threshold
            print("You are below average. you need to sit up!")
            
        #getting all unique subject  
        Subjects=set()
        for assignment in Assignment.assignment:
            Subjects.add(assignment.subject)
        
        #per subject average
        print(f"Your per subject average grade is shown below" )
        print()
        for Subject in Subjects:
            grade=0
            count=0 
            for assignment in Assignment.assignment:
                
                if assignment.subject.lower().strip()==Subject.lower().strip():
                    grade= grade+assignment.calculate_percent()
                    count+=1
            if count > 0:
                Average=grade/count
                print(f"{Subject}:{Average}")
                print()
        #highest scoring assignment
        if Assignment.number_of_Assignment==0:
            print("No assignment to evaluate")
        else:
            highest=Assignment.assignment[0]
       
            for assignment in Assignment.assignment:
                if assignment.calculate_percent()>highest.calculate_percent():
                    highest=assignment
            print(f'Your highest scoring assignment is {assignment.subject} with an average percent of {highest.calculate_percent()} ')
        
       
    
        #lowest scoring assignment    
        if Assignment.number_of_Assignment==0:
            print("No assignemnt to evaluate")
        else:
            lowest=Assignment.assignment[0]
               
            for assignment in Assignment.assignment:
                if assignment.calculate_percent()<lowest.calculate_percent():
                            lowest=assignment
            print(f'Your lowest scoring assignment is {assignment.subject} with an average percent of {lowest.calculate_percent()}')

        #top performing subjects
        if Assignment.number_of_Assignment==0:
            print("No assignemnt to evaluate")
        else:
            print("Your top 5 performing assignments are :")
            assignmentnew=sorted(Assignment.assignment,key=lambda assignment:assignment.calculate_percent(),reverse=True)
            for assignment in assignmentnew[:5]:
                print(f"{assignment.subject[0]}:{assignment.calculate_percent()}")
                print()
        