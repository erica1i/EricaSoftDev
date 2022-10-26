'''
Henali: Henry (e), Erica (hugo), Aahan (spikes)
SoftDev Pd 8
18: (Python+Sqlite)3: A Mare Widge Made in Hebben
Oct 25, 2022
Estimated Time:
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

students = open('students.csv')
students_dict = csv.DictReader(students)

c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")

for row in students_dict :
    print(row)
    command = "INSERT INTO students VALUES ('"+row['name']+"', "+row['age']+", "+row['id']+");"
    c.execute(command)

courses = open('courses.csv')
courses_dict = csv.DictReader(courses)

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")

for row in courses_dict :
    print(row)
    command = "INSERT INTO courses VALUES ('"+row['code']+"', "+row['mark']+", "+row['id']+");"
    c.execute(command)

db.commit() #save changes
db.close()  #close database
