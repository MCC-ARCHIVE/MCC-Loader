import subprocess, os
import tkinter as tk
from tkinter import messagebox
import webbrowser, os, re, json, random
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import requests, random, re
    from random import choice, randint, shuffle
    import requests, pystyle
    from pystyle import Write, Colors, Colorate
except:
    os.system("pip install faker")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system('pip install requests && pip install bs4 && pip install pystyle && pip install pycryptodome && pip install gratient')
mine = """
\n
    ╔═════════════════════════════════════════════════════════════════════════╗    
    ║______  ___________________   ______              _________              ║    
    ║___   |/  /_  ____/_  ____/   ___  / ____________ ______  /____________  ║    
    ║__  /|_/ /_  /    _  /        __  /  _  __ \  __ `/  __  /_  _ \_  ___/  ║    
    ║_  /  / / / /___  / /___      _  /___/ /_/ / /_/ // /_/ / /  __/  /      ║    
    ║/_/  /_/  \____/  \____/      /_____/\____/\__,_/ \__,_/  \___//_/       ║    
    ╚═════════════════════════════════════════════════════════════════════════╝    


    ╔═════════════════╦═══════════════════════════════════════════════════════╗    
    ║     General     ║                                                       ║    
    ╠═════════════════╣  MENU:                  │  BLATANT CLIENTS:           ║    
    ║      Ghost      ║    [00] General         │    [P] Rise patcher         ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [3.8] Rise v3.8          ║    
    ║—————Blatant—————║    [02] Blatant Clients │    [3.9] Rise v3.9          ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [3.92] Rise 3.92         ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [4.0] Rise v4.0          ║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [4.1] Rise v4.1          ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [4.4] Rise v4.4          ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [5.0] Rise v5.0          ║    
    ║       CS2       ║    [08] MC plugins      │    [5.1] Rise v5.1          ║    
    ╠═════════════════╣    [09] Spoofer         │    [5.31] Rise 5.31         ║    
    ║     Valorant    ║    [10] Cracks          │    [5.90] Rise v5.90        ║    
    ╠═════════════════╣    [11] Others          │    [5.98] Rise v5.98        ║    
    ║      Roblox     ║                         │    [5.103] Rise v5.100 r3   ║    
    ╠═════════════════╣                         │    [6.0] Rise v6.0          ║    
    ║     Plugins     ║                         │    [6.0.9] Rise v6.0.9      ║    
    ╠═════════════════╣                         │    [6.0.22] Rise v6.0.22    ║    
    ║     Spoofer     ║                         │    [6.0.24] Rise v6.0.24    ║    
    ╠═════════════════╣                         │    [6.1] Rise v6.1          ║    
    ║     Cracks      ║                         │    [6.1.25] Rise v6.1.25    ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║                                  [19] Go back =>      ║	    
    ╚═════════════════════════════════════════════════════════════════════════╝  
\n
"""

print(Colorate.Horizontal(Colors.purple_to_blue, mine, 1))
print("\n")
while True:
    chon = Write.Input("    [blatant@input] >  ", Colors.purple_to_blue, interval=0.0025)
    if chon == '00':
        print("                                              \033[1;39mLoading General Page..")
        os.system("cls")
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/general.py').text)
    if chon == '01':
        print("                                              \033[1;39mLoading Ghost Clients Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/ghost/ghost_page_1.py').text)
    if chon == '02':
        print("                                              \033[1;39mLoading Blatant Clients Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_page_1.py').text)
    if chon == '03':
        print("                                              \033[1;39mLoading Anarchy Clients Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/anarchy/anarchy_page_1.py').text) 
    if chon == '04':
        print("                                              \033[1;39mLoading Autoclicker Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/autoclicker/autoclicker_page_1.py').text)
    if chon == '05':
        print("                                              \033[1;39mLoading CS2 Cheats Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/cs2.py').text)
    if chon == '06':
        print("                                              \033[1;39mLoading Valorant Cheats  Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/valorant.py').text)
    if chon == '07':
        print("                                              \033[1;39mLoading Roblox Cheats Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/roblox.py').text)
    if chon == '08':
        print("                                              \033[1;39mLoading Minecraft plugins Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/plugins/plugins_page_1.py').text)
    if chon == '09':
        print("                                              \033[1;39mLoading Spoofer Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/spoofer.py').text)
    if chon == '10':
        print("                                              \033[1;39mLoading Cracks Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/cracks.py').text)
    if chon == '11':
        print("                                              \033[1;39mLoading Others Page..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/others/others_page_1.py').text)
    if chon == '19':
        print("                                              \033[1;39mLoading Blatant Page 1..")
        os.system("cls")
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_page_1.py').text)
    if chon == '1.2':
        os.system("cls")
        exec(requests.get("https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Vestige").text)
    if chon == 'P':
          webbrowser.open_new("https://www.mediafire.com/file/48i74z1wnp4icox/Rise+Patcher.zip/file")
    if chon == '3.8':
          webbrowser.open_new("https://www.mediafire.com/file/2i5u9ixwevrb7fy/Rise_3.8.zip/file")
    if chon == '3.9':
          webbrowser.open_new("https://www.mediafire.com/file/3mcbv2dlvu7jkcw/Rise_3.92.zip/file")
    if chon == '3.92':
          webbrowser.open_new("https://www.mediafire.com/file/3mcbv2dlvu7jkcw/Rise_3.92.zip/file")
    if chon == '4.0':
          webbrowser.open_new("https://www.mediafire.com/file/g9zdwih1hc6rfrq/Rise_b4.0.zip/file")
    if chon == '4.1':
          webbrowser.open_new("https://www.mediafire.com/file/1j4gkfvos0odsvn/Rise_b4.1.zip/file")
    if chon == '4.4':
          webbrowser.open_new("https://www.mediafire.com/file/731nczf2i4sxvzv/Rise_b4.4.zip/file")
    if chon == '5.0':
          webbrowser.open_new("https://www.mediafire.com/file/yudbu3qa11qqya3/Rise_5.0.zip/file")
    if chon == '5.1':
          webbrowser.open_new("https://www.mediafire.com/file/novpq1k74ctn78b/Rise_5.1.zip/file")
    if chon == '5.31':
          webbrowser.open_new("https://www.mediafire.com/file/taz0cfp42ad4uhg/Rise_5.31.zip/file")
    if chon == '5.90':
          webbrowser.open_new("https://www.mediafire.com/file/yon24htp9y74b5m/Rise_5.90.zip/file")
    if chon == '5.98':
          webbrowser.open_new("https://www.mediafire.com/file/gqpw9ewb1ca0khh/Rise5.98.zip/file")
    if chon == '5.103':
          webbrowser.open_new("https://www.mediafire.com/file/0xbcmhb8or2ahx8/Rise5.100r3.zip/file")
    if chon == '6.02':
          webbrowser.open_new("https://www.mediafire.com/file/nmcnc96irhehem1/Rise6.0pre2.zip/file")
    if chon == '6.03':
          webbrowser.open_new("https://www.mediafire.com/file/swv5mu58fcobii6/Rise_6.0pre3.zip/file")
    if chon == '6.04':
          webbrowser.open_new("https://www.mediafire.com/file/fyf2h5qdln4iefk/Rise_6.0pre4.zip/file")
    if chon == '6.0':
          webbrowser.open_new("https://www.mediafire.com/file/e8ohjc54bw840ep/Rise_6.zip/file")
    if chon == '6.0.9':
          webbrowser.open_new("https://www.mediafire.com/file/cd3bl142w5xycad/Risee.zip/file")
    if chon == '6.0.22':
          webbrowser.open_new("https://www.mediafire.com/file/8hokbdxmnfvguwz/Rise+6.0.22+beta.zip/file")
    if chon == '6.0.24':
          webbrowser.open_new("https://mega.nz/file/gnJkzBSa#SKCmxOD7D38Mg9M53EN0_phpDP7Or2spzZD35XFOhCg")
    if chon == '6.1':
          webbrowser.open_new("https://www.masterof13fps.com/forum/threads/rise-cracked-by-qreaj.8954/")
    if chon == '6.1.25':
          webbrowser.open_new("https://workupload.com/start/tEH4ZYGhPPq")
    else:
        print("\033[F\033[K", end="", flush=True)