from Add_assignment import Assignment
def calculate_percent(self):
            return(self.score/self.max_score*100)
                    
                                   
@classmethod
def overall_average(cls):
        total_grade=0
        if Assignment.number_of_Assignment==0:
                return 0
        for assignment in Assignment.assignment:
            total_grade= total_grade+assignment.calculate_percent()
        print(f"Your overall average grade is {total_grade/Assignment.number_of_Assignment}")
        if overall_average<50:
            print("You are below average. you need to sit up!")
Assignment.overall_average()