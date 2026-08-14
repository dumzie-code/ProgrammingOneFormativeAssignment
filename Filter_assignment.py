from Add_assignment import Assignment
from Add_assignment import Homework
from Add_assignment import Exam
from datetime import datetime


def filter_by_subject():
    subject=input('Enter a subject: ')
    for assignment in Assignment.assignment:
        if assignment.subject==subject.lower().strip():
            print(f"Filtered by {subject}")
            print( f"Summary of {assignment.subject}: {assignment.title}\n"
                       f"Subject: {assignment.subject}\n"
                       f"Score: {assignment.score}/{assignment.max_score}\n"
                       f"Due date: {assignment.due_date}\n"
                       f"Type: {assignment.type}\n")
            print()
                       
    

def filter_by_Exam ():
    for assignment in Assignment.assignment:
        if assignment.type=="Exam":
            print(f"Filtered by Exam\n"
                  f"Summary of {assignment.subject}: {assignment.title}\n"
                  f"Subject: {assignment.subject}\n"
                  f"Score: {assignment.score}/{assignment.max_score}\n"
                  f"Due date: {assignment.due_date}\n"
                  f"Type: {assignment.type}\n")
            print()
            
            
def filter_by_Homework():
    for assignment in Assignment.assignment:
        if assignment.type=="Homework":
           print(f"Filtered by Homework\n"
                 f"Summary of {assignment.subject}: {assignment.title}\n"
                 f"Subject: {assignment.subject}\n"
                 f"Score: {assignment.score}/{assignment.max_score}\n"
                 f"Due date: {assignment.due_date}\n"
                 f"Type: {assignment.type}\n")
           print()
                       
def filter_by_duedate():
    for assignment in Assignment.assignment:
            if assignment.due=="Homework":
               print(f"Filtered by Homework\n"
                     f"Summary of {assignment.subject}: {assignment.title}\n"
                     f"Subject: {assignment.subject}\n"
                     f"Score: {assignment.score}/{assignment.max_score}\n"
                     f"Due date: {assignment.due_date}\n"
                     f"Type: {assignment.type}\n")
               print()