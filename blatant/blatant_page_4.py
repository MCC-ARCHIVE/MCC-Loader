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
    ║      Ghost      ║    [00] General         │    [58.2] North Client      ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [59.2] Felix Client      ║    
    ║—————Blatant—————║    [02] Blatant Clients │    [60.2] Bloody Client     ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [61.2] Prestige Client   ║    
    ║     Anarchy     ║    [04] Autoclicker     │    [62.2] Thunderhack Deluxe║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [63.2] Cyrus Client      ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [64.2] Atani Client      ║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [65.2] ClientWare        ║    
    ║       CS2       ║    [08] MC plugins      │    [66.2] Sigma             ║    
    ╠═════════════════╣    [09] Spoofer         │    [67.2] Astomero          ║    
    ║     Valorant    ║    [10] Cracks          │    [68.2] Dark Client       ║    
    ╠═════════════════╣    [11] Others          │    [69.2] RektSky B5        ║    
    ║      Roblox     ║                         │    [70.2] FDP Client        ║    
    ╠═════════════════╣                         │    [71.2] Icarus X          ║    
    ║     Plugins     ║                         │    [72.2] Francium + Rebor  ║    
    ╠═════════════════╣                         │    [73.2] Asteria           ║    
    ║     Spoofer     ║                         │    [74.2] Lime Reborn       ║    
    ╠═════════════════╣                         │    [75.2] FDP Laoshul       ║    
    ║     Cracks      ║                         │    [76.2] Atani             ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║  [22] Prev Page <=      │        [24] Next Page =>    ║   
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
    if chon == '22':
        print("                                              \033[1;39mLoading Blatant Page 3..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/1337hertz/mcc/main/blatant/blatant_page_3.py').text)
    if chon == '24':
        print("                                              \033[1;39mLoading Blatant Page 5..")
        os.system('cls') 
        exec(requests.get('https://raw.githubusercontent.com/1337hertz/mcc/main/blatant/blatant_page_5.py').text)

    if chon == '58.2':
        webbrowser.open_new("https://workupload.com/file/jMUrDuxpaaH")
    if chon == '59.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1129699151018459240/1153979707788890112/Felix21_1.jar")
    if chon == '60.2':
        webbrowser.open_new("https://github.com/WalmartSolutions/BloodyClient-0.4.4")
    if chon == '61.2':
        webbrowser.open_new("https://www.mediafire.com/file/78jrpo6eebgbif4/Prestigee.zip/file")
    if chon == '62.2':
        webbrowser.open_new("https://github.com/WalmartSolutions/ThunderHack-Deluxe")
    if chon == '63.2':
        webbrowser.open_new("https://workupload.com/file/KWLqZqNcEfB")
    if chon == '64.2':
        webbrowser.open_new("https://workupload.com/file/6sbhyuvFpcD")
    if chon == '65.2':
        webbrowser.open_new("https://www.mediafire.com/file/w0bsrpe00jtvkc3/ClientWare_b1.0.zip/file")
    if chon == '66.2':
        webbrowser.open_new("https://sites.google.com/view/nezha-anticheat/sigma-archive")
    if chon == '67.2':
        webbrowser.open_new("https://workupload.com/file/ux2JBKK8dU5")
    if chon == '68.2':
        webbrowser.open_new("https://workupload.com/file/szFZJUmjGmL")
    if chon == '69.2':
        webbrowser.open_new("https://www.mediafire.com/file/xkm16qm7q5x94g8/rektsky.rar/file")
    if chon == '70.2':
        webbrowser.open_new("https://fdpinfo.github.io/download")
    if chon == '71.2':
        webbrowser.open_new("https://workupload.com/file/deQbL32TQR4")
    if chon == '72.2':
        webbrowser.open_new("https://www.mediafire.com/file/jxtx2qvjtg5ya8n/Negr.zip/file")
    if chon == '73.2':
        webbrowser.open_new("https://github.com/WalmartSolutions/Asteria.rip")
    if chon == '74.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1129999297857990660/1169887601445052436/Lime-reborn.zip?ex=655709bb&is=654494bb&hm=d3d786081e19bc5fd3b50eec0e77218a97c50457db68bdb15a7f97adc211b6c1&")
    if chon == '75.2':
        webbrowser.open_new("https://github.com/laoshuikaixue/FDPClient")
    if chon == '76.2':
        webbrowser.open_new("https://workupload.com/file/c823T2LaFTv")
    else:
        print("\033[F\033[K", end="", flush=True)