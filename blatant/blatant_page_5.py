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
    ║      Ghost      ║    [00] General         │    [77.2] Helios            ║    
    ╠═════════════════╣    [01] Ghost Clients   │    [78.2] Pog               ║    
    ║—————Blatant—————║    [02] Blatant Clients │    [79.2] AsyncWare         ║    
    ╠═════════════════╣    [03] Anarchy Clients │    [80.2] Summer Reborn [v3]║    
    ║     Anarchy     ║    [04] Autoclicker     │    [81.2] Satiete           ║    
    ╠═════════════════╣    [05] CS2 Cheats      │    [82.2] Tifality          ║    
    ║   AutoClicker   ║    [06] Valorant Cheats │    [83.2] Air Client [Risky]║    
    ╠═════════════════╣    [07] Roblox Cheats   │    [84.2] SalHack           ║    
    ║       CS2       ║    [08] MC plugins      │    [85.2] Boze              ║    
    ╠═════════════════╣    [09] Spoofer         │    [86.2] Flow Client       ║    
    ║     Valorant    ║    [10] Cracks          │    [87.2] Radium            ║    
    ╠═════════════════╣    [11] Others          │    [88.2] None Client       ║    
    ║      Roblox     ║                         │    [89.2] Ketamine          ║    
    ╠═════════════════╣                         │    [90.2] Koks              ║    
    ║     Plugins     ║                         │    [91.2] Breeze            ║    
    ╠═════════════════╣                         │    [92.2] Myau              ║    
    ║     Spoofer     ║                         │    [93.2] Skligga           ║    
    ╠═════════════════╣                         │    [94.2] Aoba              ║    
    ║     Cracks      ║                         │                             ║    
    ╠═════════════════╣                         │                             ║    
    ║     Others      ║  [23] Prev Page <=      │                             ║   
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
    if chon == '23':
        print("                                              \033[1;39mLoading Blatant Page 4..")
        os.system("cls")
        exec(requests.get('https://raw.githubusercontent.com/MCC-ARCHIVE/MCC-Loader/main/blatant/blatant_page_4.py').text)

    if chon == '77.2':
        webbrowser.open_new("https://www.mediafire.com/file/4419kb1fnbbszwd/Helios.zip/file")
    if chon == '78.2':
        webbrowser.open_new("https://workupload.com/file/DFxJMNXqTDA")
    if chon == '79.2':
        webbrowser.open_new("https://www.mediafire.com/file/5c6ico912uq3wdn/Asyncware.zip/file")
    if chon == '80.2':
        webbrowser.open_new("https://www.mediafire.com/file/s4pubyxcv167mct/Summer+Reborn+v3.zip/file")
    if chon == '81.2':
        webbrowser.open_new("https://www.mediafire.com/file/382s01u180l8pti/Satiate.zip/file")
    if chon == '82.2':
        webbrowser.open_new("https://workupload.com/file/BeHqpWqNMVv")
    if chon == '83.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1160274406128484403/1181187679648489482/airclient-1.2.jar?ex=658025c0&is=656db0c0&hm=d34ecc28179ffc6787fcf8f42a180806c9ef11342503d7ce38289675b8630656&")
    if chon == '84.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1187569667779342367/1187569705507115109/SalHack.zip?ex=65975d79&is=6584e879&hm=861c57691bc720a20db3d3b2d83e4e107f35eb6768a3d5c517fdd2b56bcfa726&")
    if chon == '85.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1187494939085520916/1187494981397655592/bozecrack.zip?ex=659717e2&is=6584a2e2&hm=bd0c151d9c5e2d0cf41151523e8c7e4d6030e68d490a9d08babaf991fca5365c&")
    if chon == '86.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1187571000158732369/1187615112056557588/Flow-1.1.zip?ex=659787c3&is=658512c3&hm=1744f94d2fc0d26538bb3698677d093104633ced7f5a03f73d8e00a49eff4913&")
    if chon == '87.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1187571000158732369/1187615111557431336/Radium.zip?ex=659787c3&is=658512c3&hm=0bfc8ca74b7418cf34b058c0e1c3fe1fa1e7b6a822914d5410c33b7a4f452a21&")
    if chon == '88.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1187571000158732369/1187615112555671632/None_B2.1.rar?ex=659787c3&is=658512c3&hm=786957f64ce2b85ec7f6a88fe74d4cc0b93793f6ef89196a898340c3ef9100f1&")
    if chon == '89.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1187571000158732369/1187615113704910908/Ketamine.zip?ex=659787c3&is=658512c3&hm=735a03feae76f7f9ad25604cbf806315129e88b3f6161346cd7f11718fa9eee8&")
    if chon == '90.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1187571000158732369/1187615113025441832/Koks.zip?ex=659787c3&is=658512c3&hm=ace12e4473400e9bc4529344cd453abcbcbb70a86fe6e67423acd3fc756da779&")
    if chon == '91.2':
        webbrowser.open_new(
            "https://cdn.discordapp.com/attachments/1133744936160862279/1189787677818626069/breeze_crack.jar?ex=659f6f1f&is=658cfa1f&hm=3c47ed31eedefdc92b576ca89e46f3979359c3079d1659e6ceed24c1535e42ae&")
    if chon == '92.2':
        webbrowser.open_new("https://drive.proton.me/urls/PB9PKP8C8W#0ol6F9HyRGDL")
    if chon == '93.2':
        webbrowser.open_new("https://www.mediafire.com/file/hs8ejb3kagvbvk8/Skligga_%2528FABRIC%2529.zip/file")
    if chon == '94.2':
        webbrowser.open_new("https://www.mediafire.com/file/smhau035ax85lsc/Aoba.rar/file")
    else:
        print("\033[F\033[K", end="", flush=True)