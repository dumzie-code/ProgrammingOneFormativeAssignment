from Add_assignment import Assignment
assignment=[]
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
                
                if assignment.subject==Subject.lower().strip():
                    grade= grade+assignment.calculate_percent()
                    count+=1
        Average=grade/count
        print("Your per subject average grade is:" )
        print(f" {Subject} :{Average}")
    
 
def highest_scoring_assignment():
    s_assignment=assignment.sort(reverse=True)
    for s_assignment in Assignment.assignment:
        pass
    
        
    
  
  