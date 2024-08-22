from bs4 import BeautifulSoup
import urllib3

def nslookup(target):
    http = urllib3.PoolManager()
    url = http.request('GET', 'https://api.hackertarget.com/dnslookup/?q=' + target).data
    soup = BeautifulSoup(url, 'lxml')
    print(soup.p.string)

def Information():
    ip = urllib3.PoolManager().request('GET', "https://wtfismyip.com/text").data.decode('utf-8')
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
