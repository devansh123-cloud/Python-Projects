# Conditions for the code 
# 90–100: A+
# 80–89: A
# 70–79: B
# 60–69: C
# <60: F

name = input("Enter students name : ")
maths = int(input("Enter maths marks:"))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks:"))

avg = (maths + english + science)/3

print(f"{name}'s Report Card")


if (avg>= 90):
    print("A+")
    print("Excellent")
    
elif (avg>= 80):
    print("A")
    print("Great Job")
    
elif (avg>=70):
      print("B+")
      print("Good Job")
    
        
elif (avg>=60):
      print("B")
      print("Good")
      
          
elif (avg>=50):
      print("C")
      print("Work Harder")
          
elif (avg>=40):
      print("F")
      print("Better luck Next Time")
      
      
    
    
    

# if avg >= 90:
#     grade = "A+"
# elif avg >= 80:
#     grade = "A"
# elif avg >= 70:
#     grade = "B"
# elif avg >= 60:
#     grade = "C"
# elif avg >= 50:
#     grade = "D"
# else:
#     grade = "F"
    
    # print("--- Report Card ---")
    # print(f"Name:{name}")
    # print(f"Maths:{maths}")
    # print(f"science:{science}")
    # print(f"english:{english}")
    # print(f"average:{avg}")
    # print(f"Grade :{grade} ")
    
    # if grade in ["A+" ,"A", "B"]:
    #     print(f"Great Job : {name}")
        
    # else:
    #     print(f"WorkHarder: {name}")


