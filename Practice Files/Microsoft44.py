print('hello world!')

name=input('Enter your name: ')
print(name)

print('blank line \nin the middle of the string')

print('it\'s an example for using double quotes')

first_name='Karthick'
print(first_name)
last_name='srinivasan'
print(first_name+' '+last_name)
print(first_name.upper())
print(first_name.lower())
print(first_name.capitalize())
print(first_name.count('k'))

print(first_name.lower()+' '+first_name.upper()+' '+\
    first_name.capitalize())

first_name='Karthick'
last_name='srinivasan'
output= 'hello, ' + first_name,last_name
print(output)
output='hello {1},{0} '.format(first_name,last_name)
print(output)
output=f'hello {first_name},{last_name}'
print(output)

first_num=2
second_num=5
print(first_num+second_num)
print(first_num-second_num)
print(first_num*second_num)
print(first_num/second_num)
print(first_num**second_num)
print(first_num^second_num)

first_name='karthick\'s age is '
age=25
print(first_name+str(age))

num1=int(input('Enter the 1st number: '))
num2=int(input('Enter the 2nd number: '))
print(num1+num2)

from datetime import datetime,timedelta
currentDate=datetime.now()
print('currentDate is '+str(currentDate))
oneday=timedelta(days=1)
print(currentDate-oneday)
print(currentDate.day)
print(currentDate.month)
print(currentDate.year)
print(currentDate.hour)
print(currentDate.minute)
print(currentDate.second)

birthday=input('Enter your birthday (dd/mm/yyyy)')
birthday_date=datetime.strptime(birthday, '%d/%m/%Y')
print(birthday +': '+str(birthday_date))

x=5
y=2
try:
    print(x/y)
except ZeroDivisionError as e:
    print('not allowed to divide by 0')
else:
    print('something else went wrong')
finally:
    print('cleanup code')

names=['ash','tsubame','karthick']
marks=[]
marks.append(90)
marks.append(100)
print(len(marks))
marks.insert(0,95)
names.sort()
marks.sort()
print(names,marks)

from array import array
scores=array('d')
scores.append(90)
scores.append(100)
print(scores)
print(scores[1])

karthick = {'first':'karthick'}
karthick['last']='ash'
tsubame = {'first':'tsubame'}
tsubame['last']='hatori'
people=[]
people.append(karthick)
people.append(tsubame)
people.append({'first':'shinzo','last':'hatori'})
print(people)
karthick['last']='ninja'
print(people)

name=['karthick','ash']
index=0
while index<len(name):
    print(name[index])
    index+=1

from helpers import display
display('sample message',True)

import json
person_dict={'first':'karthick','last':'ash'}
person_json=json.dumps(person_dict)
print(person_json)

staff_dict={}
staff_dict['program_manager']=person_dict
staff_json=json.dumps(staff_dict)
print(staff_json)

language_list=['Eng','Tam','Kan']
person_dict['languages']=language_list
person_json=json.dumps(person_dict)
print(person_json)

staff_dict['program_manager']=person_dict
staff_json=json.dumps(staff_dict)
print(staff_json)

import os
from dotenv import load_dotenv
os_version = os.getenv('OS')
print(os_version)

load_dotenv()
database = os.getenv('DB')
print(database)


