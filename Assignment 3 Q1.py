# Assignment 3
# Question 1


use=input ("u have to enter a word/sentence \n")
count=0

for i in use :
 if i==' ':
   count=1
 if count==1:
   if i!=' ':
     count=2

if count<=1 :
  x=set(use)
  for j in x:
    if x!=' ':
     print (f"occurrence of {j} = {use.count(j)}")


if count>1:
  string=''
  dict_={}
  a=0

  for k in range (len(use)):
     if use[k]==' ': 
       values=dict_.values()
       values_=set(values)
       if string not in values_ and string!=' ':
         print(f" occurrence of {string} = {use. count (string)}")
         dict_[a] =string
         a+=1
       string=''
       
     if use[k]!=' ':
       string+=use[k]
       if k== len(use)-1 :
         values=dict_.values()
         values_=set(values)
         if string not in values_ and string!=' ':
           print(f" occurrence of {string} = {use. count (string)}")
