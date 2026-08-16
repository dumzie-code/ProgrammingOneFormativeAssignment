
# Programming One Formative Assignment - Assignment & Grade Tracker

# Project Overview

This project is an Assignment and Grade Tracker created for the Programming One Formative Assignment by me, Chukwudumebi Emmanuella Ukogu.

The program allows students to add and manage their homework and exams, view their assignments, filter assignments by subject, type, and due date, and see a summary of their academic performance which includes overall average grade, top 5 perfomring assignments, highest and lowest assignments, and per subject average.

The project was developed using Python and demonstrates the use of classes, inheritance, methods, loops, conditional statements, lists, sets, sorting, exception handling, and user input.

# Features

# 1. Add Homework

Users can add a homework assignment by entering:

- Subject
- Assignment title
- Score (if already graded)
- Maximum score((if already graded))
- Due date

Homework can also be added without a score if it has not been graded yet.

The program checks that:

- The score does not exceed the maximum score.
- The due date is not before today's date.
- The due date follows the `YYYY-MM-DD` format.

# 2. Add Exam

Users can add an exam by entering:

- Subject
- Exam title
- Score
- Maximum score

The program checks that the score does not exceed the maximum score.

# 3. List Assignments

Users can view all assignments(homework and exam) that have been added to the tracker.

For each assignment, the program displays:

- Subject
- Title
- Score(if avaliable)
- Maximum score(if avaliable)
- Due date(if avaliable)
- Assignment type

# 4. Filter Assignments

The tracker allows assignments to be filtered by:

# Subject

Users can enter a subject and view only assignments belonging to that subject.

# Homework

Displays only assignments that are classified as homework.

#### Exam

Displays only assignments that are classified as exams.

# Due Date

Users can enter a month and view assignments that are due during that month.

If no matching assignments are found, the program displays an appropriate message for all filtering options.

# 5. Grade Summary

The summary feature provides information about academic performance.

It calculates:

- Overall average grade
- Average grade for each subject
- Highest-scoring assignment
- Lowest-scoring assignment
- Top five performing assignments

The program also provides a warning when the overall average is below 50%.

# Object-Oriented Programming

The project uses object-oriented programming concepts.

# Assignment Class

The `Assignment` class is the parent class and stores common information such as:

- Subject
- Title
- Score
- Maximum score
- Due date
- Assignment type

It also contains methods for:

- Adding assignments to the tracker
- Calculating assignment percentages

# Homework Class

`Homework` inherits from the `Assignment` class.

This allows homework assignments to use the attributes and methods defined in the parent class while also allowing homework-specific functionality like creating new homework.

# Exam Class

`Exam` also inherits from the `Assignment` class.

This demonstrates inheritance by allowing both homework and exams to be managed using the same general assignment structure.

# Files

The project contains the following main files:

```text
ProgrammingOneFormativeAssignment/
│screenshots
├── Tracker/
│   ├── Assignment.py
│   ├── grade_tracker.py
│   └── main.py
│
├── Reflection.pdf
└── README.md
Assignment.py
Contains the Assignment, Homework, and Exam classes.

grade_tracker.py
Contains the filtering, listing, and grade summary functions.

main.py
Contains the main menu and allows the user to interact with the assignment tracker.

Reflection.pdf
Contains my reflection on the project, including what I learned, challenges I faced, and how I would improve the project with more time.


# Files

Requirements:

1.Python 3 must be installed on the computer.
2.Running the Program
3.Open the project in Visual Studio Code and run:
main.py

Alternatively, open the terminal in the Tracker folder and run:
python main.py
The program will display a menu:
Welcome to your assignment/grade tracker

1. Add homework
2. Add exam
3. List Assignments
4. Filter
5. Summary
6. Exit

The user can then select an option by entering the corresponding number.
Validation
The program includes input validation to prevent invalid information from being entered.

Examples include:
1.Preventing scores from being greater than the maximum score.
2.Preventing due dates from being earlier than today's date.
3.Checking that dates follow the required format.
4.Handling invalid menu selections(inputs that are >6 and less<1 or inputs that are strings)
5.Handling assignments that have not yet received a grade.
6.Displaying a message when no assignments match a selected filter.


