'''
Henali: Henry (e), Erica (hugo), Aahan (spikes)
SoftDev Pd 8
18: (Python+Sqlite)3: A Mare Widge Made in Hebben
Oct 25, 2022
Estimated Time: 1.0 hr 

DISCO:
- If the csv file doesn't match with the type assigned in the database, it returns a TYPE error
- If the primary key id isn't unique, you get an integrity error
- The primary key id isn't expected unless you write/specify it in the command when you create the database
- If you use the open thing without "with", you must close it yourself
- students_dict is an object of Dictionary --> not a dictionary itself bc we don't get rid of the new lines (??)

QCC: 
- bassnectar! 
- tokimonsta

'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE= "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

# students = open('students.csv')
# students_dict = csv.DictReader(students)

# c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")

# for row in students_dict :
#     print(row)
#     command = "INSERT INTO students VALUES ('"+row['name']+"', "+row['age']+", "+row['id']+");"
#     c.execute(command)

with open('students.csv') as students:
    students_dict = csv.DictReader(students)
    c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")
    for row in students_dict :
        print(row)
        # c.execute("SELECT * FROM students;")
        command = "INSERT INTO students VALUES ('"+row['name']+"', "+row['age']+", "+row['id']+");"
        c.execute(command)



with open('courses.csv') as courses:
    courses_dict = csv.DictReader(courses)

    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")

    for row in courses_dict :
        print(row)
        command = "INSERT INTO courses VALUES ('"+row['code']+"', "+row['mark']+", "+row['id']+");"
        c.execute(command)

db.commit() #save changes
db.close()  #close database
