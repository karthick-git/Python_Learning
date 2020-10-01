# sample=[]
# for i in range(101):
#   sample.append(i)
# print(sample)

sample=[0,1,6,5,3,7,9,2,8]
sum=10
result=[]
answer=[]
for i in range(len(sample)):
  for j in range(len(sample)):
    if(i!=j and sample[i]+sample[j]==sum):
      if(result.__contains__(sample[i])):
        continue
      else:
        result.append(sample[i])
        result.append(sample[j])
print(result)
while(len(result)>0):
  answer.append(result.pop())
  answer.append(result.pop())
  print(answer)
  answer.clear()


        
        
    

  