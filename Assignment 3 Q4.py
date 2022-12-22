# Assignment 3 
# Question 4

dict_1={4:"D",5:"C",6:"C+",7:"B",8:"B+",9:"A",10:"A+"}
dict_2={4:"Poor",5:"Below Average",6:"Average",7:"Good",8:"Very Good",9:"Excellent",10:"Outstanding"}
 
print ("Enter ur grade number, it should be between 4 and 10) ")
grade=input ()
a=int (grade)

if a<4 or a>10:
  print (" Invalid grade number ")
else :
  print (f"Your grade is '{dict_1[a]}' and {dict_2[a]} performance ")
