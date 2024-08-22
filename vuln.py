import requests
import os
import re
import time
from colorama import Fore
import sys
from multiprocessing.dummy import Pool
from time import time as timer

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
""")

os.system("touch verratti.txt")

target = input(f"{Fore.WHITE}Enter Your {Fore.RED} Target {Fore.WHITE} like * example.com * >> ")
urls = requests.get(f"https://web.archive.org/cdx/search/cdx?url=*.{target}/*&output=txt&fl=original&collapse=urlkey&page=/")

with open('alien.txt', 'a') as file:
    file.write(str(urls.text) + "\n")

with open('alien.txt', 'r') as read:
    rs = read.read().splitlines()

def scan(url):
    if '.php?' in url:
        print(f"{Fore.WHITE}start{Fore.RED} scanning {Fore.WHITE}")
        url2 = re.sub(r'=.*', '=', url)
        xss.exploit(url2)
        time.sleep(5)
        lfi.exploit(url2)
        time.sleep(5)
        rfi.exploit(url2)
        time.sleep(5)
        sqli.exploit(url2)

def Main():
    try:
        for url in rs:
            start = timer()
            ThreadPool = Pool(100)
            ThreadPool.map(scan, [url])  
            ThreadPool.close()
            ThreadPool.join()
            print('TIME TAKEN: ' + str(timer() - start) + ' S')
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    Main()



