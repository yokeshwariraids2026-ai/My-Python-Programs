#student marks,Percentage and grade
name=input("Enter your name:")
n=int(input("Enter no of subjects:"))
total=0;
for i in range(1,6):
    mark=float(input(f"Enter marks for subject{i}:"))
    total+=mark
    
percentage=total/5
if percentage>=90:
   grade="A+"
   performance="Outstanding"
elif percentage>=80:
     grade="A"
     performance="Excellent"
elif percentage>=70:
    grade="B"
    performance="Very Good"
elif percentage>=60:
     grade="C"
     performance="Good"
elif percentage>=50:
     grade+"D"
     performance="Average"
else:
    grade="E"
    performance="Needs Improvement"
print(f"\n--Academic Performance--")
print("student name:",name)
print("total marks:",total)
print("percentage:",round(percentage,2),"%")
print("grade:",grade)
print("performance:",performance)
       
       
