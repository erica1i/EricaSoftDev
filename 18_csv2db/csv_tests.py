import csv

# with open('students.csv') as phill:
#     dictionary = csv.DictReader(phill)
#     # for row in csv.DictReader(csvfile) :
#     #     print()

# print(csv.list_dialects())

phill = open('students.csv')
dictionary = csv.DictReader(phill)

for row in dictionary :
    print(row)