#Write a Python function that takes a sequence of numbers and
# determines whether all the numbers are different from each other.
num=list(map(int,input().split(',')))
for i in num:
    for j in num:
        if(i!=j & num[i]==num[j]):
            print(num[i])
        else:
            print('no duplicates')

#Write a Python program to create all possible strings by using
# 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import random
char_list = ['a','e','i','o','u']
randomlist=[]
for i in range(len(char_list)):
    random.shuffle(char_list)
    randomlist.append(''.join(char_list))
print(randomlist)

#Write a Python program to remove and print every third number from a list of numbers
# until the list becomes empty.
###Also called josephus problem
def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    #most important step
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1

nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)


