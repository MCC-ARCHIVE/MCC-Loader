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
    ║——————Ghost——————║    [00] General         │    [1.1] Vape cracked       ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [2.1] Blossom            ║    
    ║     Blatant     ║    [02] Blatant Clients │    [3.1] Dream Client       ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [4.1] Slapp              ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [5.1] Whiteout           ║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [6.1] Eternal Client     ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [7.1] Koid               ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [8.1] Zoomin             ║    
    ║       CS2       ║    [08] MC plugins      │    [9.1] Luvsy Client       ║    
    ╠═════════════════╣    [09] Spoofer         │    [10.1] Dope Client [V1]  ║    
    ║     Valorant    ║    [10] Cracks          │    [11.1] Checkz            ║    
    ╠═════════════════╣    [11] Others          │    [12.1] Neo Reach         ║    
    ║      Roblox     ║                         │    [13.1] Obscure Client    ║    
    ╠═════════════════╣                         │    [14.1] Lithium Lite      ║    
    ║     Plugins     ║                         │    [15.1] Raven [B+ -> B4]  ║    
    ╠═════════════════╣                         │    [16.1] Fractal Injector  ║    
    ║     Spoofer     ║                         │    [17.1] WTap V3           ║    
    ╠═════════════════╣                         │    [18.1] ESP Client        ║    
    ║     Cracks      ║                         │    [19.1] Cucklord          ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║                                  [20] Next Page =>    ║    
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
    if chon == '1.1':
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Vape').text)
    if chon == '2.1':
        webbrowser.open_new("https://www.mediafire.com/file/6v9xzhuv1ydezmp/Blossom.zip/file")
    if chon == '3.1':
        webbrowser.open_new("https://www.mediafire.com/file/ufktd90e503p7cb/drim.zip/file")
    if chon == '4.1':
        webbrowser.open_new("https://www.mediafire.com/file/asd0skn12pgur93/Slap.zip/file")
    if chon == '5.1':
        webbrowser.open_new("https://www.mediafire.com/file/890qfvw73k97qll/Whiteout_V2.3.zip/file")
    if chon == '6.1':
        webbrowser.open_new("https://www.mediafire.com/file/p43x2u7j2428y4c/eternal_internal.dll/file")
    if chon == '7.1':
        webbrowser.open_new("https://cdn.discordapp.com/attachments/1129999297857990660/1169617449176547338/koid.exe?ex=65560e22&is=65439922&hm=6d782d1e13b05c9b09e6f038e0faf5aa28264a36fe262b1699f2054ba603b8fd&")
    if chon == '8.1':
        webbrowser.open_new("https://www.mediafire.com/file/tnqrduaaqyu9fn8/Zoomin.zip/file")
    if chon == '9.1':
        webbrowser.open_new("https://www.mediafire.com/file/hrls1h4mp516fy7/Luvsy_Ghost_v1.0.zip/file")
    if chon == '10.1':
        webbrowser.open_new("https://www.mediafire.com/file/22evfi1yvyaormy/Dope.zip/file")
    if chon == '11.1':
        webbrowser.open_new("https://www.mediafire.com/file/gh4y87z2ybgvc9x/1.8-OptiFine_HD_U_H2.zip/file")
    if chon == '12.1':
        webbrowser.open_new("https://www.mediafire.com/file/bsw9lwpbne9ev8w/Neo_Reach.zip/file")
    if chon == '13.1':
        webbrowser.open_new("https://www.mediafire.com/file/idmpo6rmc56b826/Obscure.zip/file")
    if chon == '14.1':
        webbrowser.open_new("https://www.mediafire.com/file/njdn9o73gehyxxb/Lithium_Lite.zip/file")
    if chon == '15.1':
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Raven').text)
    if chon == '16.1':
        webbrowser.open_new("https://www.mediafire.com/file/9bw1ggpe6lpitpe/Fractal.zip/file")
    if chon == '17.1':
        webbrowser.open_new("https://www.mediafire.com/file/29naq1ybrud7f5k/WTap_v3.zip/file")
    if chon == '20':
        print("                                              \033[1;39mLoading Ghost Page 2..")
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/ghost_page_2').text)
    else:
        print("\033[F\033[K", end="", flush=True)