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
    ║      Ghost      ║    [00] General         │    [39.2] Azura             ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [40.2] Eris [v0.1b]      ║    
    ║—————Blatant—————║    [02] Blatant Clients │    [41.2] Gravity [V2.1]    ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [42.2] MythRecode        ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [43.2] Resolute          ║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [44.2] Exhibition        ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [45.2] Raze Launcher     ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [46.2] Tank Client       ║    
    ║       CS2       ║    [08] MC plugins      │    [47.2] Lirium Client     ║    
    ╠═════════════════╣    [09] Spoofer         │    [48.2] Eject Client      ║    
    ║     Valorant    ║    [10] Cracks          │    [49.2] Nursultan Client  ║    
    ╠═════════════════╣    [11] Others          │    [50.2] Aritum Client     ║    
    ║      Roblox     ║                         │    [51.2] Trinity Client    ║    
    ╠═════════════════╣                         │    [52.2] Fan               ║    
    ║     Plugins     ║                         │    [53.2] Astolfo Client    ║    
    ╠═════════════════╣                         │    [54.2] Milky B4          ║    
    ║     Spoofer     ║                         │    [55.2] IntCrack [Old]    ║    
    ╠═════════════════╣                         │    [56.2] Gothaj Client     ║    
    ║     Cracks      ║                         │    [57.2] Kevin Client      ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║  [21] Prev Page <=      │        [23] Next Page =>    ║   
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
    if chon == '21':
        print("                                              \033[1;39mLoading Blatant Page 2..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_page_2.py').text)
    if chon == '23':
        print("                                              \033[1;39mLoading Blatant Page 4..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_page_4.py').text)
    if chon == '39.2':
        webbrowser.open_new("https://www.mediafire.com/file/1yhvf0i0mpl2dbt/Azura.zip/file")
    if chon == '40.2':
        webbrowser.open_new("https://www.mediafire.com/file/uv4tlaun90mdm5t/Eris_v0.1b.zip/file")
    if chon == '41.2':
        webbrowser.open_new("https://www.mediafire.com/file/2xf07ank6q8hn7k/Gravity_2.1.zip/file")
    if chon == '42.2':
        webbrowser.open_new("https://www.mediafire.com/file/cjnhbq8zi6ymud2/MythRecode.zip/file")
    if chon == '43.2':
        webbrowser.open_new("https://www.mediafire.com/file/lykk51nxnj69rug/Resolute.zip/file")
    if chon == '44.2':
        webbrowser.open_new("https://mimhax.netlify.app/Files/Exhibition.zip")
    if chon == '45.2':
        webbrowser.open_new("https://workupload.com/file/rtDnzJ4AdHD")
    if chon == '46.2':
        webbrowser.open_new("https://www.mediafire.com/file/oh5i9phntq5belu/TANK_V4.rar/file")
    if chon == '47.2':
        webbrowser.open_new("https://www.mediafire.com/file/f58fm3ala4gd9jh/Lirium.zip/file")
    if chon == '48.2':
        webbrowser.open_new("https://workupload.com/file/KNBVq9RWveV")
    if chon == '49.2':
        webbrowser.open_new("https://www.mediafire.com/file/7o90az3854e6nrk/Nur_6.5.rar/file")
    if chon == '50.2':
        webbrowser.open_new("https://www.mediafire.com/file/jdgcjay0c2cxr9o/Aritum.zip/file")
    if chon == '51.2':
        webbrowser.open_new("https://www.mediafire.com/file/mtx81r37t9m17i8/Trinity_2.10.zip/file")
    if chon == '52.2':
        webbrowser.open_new("https://www.mediafire.com/file/v6aky6mbt122h1s/Fan.zip/file")
    if chon == '53.2':
        webbrowser.open_new("https://anotepad.com/notes/gpniw2gw")
    if chon == '54.2':
        webbrowser.open_new("https://www.mediafire.com/file/ys7mbvidluv4ehb/Milky_b4.zip/file")
    if chon == '55.2':
        webbrowser.open_new("https://www.mediafire.com/file/t25fequ4ap6j9tz/IntCrack_%2528old%2529.zip/file")
    if chon == '56.2':
        webbrowser.open_new("https://www.mediafire.com/file/d2286khjb7adwnr/Gothaj.zip/file")
    if chon == '57.2':
        webbrowser.open_new("https://github.com/RE-KevinClient/KevinClient-Reborn/releases/tag/u2.4.8")
    else:
        print("\033[F\033[K", end="", flush=True)