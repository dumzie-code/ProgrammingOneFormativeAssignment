
          
class Assignment:
    def __init__(self,subject,title,score,max_score,due_date,type) :
        self.subject=subject
        self.title=title
        self.score=score
        self.max_score=max_score
        self.due_date=due_date
        self.type=type         
        
class Homework(Assignment):
    pass
class Exam(Assignment):
    pass








def welcome():
    print("1.Add homework\n2.Add exam\n3.List Assignments\n4.Filter\n5.Summary\n6.Exit\n")
    choice=int(input("Select an action:"))
    if choice==1:
        print("Hi")
    else:
        print("NO")
   

welcome()