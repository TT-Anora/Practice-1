"""
1. Find the longest continuous sequence from the list
"""

list_ = [1,9,3,10,2,20,5,6,7,8]

list_.sort()
print(list_)
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 20]

max_seq = []
for index in range(len(list_)-1):
    if list_[index] + 1 == list_[index + 1]:
        temp = [list_[index]]
        for next in range(index+1, len(list_)-1):
            if list_[next] + 1 == list_[next + 1]:
                temp.append(list_[next + 1])
            else:
                if len(temp) > len(max_seq):
                    max_seq = temp
                break

print(max_seq)

"""
2.
enrollment_data = [
    ("Alice", ["Math", "Physics", "Chemistry"]),
    ("Bob", ["Physics", "Biology"]),
    ("Charlie", ["Math", "Physics"]),
    ("David", ["Math", "Physics", "Chemistry", "Computer Science"]),
    ("Eve", ["Math", "Chemistry"])
]

courses_to_check = ["Math", "Physics"]

Output:
{'Alice', 'David', 'Charlie'}
"""

# Was asked to only code the part of adding tuples into dict
# list_ =[
#     (1, "a"),
#     (2, "b"),
#     (3, "c")
# ]
#
# myDict = {}
#
# for each in list_:
#     print(each)
#     myDict[each[0]] = each[1]
#
#
# print(myDict)


def findTeachersForCourses(list_ : list):
    temp = []
    set1 = set(list_)
    set2 = {}
    for key, val in myDict.items():
        set2 = set(val)
        if set1.intersection(set2) == set1:
            temp.append(key)
    return set(temp)

enrollment_data = [
    ("Alice", ["Math", "Physics", "Chemistry"]),
    ("Bob", ["Physics", "Biology"]),
    ("Charlie", ["Math", "Physics"]),
    ("David", ["Math", "Physics", "Chemistry", "Computer Science"]),
    ("Eve", ["Math", "Chemistry"])
]

courses_to_check = ["Math", "Physics"]

myDict = {}

for each in enrollment_data:
    myDict[each[0]] = each[1]

print(myDict)
print(findTeachersForCourses(courses_to_check))

"""
3. You have a CSV file named student_scores.csv with the following columns: 
StudentID, Name, Subject, Score. 
Write a Python function find_top_students(filename="student_scores.csv", top_n=3) 
that reads this CSV file and returns a list of the names of the top top_n students 
based on their average score across all subjects.

StudentID,Name,Subject,Score
101,Alice,Math,90
101,Alice,Science,85
102,Bob,Math,78
102,Bob,Science,92
103,Charlie,Math,95
103,Charlie,English,88
101,Alice,English,92
102,Bob,English,80
"""

import csv

def findAvg(myDict_: dict):
    for value in myDict_.values():
        avg = value[0]/value[1]
        value.append(float(avg))

    return myDict_

def findTopN(myDict_: dict, N: int):
    myDict_ = dict(sorted(myDict_.items(), key=lambda x: x[1][-1], reverse=True))
    count = 0
    # print(myDict_)
    for key, value in myDict_.items():
        if count <= 3:
            print(value)


def find_top_students(filename="Data.csv", top_n=3):
    with open(filename, "r") as csvFile:
        reader = csv.reader(csvFile)
        myDict_ = {}

        for x in reader:
            if x[-1] == "Score": continue
            totalMarks = int(x[-1])
            if x[0] in myDict_.keys():
                myDict_[x[0]][0] = myDict_[x[0]][0] + int(x[-1])
                myDict_[x[0]][1] += 1
            else:
                myDict_[x[0]] = [totalMarks, 1, x[1]]

    print(myDict_)
    myDict_ = findAvg(myDict_)
    findTopN(myDict_, top_n)

find_top_students()