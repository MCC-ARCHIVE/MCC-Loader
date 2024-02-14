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
    ╠═════════════════╣  MENU:                  │  VAPE CRACKED :             ║    
    ║——————Ghost——————║    [00] General         │    [4.10] Vape v4.10        ║        
    ╠═════════════════╣    [01] Ghost Clients   │    [4.06] Vape v4.06        ║    
    ║ Blatant Clients ║    [02] Blatant Clients │    [4.04] Vape v4.04 + Lite ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [3.25] Vape v3.25        ║    
    ║ Anarchy Clients ║    [04] Autoclicker     │                             ║    
    ╠═════════════════╣    [05] CS2 Cheats      │                             ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │                             ║    
    ╠═════════════════╣    [07] Roblox Cheats   │                             ║    
    ║    CS2 Cheats   ║    [08] Utilities       │                             ║    
    ╠═════════════════╣    [09] Discord         │                             ║    
    ║ Valorant Cheats ║    [10] Windows         │                             ║    
    ╠═════════════════╣    [11] Misc            │                             ║    
    ║      ONION      ║                         │                             ║    
    ╠═════════════════╣                         │                             ║    
    ║    UTILITIES    ║                         │                             ║    
    ╠═════════════════╣                         │                             ║    
    ║     DISCORD     ║                         │                             ║    
    ╠═════════════════╣                         │                             ║    
    ║     WINDOWS     ║                         │                             ║    
    ╠═════════════════╣                         │                             ║    
    ║      MISCS      ║                                  [19]  Go Back  <=    ║    
    ╚═════════════════════════════════════════════════════════════════════════╝  
\n
"""

print(Colorate.Horizontal(Colors.purple_to_blue, mine, 1))
print("\n")
while True:
    chon = Write.Input("    [vape@input] >  ", Colors.purple_to_blue, interval=0.0025)
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
    if chon == '3.25':
        webbrowser.open_new("https://www.mediafire.com/file/8coudk5wgq9ssla/Vape_v3.25.zip/file")
    if chon == '4.04':
        webbrowser.open_new("https://anotepad.com/notes/4qyx3tmb")
    if chon == '4.06':
        webbrowser.open_new("https://www.mediafire.com/file/4c02w3mpw89vjwv/Vape+4.06.zip/file")
    if chon == '4.10':
        webbrowser.open_new("https://pixeldrain.com/u/zELPqtnN")

    else:
        print("\033[F\033[K", end="", flush=True)