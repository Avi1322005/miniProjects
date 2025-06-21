#Number guessing game
import random
a = random.randint(0,100)
b = int(input("guess a number between 0-100:\n"))
count = 1
while(a != b):
 if(a > b):
  print("---------------guess higher---------------")
  b = int(input("guess a number betweem 0-100:\n"))
  count += 1
 elif(a < b):
  print("----------------guess lower---------------")
  b = int(input("guess a number between 0-100:\n"))
  count += 1
  count += 1
if(a == b):
  print(":-:-:-:-:-:-:-:-:-:you guessed in ",count," tries :-:-:-:-:-:-:-:-:-:")