#Dev Morais 2.0
import argparse as co
import os
import time
import colorama
from colorama import Fore, Back, Style
import webbrowser
def pynish():
    os.system("clear")
    print("Loading...")
    time.sleep(3)
    os.system("pkg install python-pip")
    os.system("pip install colorama")

    os.system("clear")
    colorama.init(autoreset=True)
    apres = (Fore.BLUE + """
      ______                __         __
     |   __ \.--.--..-----.|__|.-----.|  |--.
     |    __/|  |  ||     ||  ||__ --||     |
     |___|   |___  ||__|__||__||_____||__|__|
             |_____|

           Developer: Dev Morais
           Data: 9/Julho/2024
           Version: 2.1
       """)
    print(apres)
    print(Fore.RED + """
    [1] - Hydra Install
    [2] - Kali Termux Install
    [3] - Exit Pynish
    [4] - Slowloris Linux
    [5] - Nmap Termux
    [6] - Sqlmap Install
    [7] - Metasploit Install
    [8] - Dirb Install
    [9] - WebSite [Confiável]
    """)
    option = input("--> ")

    if option == "1":
        time.sleep(1)
        print(Fore.YELLOW + "[==2%]")
        time.sleep(3)
        print(Fore.YELLOW + "[======25%]")
        time.sleep(2)
        print(Fore.YELLOW + "[===========60%]")
        time.sleep(5)
        print(Fore.YELLOW + "[100%]")
        os.system("clear")
        print(apres)
        os.system("pkg install hydra -y")
        print(Fore.GREEN + "Installation done successfully")
    elif option == "2":
        time.sleep(1)
        print(Fore.YELLOW + "[==2%]")
        time.sleep(3)
        print(Fore.YELLOW + "[======25%]")
        time.sleep(2)
        print(Fore.YELLOW + "[===========60%]")
        time.sleep(5)
        print(Fore.YELLOW + "[100%]")
        os.system("clear")
        print(apres)
        os.system("termux-setup-storage")
        os.system("pkg install wget -y")
        os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
        os.system("chmod +x install-nethunter-termux")
        os.system("./install-nethunter-termux")
    elif option == "3":
        exit()
    elif option == "4":
        time.sleep(1)
        print(Fore.YELLOW + "[==2%]")
        time.sleep(3)
        print(Fore.YELLOW + "[======25%]")
        time.sleep(2)
        print(Fore.YELLOW + "[===========60%]")
        time.sleep(5)
        print(Fore.YELLOW + "[100%]")
        os.system("clear")
        print(apres)
        os.system("sudo apt-get install perl")
        os.system("git clone https://github.com/GHuom/GHubgenius/sl>")
        print(Fore.GREEN + "Installation done successfully")
    elif option == "5":
        time.sleep(1)
        print(Fore.YELLOW + "[==2%]")
        time.sleep(3)
        print(Fore.YELLOW + "[======25%]")
        time.sleep(2)
        print(Fore.YELLOW + "[===========60%]")
        time.sleep(5)
        print(Fore.YELLOW + "[100%]")
        os.system("clear")
        print(apres)
        os.system("apt install nmap -y")
        print(Fore.GREEN + "Installation done successfully")
    elif option == "6":
        time.sleep(1)
        print(Fore.YELLOW + "[==2%]")
        time.sleep(3)
        print(Fore.YELLOW + "[======25%]")
        time.sleep(2)
        print(Fore.YELLOW + "[===========60%]")
        time.sleep(5)
        print(Fore.YELLOW + "[100%]")
        os.system("clear")
        print(apres)
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
        print(Fore.GREEN + "Installation done successfully")
    elif option == "7":
      time.sleep(1)
      print(Fore.YELLOW + "[==2%]")
      time.sleep(3)
      print(Fore.YELLOW + "[======25%]")
      time.sleep(2)
      print(Fore.YELLOW + "[===========60%]")
      time.sleep(5)
      print(Fore.YELLOW + "[100%]")
      os.system("clear")
      print(apres)
      os.system("git clone https://github.com/gushmazuko/metasploit_in_termux.git")
      print(Fore.GREEN+"Installation done successfully")
    elif option == "8":
      time.sleep(1)
      print(Fore.YELLOW + "[==2%]")
      time.sleep(3)
      print(Fore.YELLOW + "[======25%]")
      time.sleep(2)
      print(Fore.YELLOW + "[===========60%]")
      time.sleep(5)
      print(Fore.YELLOW + "[100%]")
      os.system("clear")
      print(apres)
      os.system("pkg install dirb")
      print(Fore.GREEN+"Installation done successfully")
    elif option == 9:
        time.sleep(1)
        print(Fore.YELLOW + "[==2%]")
        time.sleep(3)
        print(Fore.YELLOW + "[======25%]")
        time.sleep(2)
        print(Fore.YELLOW + "[===========60%]")
        time.sleep(5)
        print(Fore.YELLOW + "[100%]")
        os.system("clear")
        print("https://registrar-dados.netlify.app")
        url = "https://registrar-dados.netlify.app"
        webbrowser.open(url)
        
        
        
      


def main():
    parser = co.ArgumentParser(description="Choose a number from 1 to 6 from the options")
    parser.add_argument('-a', type=int, help="Number to be chosen from the options")
    parser.add_argument('--list', metavar='STRING', type=str, nargs='?', const="Default message", help="Show list options")
    args = parser.parse_args()

    if args.list:
      print(Fore.RED + """
      [1] - Hydra Install
      [2] - Kali Termux Install
      [3] - Exit Pynish
      [4] - Slowloris Linux
      [5] - Nmap Termux
      [6] - Sqlmap Install
      [7] - Metasploit Install
      [8] - Dirb Install
      [9] - WebSite [Confiável]
      """)
      exit()

    if args.a:
        print(f"{args.a}")
        if args.a == 1:
          os.system("pkg install hydra -y")
          print(Fore.GREEN + "Installation done successfully")
        else:
          if args.a == 2:
            os.system("termux-setup-storage")
            os.system("pkg install wget -y")
            os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
            os.system("chmod +x install-nethunter-termux")
            os.system("./install-nethunter-termux")
          else:
            if args.a == 3:
              os.system("clear")
              print("""
              ####         ####
              #  #         #  #
              ###  ##  #   ###  ##  #
              # ##  # #    # ##  # #
              #  #  # #    #  #  # #
              ####   #     ####   #
                     #            #
                     #            #


              """)
              exit()
            else:
              if args.a == 4:
                os.system("sudo apt-get install perl")
                os.system("git clone https://github.com/GHuom/GHubgenius/sl>")
                print(Fore.GREEN + "Installation done successfully")
              else:
                if args.a == 5:
                  os.system("apt install nmap -y")
                  print(Fore.GREEN + "Installation done successfully")
                else:
                  if args.a == 6:
                    os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
                    print(Fore.GREEN + "Installation done successfully")
                  else:
                    if args.a == 7:
                      os.system("git clone https://github.com/gushmazuko/metasploit_in_termux.git")
                      print(Fore.GREEN+"Installation done successfully")
                    else:
                      if args.a == 8:
                        os.system("pkg install dirb")
                        print(Fore.GREEN+"Installation done successfully")
                      else:
                          if args.a == 9:
                              
                              print("https://registrar-dados.netlify.app")
                              url = "https://registrar-dados.netlify.app"
                              webbrowser.open(url)
                        
    else:
        pynish()

if __name__ == '__main__':
    main()
