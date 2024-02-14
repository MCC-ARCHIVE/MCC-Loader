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
    ╠═════════════════╣  MENU:                  │  GHOST CLIENTS:             ║    
    ║——————Ghost——————║    [00] General         │    [39.1] Bayoneta          ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [40.1] Vega Client       ║    
    ║     Blatant     ║    [02] Blatant Clients │    [41.1] Dope V2           ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [42.1] Sumo              ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [43.1] Evil Eye [Risky]  ║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [44.1] BetterTimeChanger ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [45.1] Candy             ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [46.1] Storm AimAssist   ║    
    ║       CS2       ║    [08] MC plugins      │    [47.1] Reach Displa      ║    
    ╠═════════════════╣    [09] Spoofer         │    [48.1] Noise             ║    
    ║     Valorant    ║    [10] Cracks          │    [49.1] Supremacy         ║    
    ╠═════════════════╣    [11] Others          │    [50.1] Sprite            ║    
    ║      Roblox     ║                         │    [51.1] Weizu Reach       ║    
    ╠═════════════════╣                         │    [52.1] Juul [Risky]      ║    
    ║     Plugins     ║                         │    [53.1] Enthapy           ║    
    ╠═════════════════╣                         │    [54.1] Legitish          ║    
    ║     Spoofer     ║                         │    [55.1] Ascension         ║    
    ╠═════════════════╣                         │    [56.1] North Client      ║    
    ║     Cracks      ║                         │    [57.1] November [3.03]   ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║   [20] <= Prev Page     │        [22] Next Page =>    ║    
    ╚═════════════════════════════════════════════════════════════════════════╝  
\n
"""

print(Colorate.Horizontal(Colors.purple_to_blue, mine, 1))
print("\n")
while True:
    chon = Write.Input("    [ghost@input] >  ", Colors.purple_to_blue, interval=0.0025)
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
    if chon == '39.1':
        webbrowser.open_new("https://www.mediafire.com/file/64h90bxzpy485wo/Bayoneta.zip/file")
    if chon == '40.1':
        webbrowser.open_new("https://mimhax.netlify.app/Files/vega.exe")
    if chon == '41.1':
        webbrowser.open_new("https://www.mediafire.com/file/22evfi1yvyaormy/Dope.zip/file")
    if chon == '42.1':
        webbrowser.open_new(
            "https://github.com/pesshown/Sumo-Ghost-Client-Mod-1.8.9/releases/download/1.8.9/cheatbreaker.ghost.client.rar")
    if chon == '43.1':
        webbrowser.open_new("https://www.mediafire.com/file/bq0hwesqqlpv5tk/EvilEye.zip/file")
    if chon == '44.1':
        webbrowser.open_new("https://www.mediafire.com/file/y3onjsycdh99fxe/BetterTimeChanger.zip/file")
    if chon == '45.1':
        webbrowser.open_new("https://www.mediafire.com/file/9y9i2dwo53bgqyc/Candy.zip/file")
    if chon == '46.1':
        webbrowser.open_new("https://www.mediafire.com/file/vivcxqep3ft1kfj/Storm.zip/file")
    if chon == '47.1':
        webbrowser.open_new("https://www.mediafire.com/file/1vyyqyveaux9ry4/ReachDisplay_Reach.zip/file")
    if chon == '48.1':
        webbrowser.open_new("https://www.mediafire.com/file/bnre5f11npssw7w/Noise.zip/file")
    if chon == '49.1':
        webbrowser.open_new("https://www.mediafire.com/file/pzuc1jjofuz71wd/Supremacy.zip/file")
    if chon == '50.1':
        webbrowser.open_new("https://www.mediafire.com/file/lr54bxtfgxrkua6/Sprite.zip/file")
    if chon == '51.1':
        webbrowser.open_new("https://www.mediafire.com/file/tsewloxt6w8c42o/Weizu_Reach.zip/file")
    if chon == '52.1':
        webbrowser.open_new("https://workupload.com/file/MmWj48xsHRN")
    if chon == '53.1':
        webbrowser.open_new("https://mega.nz/file/03onAJrL#97-ZrtBai1RkZ_a3vx8hCbdqrO-Kp5hxdnSkUGRqEmI")
    if chon == '54.1':
        webbrowser.open_new("https://www.mediafire.com/file/4s2cm60pk4end8j/Legitish.zip/file")
    if chon == '55.1':
        webbrowser.open_new("https://workupload.com/file/WheZ8nzR78H")
    if chon == '56.1':
        webbrowser.open_new("https://www.mediafire.com/file/g2qsbx61itsuki6/North+(2).zip/file")
    if chon == '57.1':
        webbrowser.open_new("https://www.mediafire.com/file/1gz6dk5dkzonr3s/November.zip/file")
    if chon == '20':
        print("                                              \033[1;39mLoading Ghost Page 2..")
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/ghost_page_2').text)
    if chon == '22':
        print("                                              \033[1;39mLoading Ghost Page 4..")
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/ghost_page_4').text)
    else:
        print("\033[F\033[K", end="", flush=True)