from Add_assignment import Assignment
assignment=[]
number_of_Assignment=0    


def overall_average():
       # Overall average
        total_grade=0
        grade=0
        if Assignment.number_of_Assignment==0:
                return 0
        for assignment in Assignment.assignment:
            total_grade= total_grade+assignment.calculate_percent()
            average=total_grade/Assignment.number_of_Assignment
        print(f"Your overall average grade is {average}")
        if float(average < 50):
            print("You are below average. you need to sit up!")
            
        #getting all unique subject  
        Subjects=set()
        for assignment in Assignment.assignment:
            Subjects.add(assignment.subject)
        
        #per subject average
        for Subject in Subjects:
            grade=0
            count=0 
            for assignment in Assignment.assignment:
                
                if assignment.subject.lower().strip()==Subject.lower().strip():
                    grade= grade+assignment.calculate_percent()
                    count+=1
            if count > 0:
                Average=grade/count
                print(f"Your per subject average grade in {Subject} is:" )
                print(f"{Subject}:{Average}")
        #highest scoring assignment
        if Assignment.number_of_Assignment==0:
            print("No assignemnt to evaluate")
        else:
            highest=Assignment.assignment[0]
       
            for assignment in Assignment.assignment:
                if assignment.calculate_percent()>highest.calculate_percent():
                    highest=assignment
            print(f'Your highest scoring assignment is {assignment.subject} with an average peecent of {highest.calculate_percent()} ')
        
       
    
        #lowest scoring assignment    
        if Assignment.number_of_Assignment==0:
                    print("No assignemnt to evaluate")
        else:
            lowest=Assignment.assignment[0]
               
            for assignment in Assignment.assignment:
                if assignment.calculate_percent()<lowest.calculate_percent():
                            lowest=assignment
            print(f'Your lowest scoring assignment is {assignment.subject} with an average peecent of {lowest.calculate_percent()} ')

        
    
  
  