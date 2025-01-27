import csv
file = open("record.csv", "r")
with file:
    read = csv.reader(file)
    for row in read:
        print(row)

print(" ")

file = open("record_pipe.csv", "r")
with file:
    reader = csv.reader(file, delimiter="|")
    for row in reader:
        print(row)

print(" ")

file = open("record_tab.csv", "r")
with file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        print(row)
print(" ")

import csv
file = open("record.csv", "r")
with file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row))

print(" ")

names = [['FirstName', 'LastName'],
         ['Sofia', 'Reyes'],
         ['Jerome', 'Jackson'],
         ['Jia', 'Zhong']] # a list of lists

file = open('names.csv', "w")
with file:
    file_writer = csv.writer(file)
    for row in names:
        file_writer.writerow(row)

file = open('names.csv', 'w')
with file:
    fnames = ['FirstName', 'LastName']
    writer = csv.DictWriter(file, fieldnames=fnames)
    writer.writeheader()
    writer.writerow({'FirstName': 'Sofia', 'LastName': 'Reyes'})
    writer.writerow({'FirstName': 'Jerome', 'LastName': 'Jackson'})
    writer.writerow({'FirstName': 'Jia', 'LastName': 'Zhong'})