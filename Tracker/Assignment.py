from datetime import datetime
class Assignment:  
    number_of_Assignment=0    
    assignment=[] 
    total_grade=0
    
    def __init__(self,subject,title,type,due_date=None,score=None,max_score=None) :
        self.__subject=subject.lower().strip()
        self.__title=title.lower().strip()
        self.__score=score
        self.__max_score=max_score
        self.__due_date=due_date
        self.__type=type #homework' or 'exam'
        
    @property
    def subject(self):
        return self.__subject
        
        
    @property
    def title(self):
        return self.__title
    
    @property
    def score(self):
        return self.__score
            
    @property
    def max_score(self):
        return self.__max_score
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def type(self):
            return self.__type
            
        
            
            
    def calculate_percent(self):
        #ensuring method does not return error if score and max score =None
        if self.score==None or self.max_score==None:
            return None
        else: 
            return(self.score/self.max_score*100)
                                            
    
        
        
class Homework(Assignment):
    @classmethod
    def create_new(cls):
        subject=input("Enter a subject: ")
        title=input("Enter a title: ")
        #SCORE
        while True:
            score_input = input( "Enter a score (press enter if not graded): " )

            if score_input == "":
                score = None
                break
    
            try:
                score =float(score_input)

                if score < 0:
                    print("Score cannot be negative.")
                    continue
                break
        
            except ValueError:
                print("Invalid format. Please enter a number.")
        #MAX SCORE
        if score is None:
            max_score=None
        else:
            while True:
                try:
                    max_score = float(input("Enter the max score: "))
        
                    if max_score <= 0:
                        print("Max score must be greater than 0.")
                        continue
                    if score > max_score:
                        print("Sorry, score cannot be greater than max score. "
                        "Try again!")
                        continue
                    break
                except ValueError:
                    print("Invalid format. Please enter a number.")
        #DUE DATE
        due_date_input=input("Enter the due date(YYYY-MM-DD): ") 
        while True:
            try:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
                if due_date<datetime.today().date():
                    print("Due date cannot be befor today's date.")
                    due_date_input=input("Enter another date(YYYY-MM-DD: ")
                else:
                        break
            except ValueError:
                due_date_input= input("Invalid format. Please try again with this format date as, YYYY-MM-DD: ")
        
        
        type=cls.__name__
        return cls(subject,title,type,due_date,score,max_score)
              

class Exam(Assignment):
    @classmethod
    def create_new(cls):
        subject = input("Enter a subject: ")
        title = input("Enter a title: ")

        # SCORE
        while True:
            score_input = input("Enter a score: ")

        
            try:
                score = float(score_input)

                if score < 0:
                    print("Score cannot be negative.")
                    continue

                break

            except ValueError:
                print("Invalid format. Please enter a number.")

        # MAX SCORE
    
        while True:
            try:
                max_score = float(input("Enter the max score: "))

                if max_score <= 0:
                    print("Max score must be greater than 0.")
                    continue

                if score > max_score:
                    print( "Sorry, score cannot be greater than max score. "
                              "Try again!")
                    continue

                break

            except ValueError:
                print("Invalid format. Please enter a number.")

        due_date = None
        type = cls.__name__

        return cls(subject,title,type, due_date, score, max_score )