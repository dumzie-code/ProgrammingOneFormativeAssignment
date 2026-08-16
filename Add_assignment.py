from datetime import datetime
class Assignment:  
    number_of_Assignment=0    
    assignment=[] 
    total_grade=0
    
    def __init__(self,subject,title,due_date,type) :
        self.subject=subject.lower().strip()
        self.title=title.lower().strip()
        self.due_date=due_date
        self.type=type #homework' or 'exam'
        self.add_Assignment()
        
    
    def add_Assignment(self):
        Assignment.number_of_Assignment+=1
        print("Assignment added")
        Assignment.assignment.append(self)
        print()
        
    @classmethod
    def create_new(cls):
        subject=input("Enter a subject: ")
        title=input("Enter a title: ")
        due_date=input("Enter the due date(YYYY-MM-DD): ")
        subject=input("Enter a subject: ")
        title=input("Enter a title: ")
        due_date=input("Enter the due date(YYYY-MM-DD): ")
        
        
        type=cls.__name__
        return cls(subject,title,due_date,type)
    
    def calculate_percent(self):
            return(self.score/self.max_score*100)
                    
                                   
    
        
class Homework(Assignment):
    pass


class Exam(Assignment):
    pass