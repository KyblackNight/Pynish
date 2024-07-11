#Devloper: Morais
import time
import os
os.system("clear")
print("Loading...")
time.sleep(2)
os.system("apt install python3")
os.system("apt install python3-pip -y")
os.system("pip install colorama")



import colorama
from colorama import Fore, Back, Style
os.system("clear")
colorama.init(autoreset=True)


apres = (Fore.BLUE+"""
  ______                __         __
  |   __ \.--.--..-----.|__|.-----.|  |--.
  |    __/|  |  ||     ||  ||__ --||     |
  |___|   |___  ||__|__||__||_____||__|__|
          |_____|


        Developer:Dev Morais
        Data: 9/Julho/2024
""")


print(Fore.BLUE+"""

  ______                __         __
 |   __ \.--.--..-----.|__|.-----.|  |--.
 |    __/|  |  ||     ||  ||__ --||     |
 |___|   |___  ||__|__||__||_____||__|__|
         |_____|


       Developer:Dev Morais
       Data: 9/Julho/2024
       Version: 1.0


""")

time.sleep(3)



print(Fore.RED+"""

[1] - Hydra Install
[2] - Kali Termux Install
[3] - Exit Pynish
[4] - Slowloris Linux
[5] - Nmap Termux
[6] - Sqlmap Install


""")

time.sleep(2)

option = input("--> ")
print()

if option == "1":
  time.sleep(1)
  print(Fore.YELLOW+"[==2%]")
  time.sleep(3)
  print(Fore.YELLOW+"[======25%]")
  time.sleep(2)
  print(Fore.YELLOW+"[===========60%]")
  time.sleep(5)
  print(Fore.YELLOW+"[100%]")
  os.system("clear")
  apres = (Fore.BLUE+"""
  ______                __         __
  |   __ \.--.--..-----.|__|.-----.|  |--.
  |    __/|  |  ||     ||  ||__ --||     |
  |___|   |___  ||__|__||__||_____||__|__|
          |_____|


        Developer:Dev Morais
        Data: 9/Julho/2024
  """)
  print(apres)
  os.system("apt install hydra -y")
  print(Fore.GREEN+"Installation done successfully")
else: 
  if option =="2":
    
    time.sleep(1)
    print(Fore.YELLOW+"[==2%]")
    time.sleep(3)
    print(Fore.YELLOW+"[======25%]")
    time.sleep(2)
    print(Fore.YELLOW+"[===========60%]")
    time.sleep(5)
    print(Fore.YELLOW+"[100%]")
    os.system("clear")
    print(apres)
    os.system("termux-setup-storage")
    os.system("pkg install wget -y")
    os.system("wget -O install-nethunter-termux https://offs>")
    os.system("chmod +x install-nethunter-termux")
    os.system("./install-nethunter-termux")
  else:
              
              if option == "":
                print(Fore.YELLOW+"Invalid !")
              else:
                if option == "3": 
                  exit()
                else:
                  if option == "4":
                    oi
                    time.sleep(1)
                    print(Fore.YELLOW+"[==2%]")
                    time.sleep(3)
                    print(Fore.YELLOW+"[======25%]")
                    time.sleep(2)
                    print(Fore.YELLOW+"[===========60%]")
                    time.sleep(5)
                    print(Fore.YELLOW+"[100%]")
                    os.system("clear")
                    print(apres)
                    os.system("sudo apt-get install perl")
                    os.system("git clone https://github.com/GHubgenius/sl>")
                    os.system("cd slowloris.pl")
                    os.system("perl slowloris.pl")
                    print(Fore.GREEN+"Installation done successfully")
                  else:
                              
                              if option == "5":
                                time.sleep(1)
                                print(Fore.YELLOW+"[==2%]")
                                time.sleep(3)
                                print(Fore.YELLOW+"[======25%]")
                                time.sleep(2)
                                print(Fore.YELLOW+"[===========60%]")
                                time.sleep(5)
                                print(Fore.YELLOW+"[100%]")
                                os.system("clear")
                                print(apres)
                                os.system("apt install nmap -y")
                                print(Fore.GREEN+"Installation done successfully")
                              else:
                                if option == "6":
                                  time.sleep(1)
                                  print(Fore.YELLOW+"[==2%]")
                                  time.sleep(3)
                                  print(Fore.YELLOW+"[======25%]")
                                  time.sleep(2)
                                  print(Fore.YELLOW+"[===========60%]")
                                  time.sleep(5)
                                  print(Fore.YELLOW+"[100%]")
                                  os.system("clear")
                                  print(apres)
                                  os.system("git clone https://github.com/sqlmapprojec>")
                                  os.system("cd sqlmap")
                                  os.system("apt install python")
                                  os.system("python sqlmap.py")
                                else:
                                  print(Fore.YELLOW+"Invalid !")
                                  

