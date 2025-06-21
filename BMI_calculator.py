#to create BMI calculator
def BMI(height,weight):
  bmi=weight/(height**2)
  return(bmi)
height = int(input("enter height in cm:"))
weight = int(input("enter weight in kg:"))
print(BMI(height/100,weight))
if BMI(height/100,weight) < 18.5:
  print("you are underweight")
elif BMI(height/100,weight) >= 18.5 and BMI(height/100,weight) <= 24.9:
  print("you are normal")
else:
  print("you are overweight")