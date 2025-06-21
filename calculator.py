#to create calculator
def calculator(op,num_1,num_2):
  if op == '+':
    return(num_1 + num_2)
  elif op == '-' :
    return(num_1 - num_2)
  elif op == '*' :
    return(num_1 * num_2)
  elif op == '/' :
    return(num_1 / num_2)
  else :
    return("invalid operation")
  print(calculator(c,a,b))

a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=input("enter operation")
print(calculator(c,a,b))
m=input("do you want to use calculator again:(yes/no)")
while m=='yes':
  a=float(input("enter first number:"))
  b=float(input("enter second number:"))
  c=input("enter operation")
  print(calculator(c,a,b))
  m=input("do you want to use calculator again:(yes/no)")
print("thankyou for using calculator:)")