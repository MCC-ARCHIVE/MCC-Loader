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
    ║      Ghost      ║    [00] General         │    [1.2] Vestige            ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [2.2] Huzuni             ║    
    ║—————Blatant—————║    [02] Blatant Clients │    [3.2] Sigma              ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [4.2] FDP Client         ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [5.2] Kawaii Client      ║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [6.2] EvoBounce          ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [7.2] Lint               ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [8.2] Tenacity [v5.1 HCU]║    
    ║       CS2       ║    [08] MC plugins      │    [9.2] Stitch Client      ║    
    ╠═════════════════╣    [09] Spoofer         │    [10.2] Novoline [v4.8]   ║    
    ║     Valorant    ║    [10] Cracks          │    [11.2] Crosssine B31     ║    
    ╠═════════════════╣    [11] Others          │    [12.2] Blaze Client      ║    
    ║      Roblox     ║                         │    [13.2] ZeroDay Client    ║    
    ╠═════════════════╣                         │    [14.2] Moon Client       ║    
    ║     Plugins     ║                         │    [15.2] Rise cracked      ║    
    ╠═════════════════╣                         │    [16.2] Dortware          ║    
    ║     Spoofer     ║                         │    [17.2] Drunk Client      ║    
    ╠═════════════════╣                         │    [18.2] EaZy B1337        ║    
    ║     Cracks      ║                         │    [19.2] Astrohook Client  ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║                                  [21] Next Page =>    ║    
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
        os.system("cls")
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_page_2.py').text)
    if chon == '1.2':
        os.system("cls")
        exec(requests.get("https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Vestige").text)
    if chon == '2.2':
        webbrowser.open_new("https://www.mediafire.com/file/vcaoo6kam878h07/huzuni.rar/file")
    if chon == '3.2':
        webbrowser.open_new("https://www.mediafire.com/file/z1dpsfi8ow4k0ar/sigma.zip/file")
    if chon == '4.2':
        webbrowser.open_new("https://www.mediafire.com/file/76pwmepnhmh1j3r/FDP_Client_Clean_4934678.jar/file")
    if chon == '5.2':
        webbrowser.open_new("https://drive.google.com/file/d/1bMBKvXvoqv85LvMnCUIUh3jkSwtkcw4R/view")
    if chon == '6.2':
        webbrowser.open_new("https://drive.google.com/file/d/1DiKI8M4TAnhvYEHCHdQgMjhkls33jDF9/view")
    if chon == '7.2':
        webbrowser.open_new("https://drive.google.com/file/d/1NjWP-HWSenlE8dWmbBfoGbN_UU2GZhmL/view")
    if chon == '8.2':
        webbrowser.open_new("https://workupload.com/file/Re6GJ2mWXJX")
    if chon == '9.2':
        webbrowser.open_new("https://mega.nz/file/bsUnwRAK#yZO4wbWA86a8YNtuniVAQtkcxf1lasYuXxTL0gdSMKs")
    if chon == '10.2':
        webbrowser.open_new("https://anotepad.com/notes/pndjshra")
    if chon == '11.2':
        webbrowser.open_new("https://www.mediafire.com/file/ek0gg130dm767rb/CrossSine-B31.jar/file")
    if chon == '12.2':
        webbrowser.open_new("https://www.mediafire.com/file/vti3ff68h26jhvu/BlazeClient.zip/file")
    if chon == '13.2':
        webbrowser.open_new("https://www.mediafire.com/file/rvje41s01i4gary/zrd.zip/file")
    if chon == '14.2':
        webbrowser.open_new("https://www.mediafire.com/file/komh0qjyq6lh6de/Moon.rar/file")
    if chon == '15.2':
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_rise.py').text)
    if chon == '16.2':
        webbrowser.open_new("https://www.mediafire.com/file/itc99scy7znfwfd/Dortware.zip/file")
    if chon == '17.2':
        webbrowser.open_new("https://www.mediafire.com/file/cy4g72taj57119o/Drunk_Client.zip/file")
    if chon == '18.2':
        webbrowser.open_new("https://www.mediafire.com/file/wdoyfxhb4id2nkp/EaZy+b1337.zip/file")
    if chon == '19.2':
        webbrowser.open_new("https://www.mediafire.com/file/wzh1dzuqynvo7fz/Astrohook_1.8.8.zip/file")
    else:
        print("\033[F\033[K", end="", flush=True)