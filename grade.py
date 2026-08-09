
          
class Assignment:
    number_of_Assignment=0
    assignment=[]
    def __init__(self,subject,title,score,max_score,due_date,type) :
        self.subject=subject.lower().strip()
        self.title=title.lower().strip()
        self.score=float(score)
        self.max_score=float(max_score)
        self.due_date=due_date
        self.type=type #homework' or 'exam'
        Assignment.add_Assignment
       
        
    def add_Assignment(self):
        Assignment.number_of_Assignment+=1
        print("Assignment added")
        Assignment.assignment.append(self)
    
    def create_new(self):
            self.subject=input("Enter a subject")
            self.title=input("Enter a title")
            self.score=input("Enter a score")
            self.max_score=input("Enter the max score")
            self.due_date=input("Enter the due date")
        
class Homework(Assignment):
    def __init__(self,subject,title,score,max_score,due_date,type):
        super().__init__(subject,title,score,max_score,due_date,type)
        
    
                    
class Exam(Assignment):
   
     def __init__(self,subject,title,score,max_score,due_date,type):
             super().__init__(subject,title,score,max_score,due_date,type)
             
    
# class Grade:
#     def __init__(self,subject,title,score,max_score,type):
#         self.subject=subject
#         self.title=title
#         self.score=score
#         self.max_score=max_score
#         self.type=type         
        
#     def get_grade(self):
#         return self.grade
        
#     def get_overall_average_grade(self):
#         value=0
#         for subject in self.subject:
#             value+=self.get_grade
#             return value/len(self.subject)
        

assignment=Assignment("science","quiz",10, 10, 10/12, Homework)
assignment.add_Assignment()

# # print(assignment[0])
print (Assignment.number_of_Assignment)
print(Assignment.assignment[0].subject)

for assignment in Assignment.assignment:
    print (assignment.title)




# # def welcome():
# #     print("1.Add homework\n2.Add exam\n3.List Assignments\n4.Filter\n5.Summary\n6.Exit\n")
# #     choice=int(input("Select an action:"))
# #     if choice==1:
# #         input
# #     else:
# #         print("NO")
   

# # welcome()