#basic exercises part-1


##program to locate Python site-packages.
# import site;
# print(site.getsitepackages())

##Python program to get OS name, platform and release information
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

## For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)

##add if input is an integer
# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b
# print(add_numbers('s', 20))

##LCM
# a=int(input('Enter num1: '))
# b=int(input('Enter num2: '))
# num=0
# if(b>a): a,b=b,a
# divisors=[]
# gcd=1
# for i in range(2,num+1):
#     if(a%i==0 and b%i==0):
#         divisors.append(i)
# if(len(divisors)==0) : gcd=1
# elif(len(divisors)==1): gcd=divisors[0]
# else: gcd=divisors[-1]
# print(int(a*b/gcd))

##GCD
# a=int(input('Enter num1: '))
# b=int(input('Enter num2: '))
# num=0
# if(a>b): num=b
# else: num=a
# divisors=[]
# for i in range(2,num+1):
#     if(a%i==0 and b%i==0):
#         divisors.append(i)
# if(len(divisors)==0) : print(1)
# elif(len(divisors)==1): print(divisors[0])
# else: print(divisors[-1])

# b=float(input('Enter height: '))
# h=float(input('Enter height: '))
# print(0.5*b*h)

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(color_list_1.difference(color_list_2))

# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# count=0
# for i in range(len(numbers)):
#     if(numbers[i]==237):
#         count=i
# for i in range(count):
#     if(numbers[i]%2==0):
#         print(numbers[i])

# n=list(input().split(','))
# str=''
# for i in n:
#     str+=i
# print(str)

# n=list(map(int,input().split(',')))
# for i in n:
#     print('*'*i)

# n=input()
# if n in ['a','e','i','o','u']:
#     print('yes')
# else:
#     print('no')

# n=list(map(int,input().split(',')))
# count=0
# for i in n:
#     if i==4:
#         count+=1
# print(count)

# n=input()
# m=int(input())
# for i in range(m):
#     print(n,end='')

# s=input()
# if s.startswith('is'):
#     print(s)
# else:
#     print('is'+s)

# n=list(map(int,input().split(',')))
# sum=0
# for i in range(3):
#     sum+=n[i]
#
# if(n[0]!=n[1]):
#     print(sum)
# else:
#     print(sum*3)

# from datetime import date
# date1=date(2020,9,20)
# date2=date(2020,9,10)
# diff=date1-date2
# print(diff.days)

# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")

# import calendar
# m=int(input('Enter the month: '))
# y=int(input('Enter the year: '))
# print(calendar.month(y,m))

# print(abs.__doc__)

# n = input()
# print(int(n)+int(n+n)+int(n+n+n))

# n=input().split(',')
# print(n[0]+'/'+n[1]+'/'+n[2])

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])

##print with indentation
# Sample_String= "Twinkle, twinkle, little star,\n\t\t How I wonder what you are! \n\t\t\t\t Up above the world so high, \n\t\t\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n\t\t How I wonder what you are"
# print(Sample_String)

##display python version installed
# import sys
# print(sys.version)
# print(sys.version_info)

##display today's date
# import datetime
# print(datetime.datetime.now())

##convert to tuple
# n=input().split(',')
# print(n)
# print(tuple(n))

##print file extension
# n=input()
# i=n.index('.')
# print(n[i+1:])
