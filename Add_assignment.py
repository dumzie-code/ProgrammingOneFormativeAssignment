from datetime import datetime
class Assignment:  
    number_of_Assignment=0    
    assignment=[] 
    total_grade=0
 
    def __init__(self,subject,title,score,max_score,due_date,type) :
        self.subject=subject.lower().strip()
        self.title=title.lower().strip()
        self.score=float(score)
        self.max_score=float(max_score)
        self.due_date=due_date
        self.type=type #homework' or 'exam'
        self.add_Assignment()
        
    
    def add_Assignment(self):
        Assignment.number_of_Assignment+=1
        print("Assignment added")
        Assignment.assignment.append(self)
    @classmethod
    def create_new(cls):
        subject=input("Enter a subject: ")
        title=input("Enter a title: ")
        score=input("Enter a score: ")
        max_score=input("Enter the max score:" )
        due_date=input("Enter the due date(YYYY-MM-DD): ")
        type=cls.__name__
        return cls(subject,title,score,max_score,due_date,type)
    # def calculate_percent(self):
    #     overall_average+=1
    #     print(f"You are overall percentage is this assignment is {(self.score/self.max_score)*100}")
    def calculate_percent(self):
            return(self.score/self.max_score*100)
                    
                                   
    
        
class Homework(Assignment):
   pass
class Exam(Assignment):
   pass
