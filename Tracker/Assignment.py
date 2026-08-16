from datetime import datetime
class Assignment:  
    number_of_Assignment=0    
    assignment=[] 
    total_grade=0
    
    def __init__(self,subject,title, due_date,type,score=None,max_score=None) :
        self.subject=subject.lower().strip()
        self.title=title.lower().strip()
        self.score=score
        self.max_score=max_score
        self.due_date=due_date
        self.type=type #homework' or 'exam'
        self.add_Assignment()
    def add_Assignment(self):
            Assignment.number_of_Assignment+=1
            print("Assignment added successfully")
            Assignment.assignment.append(self)
            print()
           
    def calculate_percent(self):
        #ensuring method does not return error if score and max score =None
        if self.score==None and self.max_score==None:
            return None
        else: 
            return(self.score/self.max_score*100)
                                            
    
        
        
class Homework(Assignment):
    @classmethod
    def create_new(cls):
        subject=input("Enter a subject: ")
        title=input("Enter a title: ")
        score_input=input("Enter a score(press enter if not graded): ")
        if score_input=="":
            score=None
            max_score=None
        else:  
            score=float(score_input)  
            max_score=float(input("Enter the max score: "))
            
            #ensuring score does not exceed max score
            while score>max_score:
                print("Sorry score can not be greater than max score. Try again!")
                score=float(input("Enter a score: "))
        due_date_input=input("Enter the due date(YYYY-MM-DD): ") 
        while True:
            try:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
                if due_date<datetime.today().date():
                    print("Due date cannot be befor today's date.")
                    due_date=input("Enter another date(YYYY-MM-DD: ")
                else:
                   break
            except ValueError:
                due_date_input = input("Invalid format. Please try again with this format date as, YYYY-MM-DD: ")
        
        
        type=cls.__name__
        return cls(subject,title,due_date,type,score,max_score,)
              

class Exam(Assignment):
    @classmethod
    def create_new(cls):
            subject=input("Enter a subject: ")
            title=input("Enter a title: ")
            score=float(input("Enter a score: "))
            max_score=float(input("Enter the max score: "))
            #ensuring score does not exceed max score
            while score>max_score:
                print("Sorry score can not be greater than max score. Try again!")
                score=float(input("Enter a score: "))
            due_date_input=input("Enter the due date(YYYY-MM-DD): ")
            while True:
                try:
                    due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
                    if due_date<datetime.today().date():
                        print("Due date cannot be befor today's date.")
                        due_date=input("Enter another date(YYYY-MM-DD: ")
                    else:
                        break
                except ValueError:
                    due_date_input = input("Invalid format. Please try again with this format date as, YYYY-MM-DD: ")
                    
            type=cls.__name__
            return cls(subject,title,due_date,type,score,max_score,)
                  