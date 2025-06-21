#Click on time game
import time
start = time.time()
x=input("press enter exactly after 10 seconds:")
end = time.time()
print("you clikced after ",int(end-start),"seconds")
if(int(end-start) ==  10):
  print("right on spot")
elif(int(end - start) < 10):
  print("you are too quick")
else:
  print("you are to slow")