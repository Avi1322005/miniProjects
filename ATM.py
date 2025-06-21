# to create ATM software with witdraw, check balance, and deposit option

balance=float(input("what is your current balnce:"))
def atm(op,amount):
  if op == 1:
    x=float(input("enter amount you want to add: "))
    print("your current balance is: ",balance+x)
  elif op == 2:
    y=float(input("enter amount you want to withdraw: "))
    if y > balance:
      print("insufficient balance")
    else:
      print("your current balance is: ",balance-y)
  elif op == 3:
    print("your current balance is: ",balance)
  else:
    print("invalid option")
op = int(input("""select any one option:
               1.DEPOSIT
               2.WITHDRAW
               3.CHECK BALANCE """
))
atm(op,balance)
m=input("do you want to use ATM again:(yes/no)")
while m=='yes':
  op = int(input("""select any one option:
               1.DEPOSIT
               2.WITHDRAW
               3.CHECK BALANCE """
))
  atm(op,balance)
  m=input("do you want to use ATM again:(yes/no)")
print("thankyou for using ATM:)")