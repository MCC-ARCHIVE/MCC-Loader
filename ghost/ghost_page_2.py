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
    ║——————Ghost——————║    [00] General         │    [20.1] Cucklord Reborn   ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [21.1] Elixe Client      ║    
    ║     Blatant     ║    [02] Blatant Clients │    [22.1] Iridium Client    ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [23.1] Axenta V2         ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [24.1] Smok [v2.2]       ║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [25.1] Itami Client      ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [26.1] Kriso B1          ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [27.1] Mind Client       ║    
    ║       CS2       ║    [08] MC plugins      │    [28.1] Mye Ghost         ║    
    ╠═════════════════╣    [09] Spoofer         │    [29.1] Nyctum            ║    
    ║     Valorant    ║    [10] Cracks          │    [30.1] Shiba             ║    
    ╠═════════════════╣    [11] Others          │    [31.1] Uboa V2           ║    
    ║      Roblox     ║                         │    [32.1] Karma [Old]       ║    
    ╠═════════════════╣                         │    [33.1] Whiteout [Working]║    
    ║     Plugins     ║                         │    [34.1] Emo Client        ║    
    ╠═════════════════╣                         │    [35.1] Epic Client       ║    
    ║     Spoofer     ║                         │    [36.1] Gasper            ║    
    ╠═════════════════╣                         │    [37.1] Chromatic         ║    
    ║     Cracks      ║                         │    [38.1] Akira Client      ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║  [19] <= Prev Page      │        [21] Next Page =>    ║    
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
    if chon == '20.1':
        webbrowser.open_new("https://www.mediafire.com/file/t9mrmlmgxb4nsgv/Cucklord_Reborn.zip/file")
    if chon == '21.1':
        webbrowser.open_new("https://www.mediafire.com/file/ymd1hc1j7nb7qj1/Elixe.zip/file")
    if chon == '22.1':
        webbrowser.open_new("https://www.mediafire.com/file/x2epdf2ai8xlr15/Iridium_Ghost.zip/file")
    if chon == '23.1':
        webbrowser.open_new("https://www.mediafire.com/file/yzbmndznry00jrk/Axenta_V2.zip/file")
    if chon == '24.1':
        webbrowser.open_new("https://www.mediafire.com/file/iiapzj07j8e1z6a/Smok.zip/file")
    if chon == '25.1':
        webbrowser.open_new("https://www.mediafire.com/file/vtp18l7ygr7t0ff/Itami.zip/file")
    if chon == '26.1':
        webbrowser.open_new("https://www.mediafire.com/file/seaymmk3w14rxt7/Kriso_b1.zip/file")
    if chon == '27.1':
        webbrowser.open_new("https://www.mediafire.com/file/0avv5njdwx29omn/Mind_Client.zip/file")
    if chon == '28.1':
        webbrowser.open_new("https://www.mediafire.com/file/f8ka0ch9m07680b/Mye_Ghost.zip/file")
    if chon == '29.1':
        webbrowser.open_new("https://www.mediafire.com/file/t0cv0fs3mw3vdvq/Nyctum.zip")
    if chon == '30.1':
        webbrowser.open_new("https://www.mediafire.com/file/v0jvcvvc1kbhj2t/Shiba.zip/file")
    if chon == '31.1':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1049374498442461194/1081999382569820180/Uboa_v2.jar")
    if chon == '32.1':
        webbrowser.open_new("https://workupload.com/file/JjFABQCJspJ")
    if chon == '33.1':
        webbrowser.open_new("https://www.mediafire.com/file/fny7xzarjh8n415/Whiteout_V3.zip/file")
    if chon == '34.1':
        webbrowser.open_new("https://www.mediafire.com/file/wgyzc22pxc83ryf/Emo.zip/file")
    if chon == '35.1':
        webbrowser.open_new("https://www.mediafire.com/file/98j1hfy0pkjmk7b/Epic.zip/file")
    if chon == '36.1':
        webbrowser.open_new("https://www.mediafire.com/file/zjgx3rat06duvm6/Gasper.zip/file")
    if chon == '37.1':
        webbrowser.open_new("https://www.mediafire.com/file/vyxlihy85lsx4mu/Chromatic.zip/file")
    if chon == '38.1':
        webbrowser.open_new("https://www.mediafire.com/file/9uujyo7z1gl0rms/Akira.zip/file")
    if chon == '19':
        print("                                              \033[1;39mLoading Ghost Page 1..")
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/ghost_page_1.py').text)
    if chon == '21':
        print("                                              \033[1;39mLoading Ghost Page 3..")
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/ghost_page_3.py').text)
    else:
        print("\033[F\033[K", end="", flush=True)
