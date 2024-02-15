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
    ║      Ghost      ║    [00] General         │    [20.2] Autumn Client     ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [21.2] Crass B2          ║    
    ║—————Blatant—————║    [02] Blatant Clients │    [22.2] Deepwater Horizon ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [23.2] Ketamine          ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [24.2] Sativa Client     ║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [25.2] XatZ              ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [26.2] Senura Client     ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [27.2] LiquidX           ║    
    ║       CS2       ║    [08] MC plugins      │    [28.2] NightX            ║    
    ╠═════════════════╣    [09] Spoofer         │    [29.2] Old IcarusX[Risky]║    
    ║     Valorant    ║    [10] Cracks          │    [30.2] IceTea Client     ║    
    ╠═════════════════╣    [11] Misc            │    [31.2] DuckSense         ║    
    ║      Roblox     ║                         │    [32.2] Mylo Client       ║    
    ╠═════════════════╣                         │    [33.2] Weedhack          ║    
    ║     Plugins     ║                         │    [34.2] Vergo             ║    
    ╠═════════════════╣                         │    [35.2] Clean Client      ║    
    ║     Spoofer     ║                         │    [36.2] LiquidBounce      ║    
    ╠═════════════════╣                         │    [37.2] Augustus          ║    
    ║     Cracks      ║                         │    [38.2] Lime              ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║  [20] Prev Page <=      │        [22] Next Page =>    ║   
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
    if chon == '20':
        print("                                              \033[1;39mLoading Blatant Page 1..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_page_1.py').text)
    if chon == '22':
        print("                                              \033[1;39mLoading Blatant Page 3..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_page_3.py').text)
    if chon == '20.2':
        webbrowser.open_new("https://www.mediafire.com/file/a7hdv2aj1lrbo42/Autumn.zip/file")
    if chon == '21.2':
        webbrowser.open_new("https://www.mediafire.com/file/ey1vhkcz2o8k1yj/Crass_B2.rar/file")
    if chon == '22.2':
        webbrowser.open_new("https://www.mediafire.com/file/ipu0x5vekwy805x/DeepwaterHorizon.zip/file")
    if chon == '23.2':
        webbrowser.open_new("https://www.mediafire.com/file/gxvdxh7zzbw3lug/Ketamine.zip/file")
    if chon == '24.2':
        webbrowser.open_new("https://www.mediafire.com/file/eg8tn6wycpj7erl/Sativa.zip/file")
    if chon == '25.2':
        webbrowser.open_new("https://www.mediafire.com/file/vhwf5gmakavup4m/Xatz_Client.zip/file")
    if chon == '26.2':
        webbrowser.open_new("https://www.mediafire.com/file/agb4afnwe68h2mv/Senura.zip/file")
    if chon == '27.2':
        webbrowser.open_new("https://www.mediafire.com/file/vw3kenw8pm2fo6v/LiquidX-v3.3.jar/file")
    if chon == '28.2':
        webbrowser.open_new("https://www.mediafire.com/file/8x1mn0m10e5l68e/NightX-B57-Release.zip/file")
    if chon == '29.2':
        webbrowser.open_new("https://www.mediafire.com/file/a9gggfoltly67hl/IcarusX_old_version.rar/file")
    if chon == '30.2':
        webbrowser.open_new("https://www.mediafire.com/file/wbbf46q5mkut5qv/IceTea.zip/file")
    if chon == '31.2':
        webbrowser.open_new("https://www.mediafire.com/file/yja0jaor2kea9ew/DuckSense-Legacy.jar/file")
    if chon == '32.2':
        webbrowser.open_new("https://www.mediafire.com/file/ql1bcg75md94lls/Mylo.zip/file")
    if chon == '33.2':
        webbrowser.open_new("https://www.mediafire.com/file/o5zroqoyuev5vpv/Weedhack.zip/file")
    if chon == '34.2':
        webbrowser.open_new("https://www.mediafire.com/file/8olb1phsp7xtjxl/Vergo.zip/file")
    if chon == '35.2':
        webbrowser.open_new("https://www.mediafire.com/file/7qqpq8clygn4etr/Clean.zip/file")
    if chon == '36.2':
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/LiquidBounce').text)
    if chon == '37.2':
        webbrowser.open_new("https://qiwi.gg/file/2RcMi0g8Pig81WTyTmwEmxHChiy-317395-Augustus")
    if chon == '38.2':
        webbrowser.open_new("https://mimhax.netlify.app/Files/Lime.zip")
    else:
        print("\033[F\033[K", end="", flush=True)