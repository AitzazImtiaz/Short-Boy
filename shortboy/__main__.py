import time
from colorama import Fore
import os

infinity=1
os.system("clear")
while infinity==1:
  os.system("bash shortboy/main.bash")
  print("")
  a=int(input(Fore.MAGENTA+"Your Option:"))
  if a==1:
    os.system("python shortboy/scripts/bitly.py")
  elif a==2:
    os.system("python shortboy/scripts/cuttly.py")
  elif a==3:
    os.system("python shortboy/scripts/aboutme.py")
  elif a==4:
    os.system("clear") 
    exit()
  else:
    print(Fore.RED+"Short but wrong 😎")
    time.sleep(2)
    os.system("clear")
