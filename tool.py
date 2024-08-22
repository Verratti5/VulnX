import urllib.parse
import urllib
import requests
import re
import threading
import sys
import os
from colorama import Fore
import xss
import sqli
import rfi
import lfi
import socket
import json
import informa
import robots
import vuln
import nslookup

Z = "\033[1;31m"  
X = "\033[1;33m"  
Z1 = "\033[2;31m"  
F = "\033[2;32m"  
A = "\033[2;34m"  
C = "\033[2;35m"  
B = "\033[2;36m"  
Y = "\033[1;34m"  
black = "\033[30m"  
red = "\033[31m"  
green = "\033[32m"  
orange = "\033[33m"  
blue = "\033[34m"  
purple = "\033[35m"  
heavenly = "\033[36m"  
light_gray = "\033[37m"  
w = Fore.WHITE

logo = f"""
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
"""

print(logo)

print(Fore.WHITE + f"""
      [1] scan target of sqli, xss, lfi, rfi
      [2] get information and more
      """)

select = str(input("Enter Your Number >>:"))
if select == '1':
    vuln.main()
elif select == "2":
    try:
        domain = input("Enter Your Target like * https://example.com/ * >> ")
        protocol = urllib.parse.urlparse(domain).scheme
        target = parse = urllib.parse.urlparse(domain).netloc
        response = requests.head(domain)
        server = response.headers.get("Server")
        ipadd = socket.gethostbyname(target)
        x = "-" * 70
        print(f"{Fore.WHITE}[{Fore.BLUE}EVENT{Fore.WHITE}] Getting info about ({Fore.BLUE}{domain}{Fore.WHITE})\n {x}")
        print(x)
        print(f"{Fore.WHITE}[{Fore.BLUE}INFO{Fore.WHITE}] DOMAIN.: {target}")
        print(f"{Fore.WHITE}[{Fore.BLUE}INFO{Fore.WHITE}] SERVER.: {server}")
        print(f"{Fore.WHITE}[{Fore.BLUE}INFO{Fore.WHITE}] IP.: {ipadd}\n{x}")
        print(f"{Fore.WHITE}[{Fore.BLUE}EVENT{Fore.WHITE}] scan ({Fore.RED}robots.txt{Fore.WHITE})\n {x}")
        robots.robots_scan(domain=domain)
        print(x)
        print(f"{Fore.WHITE}[{Fore.BLUE}EVENT{Fore.WHITE}] nslookup\n {x}")
        nslookup.nslookup(target=target)
        print(x)
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")
else:
    print(f"{Fore.RED}Please Enter Select Number")
