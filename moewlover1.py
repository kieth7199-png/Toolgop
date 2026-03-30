import os
import sys
import time
import json
import requests
import platform
import hashlib
import subprocess
from datetime import datetime, timedelta
from time import sleep, strftime

# ==========================================================
# [ TỰ ĐỘNG CÀI ĐẶT THƯ VIỆN THIẾU ]
# ==========================================================
def install_dependencies():
    try:
        from pystyle import Colors, Colorate, Write
    except ImportError:
        print("\033[1;36m[*] Dang cai dat thu vien he thong (pystyle)...")
        os.system("pip install pystyle colorama requests")
        print("\033[1;32m[✓] Cai dat hoan tat! Dang khoi dong lai...")
        sleep(2)
        os.execl(sys.executable, sys.executable, *sys.argv)

install_dependencies()
from pystyle import Colors, Colorate

# Bang mau ANSI
xnhac = "\033[1;36m"
xduong = "\033[1;34m"
trang = "\033[1;37m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    banner_text = """
 ███╗   ███╗ ██████╗ ███████╗ ██╗    ██╗    ██╗      ██████╗ ██╗   ██╗ ███████╗ ██████╗ 
 ████╗ ████║██╔═══██╗██╔════╝ ██║    ██║    ██║     ██╔═══██╗██║   ██║ ██╔════╝ ██╔══██╗
 ██╔████╔██║██║   ██║█████╗   ██║ █╗ ██║    ██║     ██║   ██║██║   ██║ █████╗   ██████╔╝
 ██║╚██╔╝██║██║   ██║██╔══╝   ██║███╗██║    ██║     ██║   ██║╚██╗ ██╔╝ ██╔══╝   ██╔══██╗
 ██║ ╚═╝ ██║╚██████╔╝███████╗ ╚███╔███╔╝    ███████╗╚██████╔╝ ╚████╔╝  ███████╗ ██║  ██║
 ╚═╝     ╚═╝ ╚═════╝ ╚══════╝  ╚══╝╚══╝     ╚══════╝ ╚═════╝   ╚═══╝   ╚══════╝ ╚═╝  ╚═╝
------------------------------------------------------------
Tool By: Moew Lover | Tiktok: moewlovertool
------------------------------------------------------------"""
    print(Colorate.Diagonal(Colors.cyan_to_blue, banner_text))

def v_dong(text):
    return Colorate.Diagonal(Colors.cyan_to_blue, text)

clear()
banner()

# --- DANH MUC TOOL ---
sections = [
    ("Tool Trao Doi Sub", ["[1.1] TDS TIKTOK V1", "[1.2] TDS TIKTOK V2", "[1.3] TDS TIKTOK NOW", "[1.4] TDS INSTAGRAM", "[1.5] DOI MK TDS"]),
    ("Tool Spam Sms", ["[2.1] SPAM SMS V1", "[2.2] SPAM SMS V2"]),
    ("Tool Dao Mail", ["[3.1] DAO MAIL", "[3.2] DAO FULL MAIL", "[3.3] CHECK LIVE/DIE", "[3.4] CHECK VALID", "[3.5] REG ACC GARENA"]),
    ("Tool Dao & Check Proxies", ["[4.1] CHECK PXY V1", "[4.2] CHECK PXY V2", "[4.3] CHECK PXY V3 VIP", "[4.4] DAO PROXY V1", "[4.5] DAO PROXY V2", "[4.6] DAO PROXY V3", "[4.7] DAO PROXY V4", "[4.8] DAO PROXY V5 VIP"]),
    ("Tool Encode & Dec", ["[5.1] DEC HYPERION", "[5.2] DEC KRAMER", "[5.3] DUMP MARSHAL", "[5.4] CONVERT MARSHAL", "[5.5] ENCODE MZB", "[5.6] ENCODE EMOJI", "[5.7] ENCODE EJULY"]),
    ("Tool Auto Golike", ["[6.1] AUTO TIKTOK", "[6.2] AUTO INSTAGRAM", "[6.3] AUTO TWITTER"]),
    ("Tool Idol Khac", ["[7.1] VLONG ZZ", "[7.2] TRINH HUONG", "[7.3] MEOWMEOW", "[7.4] HDT-TOOL", "[7.5] LKZ TOOL", "[7.6] JIRAY TOOL", "[7.7] BETA TOOL"]),
    ("Tool Tien Ich", ["[8.1] DOSS WEB VIP", "[8.2] REG PAGE PRO5", "[8.3] RUT GON LINK", "[8.4] PHAN HOI LINK", "[8.5] LOC LINK FILE"]),
    ("Tool Update & Exit", ["[9.1] MAY TINH", "[9.2] BAN MAY BAY", "[00] THOAT TOOL"])
]

for title, options in sections:
    print(v_dong(f"\n╔{'═' * 25}╗"))
    print(v_dong(f"║ {title.center(23)} ║"))
    print(v_dong(f"╚{'═' * 25}╝"))
    for i in range(0, len(options), 2):
        line = f"{xnhac}{options[i]}"
        if i + 1 < len(options):
            line = line.ljust(35) + f"{xnhac}{options[i+1]}"
        print(line)

print(v_dong("\n" + "-" * 60))
chon = input(f'{xnhac}[{trang}x{xnhac}] {trang}Nhap Lua Chon {xnhac}➤ {vang}').strip()

# --- LOGIC THUC THI ---
def run_tool(url):
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            exec(res.text)
        else:
            print(f"{do}[!] Loi: Khong the tai file ({res.status_code})")
    except Exception as e:
        print(f"{do}[!] Loi: {e}")

menu = {
    '00': 'https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml',
    '1.1': 'https://raw.githubusercontent.com/Khanh23047/TDS-TIKTOK-V1/main/tool.py',
    '1.2': 'https://raw.githubusercontent.com/Khanh23047/Tdstikv2/main/00.py',
    '1.3': 'https://raw.githubusercontent.com/Khanh23047/Tik-tiknow/main/1.py',
    '1.4': 'https://raw.githubusercontent.com/Khanh23047/TDS-IG/main/3.py',
    '1.5': 'https://raw.githubusercontent.com/Khanh23047/Mktds/main/4.py',
    '2.1': 'https://raw.githubusercontent.com/Khanh23047/Spamsmsv1/main/sms.py',
    '2.2': 'https://raw.githubusercontent.com/Khanh23047/Spamsmsv2/main/smsv2.py',
    '3.1': 'https://raw.githubusercontent.com/Khanh23047/Daomail/main/8.py',
    '3.2': 'https://raw.githubusercontent.com/Khanh23047/Full-mail/main/vietcode_toolmeow.py',
    '3.3': 'https://raw.githubusercontent.com/Khanh23047/Checklivedie/main/p.py',
    '3.4': 'https://raw.githubusercontent.com/Khanh23047/checkvali/main/10.py',
    '3.5': 'https://raw.githubusercontent.com/Khanh23047/Reggrn/main/Reggrn',
    '4.1': 'https://raw.githubusercontent.com/Khanh23047/Checklivedieproxy/main/p.py',
    '4.2': 'https://raw.githubusercontent.com/Khanh23047/Check-live-die-v2/main/q.py',
    '4.3': 'https://raw.githubusercontent.com/Khanh23047/Checklivediev2/main/p.py',
    '4.4': 'https://raw.githubusercontent.com/Khanh23047/Daoprxv1/main/daoprxv1.py',
    '4.5': 'https://raw.githubusercontent.com/Khanh23047/Daoprxv2/main/p.py',
    '4.6': 'https://raw.githubusercontent.com/Khanh23047/Daoproxyv3/main/p.py',
    '4.7': 'https://raw.githubusercontent.com/Khanh23047/Daoproxyv4/main/p.py',
    '4.8': 'https://raw.githubusercontent.com/Khanh23047/Daoproxyv4vip/main/p.py',
    '5.1': 'https://raw.githubusercontent.com/KhanhNguyen9872/hyperion_deobfuscate/main/hyperion_deobf.py',
    '5.2': 'https://raw.githubusercontent.com/KhanhNguyen9872/kramer-specter_deobf/main/kramer-specter-deobf.py',
    '5.3': 'https://raw.githubusercontent.com/KhanhNguyen9872/dump_marshal_py/main/dump_marshal.py',
    '5.4': 'https://raw.githubusercontent.com/KhanhNguyen9872/Convert_Marshal-PYC/main/cv_marshal_pyc.py',
    '5.5': 'https://raw.githubusercontent.com/Khanh23047/Encode-MZB/main/en.py',
    '5.6': 'https://raw.githubusercontent.com/Khanh23047/Encode-Emoji-/main/p.py',
    '5.7': 'https://raw.githubusercontent.com/Khanh23047/Encode-ejuly-DUYKHANH/main/encode.py',
    '6.1': 'https://raw.githubusercontent.com/Khanh23047/Golike/main/golike.py',
    '6.2': 'https://raw.githubusercontent.com/Khanh23047/Golike-ig/main/p.py',
    '6.3': 'https://raw.githubusercontent.com/Khanh23047/Golike-Twitter-/main/p.py',
    '7.1': 'https://raw.githubusercontent.com/Khanh23047/Tool-vlong/main/p.py',
    '7.2': 'https://raw.githubusercontent.com/Khanh23047/Tool-trinh-huong/main/huong.py',
    '7.3': 'https://raw.githubusercontent.com/Khanh23047/Full-mail/main/vietcode_toolmeow.py',
    '7.4': 'https://raw.githubusercontent.com/Khanh23047/Tool-hdt/main/p.py',
    '7.5': 'https://raw.githubusercontent.com/Khanh23047/Tool-lkz/main/p.py',
    '7.6': 'https://raw.githubusercontent.com/Khanh23047/Tool-jray/main/haha.py',
    '7.7': 'https://raw.githubusercontent.com/Khanh23047/Beta-tool/main/beta.py',
    '8.1': 'https://raw.githubusercontent.com/Khanh23047/DOSS-WEB/main/dos.py',
    '8.2': 'https://raw.githubusercontent.com/Khanh23047/Reg-pro5-vip/main/reg.py',
    '8.3': 'https://raw.githubusercontent.com/Khanh23047/Rutgonlink/main/10.py',
    '8.4': 'https://raw.githubusercontent.com/Khanh23047/Phanhoilink/main/10.py',
    '8.5': 'https://raw.githubusercontent.com/Khanh23047/L-c-Link-T-File/main/10.py',
    '9.1': 'https://raw.githubusercontent.com/Khanh23047/May-tinh/main/0.py',
    '9.2': 'https://raw.githubusercontent.com/Khanh23047/May-bay/main/1.py'
}

if chon in menu:
    run_tool(menu[chon])
else:
    print(f"{do}[!] Lua chon khong ton tai!")