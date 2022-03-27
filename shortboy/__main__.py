import time
from colorama import Fore
import os

infinity=1

while infinity==1:
  os.system("bash main.bash")
  print("")
  a = input(Fore.MAGENTA+"Your Option:")
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
    print(Fore.Red+"Short but wrong 😎")
    time.sleep(2)
    os.system("clear")
