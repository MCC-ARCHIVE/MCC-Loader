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
    ╠═════════════════╣  MENU:                  │  RAVEN ARCHIVE :            ║    
    ║——————Ghost——————║    [00] General         │    [B3] Raven B3            ║        
    ╠═════════════════╣    [01] Ghost Clients   │    [B+] Raven B+            ║    
    ║     Blatant     ║    [02] Blatant Clients │    [B++] Raven B++          ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [B+++] Raven B+++        ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [B++R] Raven B++ Reborn  ║     
    ╠═════════════════╣    [05] CS2 Cheats      │    [FB4] Fake Raven B4      ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [S1] Raven S1            ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [X] Raven X [Risky]      ║    
    ║       CS2       ║    [08] MC plugins      │    [BX] Raven BX            ║    
    ╠═════════════════╣    [09] Spoofer         │    [N+] Raven N+ [Risky]    ║    
    ║     Valorant    ║    [10] Cracks          │    [L] Raven N+ Lite        ║    
    ╠═════════════════╣    [11] Others          │    [B-] Raven B-            ║    
    ║      Roblox     ║                         │    [B4] Raven B4            ║    
    ╠═════════════════╣                         │    [A] Raven A [Skids]      ║    
    ║     Plugins     ║                         │    [S+] Raven S+            ║    
    ╠═════════════════╣                         │                             ║    
    ║     Spoofer     ║                         │                             ║    
    ╠═════════════════╣                         │                             ║    
    ║     Cracks      ║                         │                             ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║                                  [19] <= Go Back      ║    
    ╚═════════════════════════════════════════════════════════════════════════╝  
\n
"""

print(Colorate.Horizontal(Colors.purple_to_blue, mine, 1))
print("\n")
while True:
    chon = Write.Input("    [raven@input] >  ", Colors.purple_to_blue, interval=0.0025)
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
        print("                                              \033[1;39mLoading Ghost Page 1..")
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/ghost/ghost_page_1.py').text)
    if chon == 'B1':
        webbrowser.open_new("https://www.mediafire.com/file/dz2qqfvx8rv4s6s/[1.7.10]_Keystrokes_V4.jar/file")
    if chon == 'B2':
        webbrowser.open_new("https://www.mediafire.com/file/frqynrmi3qh9atn/raven_b2.jar/file")
    if chon == 'B3':
        webbrowser.open_new("https://www.mediafire.com/file/r2x3e7nfq88v849/ravenb3.zip/file")
    if chon == 'B+':
        webbrowser.open_new("https://github.com/Kopamed/Raven-bPLUS/releases/download/Stable1.0.26/1.8.9.BetterKeystrokes.V-1.2.jar")
    if chon == 'B++':
        webbrowser.open_new("https://k-ov.github.io/download/")
    if chon == 'B+++':
        webbrowser.open_new("https://cdn.discordapp.com/attachments/1152589174810103818/1157414961774088282/Sinner.jar")
    if chon == 'B++R':
        webbrowser.open_new("https://cdn.discordapp.com/attachments/1138115213447671932/1145748794114326569/RavenBReborn.jar")
    if chon == 'FB4':
        webbrowser.open_new("https://www.mediafire.com/file/nb0rnnb7mqmkkt8/FakeB4.zip/file")
    if chon == 'S1':
        webbrowser.open_new("https://www.mediafire.com/file/ftv4k9aep23zagp/1.8.9.Raven-S.1.jar/file")
    if chon == 'X':
        webbrowser.open_new("https://www.mediafire.com/file/0hkctqy63j5hd4r/X.zip/file")
    if chon == 'BX':
        webbrowser.open_new("https://www.mediafire.com/file/720dih1uhqu1ri7/[1.8.9]+BetterKeystrokes+V-1.2.jar/file")
    if chon == 'N+':
        webbrowser.open_new("https://cdn.discordapp.com/attachments/1013680734122287164/1037892344319578142/1.8.9_Raven-_N.jar")
    if chon == 'L':
        webbrowser.open_new("https://www.mediafire.com/file/78hs3x5hs6imefw/Raven+N.zip/file")
    if chon == 'B-':
        webbrowser.open_new("https://github.com/WalmartSolutions/RavenB-Latest")
    if chon == 'B4':
        webbrowser.open_new("https://anotepad.com/notes/j53d73qn")
    if chon == 'A':
        webbrowser.open_new("https://cdn.discordapp.com/attachments/1152589174810103818/1165317912068890776/b5.jar?ex=65870360&is=65748e60&hm=5dcdf41f1046800237921099b580554a4e44737fbb5f0823787b659072b42fb3&")
    if chon == 'S+':
        webbrowser.open_new("https://www.mediafire.com/file/6zlm2zahvmq3sit/Raven+S+.zip/file")

    else:
        print("\033[F\033[K", end="", flush=True)