# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 00:06:57 2020

@author: Himanshu Khairajani
"""

import Attendance_updation
import pandas as pd

Students =Attendance_updation.Total_Students
Months =Attendance_updation.Months
Subjects=Attendance_updation.sub

for i,j in enumerate(Students):
    print(i+1,j)
student = int(input("Enter Roll Number:\t"))

print()
for i,j in enumerate(Months):
    print(i+1,j)
month = int(input("Enter Month:\t"))

print()
for i,j in enumerate(Subjects):
    print(i+1,j)
subject = int(input("Enter Subject:\t"))


print('Attendance Information\n')
dataset=pd.read_excel('attendance_update.xlsx',sheet_name=Subjects[subject-1])
print('{} attended classes on following dates'.format(Students[student-1]),list(map(int,dataset.iloc[student-1][month+2].split(',')[1:-1])),'in {} month'.format(Months[month-1]))
