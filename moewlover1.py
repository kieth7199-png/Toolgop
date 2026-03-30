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
        print("\033[1;36m[*] Đang cài đặt thư viện hệ thống (pystyle)...")
        os.system("pip install pystyle colorama requests")
        print("\033[1;32m[✓] Cài đặt hoàn tất! Đang khởi động lại...")
        sleep(2)
        # Khởi động lại script sau khi cài xong
        os.execl(sys.executable, sys.executable, *sys.argv)

install_dependencies()
from pystyle import Colors, Colorate

# Bảng màu ANSI cơ bản
xnhac = "\033[1;36m"
xduong = "\033[1;34m"
trang = "\033[1;37m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
end = '\033[0m'

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    banner_text = f"""
 ███╗   ███╗ ██████╗ ███████╗ ██╗    ██╗    ██╗      ██████╗ ██╗   ██╗ ███████╗ ██████╗ 
 ████╗ ████║██╔═══██╗██╔════╝ ██║    ██║    ██║     ██╔═══██╗██║   ██║ ██╔════╝ ██╔══██╗
 ██╔████╔██║██║   ██║█████╗   ██║ █╗ ██║    ██║     ██║   ██║██║   ██║ █████╗   ██████╔╝
 ██║╚██╔╝██║██║   ██║██╔══╝   ██║███╗██║    ██║     ██║   ██║╚██╗ ██╔╝ ██╔══╝   ██╔══██╗
 ██║ ╚═╝ ██║╚██████╔╝███████╗ ╚███╔███╔╝    ███████╗╚██████╔╝ ╚████╔╝  ███████╗ ██║  ██║
 ╚═╝     ╚═╝ ╚═════╝ ╚══════╝  ╚══╝╚══╝     ╚══════╝ ╚═════╝   ╚═══╝   ╚══════╝ ╚═╝  ╚═╝
────────────────────────────────────────────────────────────
Tool By: Moew Lover | Tiktok: moewlovertool
────────────────────────────────────────────────────────────"""
    print(Colorate.Diagonal(Colors.cyan_to_blue, banner_text))

def v_dong(text):
    return Colorate.Diagonal(Colors.cyan_to_blue, text)

# --- KHỞI CHẠY ---
clear()
banner()

# --- DANH MỤC TOOL (RÚT GỌN CHO GIAO DIỆN SẠCH) ---
print(v_dong("╔═════════════════════╗"))
print(v_dong("║  Tool Trao Đổi Sub  ║"))
print(v_dong("╚═════════════════════╝"))
print(f"{xnhac}[1.1] {luc}TDS TIKTOK V1      {xnhac}[1.2] {luc}TDS TIKTOK V2")
print(f"{xnhac}[1.3] {luc}TDS TIKTOK NOW    {xnhac}[1.4] {luc}TDS INSTAGRAM")
print(f"{xnhac}[1.5] {luc}ĐỔI MK TĐS")

print(v_dong("\n╔═════════════════════╗"))
print(v_dong("║  Tool Spam Sms      ║"))
print(v_dong("╚═════════════════════╝"))
print(f"{xnhac}[2.1] {luc}SPAM SMS V1       {xnhac}[2.2] {luc}SPAM SMS V2")

print(v_dong("\n╔═════════════════════╗"))
print(v_dong("║  Tool Đào Mail      ║"))
print(v_dong("╚═════════════════════╝"))
print(f"{xnhac}[3.1] {luc}ĐÀO MAIL          {xnhac}[3.2] {luc}ĐÀO FULL MAIL")
print(f"{xnhac}[3.3] {luc}CHECK LIVE/DIE    {xnhac}[3.4] {luc}CHECK VALID")
print(f"{xnhac}[3.5] {luc}REG ACC GARENA")

print(v_dong("\n╔═══════════════════════════╗"))
print(v_dong("║ Tool Đào & Check Proxies  ║"))
print(v_dong("╚═══════════════════════════╝"))
print(f"{xnhac}[4.1] {luc}CHECK PXY V1      {xnhac}[4.2] {luc}CHECK PXY V2")
print(f"{xnhac}[4.3] {luc}CHECK PXY V3 VIP  {xnhac}[4.4] {luc}ĐÀO PROXY V1")
print(f"{xnhac}[4.5] {luc}ĐÀO PROXY V2      {xnhac}[4.6] {luc}ĐÀO PROXY V3")
print(f"{xnhac}[4.7] {luc}ĐÀO PROXY V4      {xnhac}[4.8] {luc}ĐÀO PROXY V5 VIP")

print(v_dong("\n╔═══════════════════════════╗"))
print(v_dong("║ Tool Encode & Dec         ║"))
print(v_dong("╚═══════════════════════════╝"))
print(f"{xnhac}[5.1] {luc}DEC HYPERION      {xnhac}[5.2] {luc}DEC KRAMER")
print(f"{xnhac}[5.3] {luc}DUMP MARSHAL      {xnhac}[5.4] {luc}CONVERT MARSHAL")
print(f"{xnhac}[5.5] {luc}ENCODE MZB        {xnhac}[5.6] {luc}ENCODE EMOJI")
print(f"{xnhac}[5.7] {luc}ENCODE EJULY")

print(v_dong("\n╔═══════════════════════════╗"))
print(v_dong("║ Tool Auto Golike          ║"))
print(v_dong("╚═══════════════════════════╝"))
print(f"{xnhac}[6.1] {luc}AUTO TIKTOK       {xnhac}[6.2] {luc}AUTO INSTAGRAM")
print(f"{xnhac}[6.3] {luc}AUTO TWITTER")

print(v_dong("\n╔═══════════════════════════╗"))
print(v_dong("║ Tool Idol Khác            ║"))
print(v_dong("╚═══════════════════════════╝"))
print(f"{xnhac}[7.1] {luc}VLONG ZZ          {xnhac}[7.2] {luc}TRỊNH HƯỚNG")
print(f"{xnhac}[7.3] {luc}MEOWMEOW          {xnhac}[7.4] {luc}HDT-TOOL")
print(f"{xnhac}[7.5] {luc}LKZ TOOL          {xnhac}[7.6] {luc}JIRAY TOOL")
print(f"{xnhac}[7.7] {luc}BETA TOOL")

print(v_dong("\n╔═════════════════════╗"))
print(v_dong("║ Tool Tiện Ích       ║"))
print(v_dong("╚═════════════════════╝"))
print(f"{xnhac}[8.1] {luc}DOSS WEB VIP      {xnhac}[8.2] {luc}REG PAGE PRO5")
print(f"{xnhac}[8.3] {luc}RÚT GỌN LINK      {xnhac}[8.4] {luc}PHẢN HỒI LINK")
print(f"{xnhac}[8.5] {luc}LỌC LINK FILE")

print(v_dong("\n╔═════════════════════╗"))
print(v_dong("║ Tool Update & Exit  ║"))
print(v_dong("╚═════════════════════╝"))
print(f"{xnhac}[9.1] {luc}MÁY TÍNH          {xnhac}[9.2] {luc}BẮN MÁY BAY")
print(f"{xnhac}[00 ] {do}THOÁT TOOL")

print(v_dong("\n────────────────────────────────────────────────────────────"))
chon = str(input(f'{xnhac}[{trang}×{xnhac}] {trang}Nhập Lựa Chọn {xnhac}➤ {vang}')).strip()

# --- LOGIC THỰC THI (ĐÃ FIX LỖI REQUEST) ---
def run_tool(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            exec(response.text)
        else:
            print(f"{do}[!] Lỗi: Không thể lấy file từ GitHub (Code {response.status_code})")
    except Exception as e:
        print(f"{do}[!] Lỗi thực thi: {e}")

if chon == '00': run_tool('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml')
elif chon == '1.1': run_tool('https://raw.githubusercontent.com/Khanh23047/TDS-TIKTOK-V1/main/tool.py')
elif chon == '1.2': run_tool('https://raw.githubusercontent.com/Khanh23047/Tdstikv2/main/00.py')
elif chon == '1.3': run_tool('https://raw.githubusercontent.com/Khanh23047/Tik-tiknow/main/1.py')
elif chon == '1.4': run_tool('https://raw.githubusercontent.com/Khanh23047/TDS-IG/main/3.py')
elif chon == '1.5': run_tool('https://raw.githubusercontent.com/Khanh23047/Mktds/main/4.py')
elif chon == '2.1': run_tool('https://raw.githubusercontent.com/Khanh23047/Spamsmsv1/main/sms.py')
elif chon == '2.2': run_tool('https://raw.githubusercontent.com/Khanh23047/Spamsmsv2/main/smsv2.py')
elif chon == '3.1': run_tool('https://raw.githubusercontent.com/Khanh23047/Daomail/main/8.py')
elif chon == '3.2': run_tool('https://raw.githubusercontent.com/Khanh23047/Full-mail/main/vietcode_toolmeow.py')
elif chon == '3.3': run_tool('https://raw.githubusercontent.com/Khanh23047/Checklivedie/main/p.py')
elif chon == '3.4': run_tool('https://raw.githubusercontent.com/Khanh23047/checkvali/main/10.py')
elif chon == '3.5': run_tool('https://raw.githubusercontent.com/Khanh23047/Reggrn/main/Reggrn')
elif chon == '4.1': run_tool('https://raw.githubusercontent.com/Khanh23047/Checklivedieproxy/main/p.py')
elif chon == '4.2': run_tool('https://raw.githubusercontent.com/Khanh23047/Check-live-die-v2/main/q.py')
elif chon == '4.3': run_tool('https://raw.githubusercontent.com/Khanh23047/Checklivediev2/main/p.py')
elif chon == '4.4': run_tool('https://raw.githubusercontent.com/Khanh23047/Daoprxv1/main/daoprxv1.py')
elif chon == '4.5': run_tool('https://raw.githubusercontent.com/Khanh23047/Daoprxv2/main/p.py')
elif chon == '4.6': run_tool('https://raw.githubusercontent.com/Khanh23047/Daoproxyv3/main/p.py')
elif chon == '4.7': run_tool('https://raw.githubusercontent.com/Khanh23047/Daoproxyv4/main/p.py')
elif chon == '4.8': run_tool('https://raw.githubusercontent.com/Khanh23047/Daoproxyv4vip/main/p.py')
elif chon == '5.1': run_tool('https://raw.githubusercontent.com/KhanhNguyen9872/hyperion_deobfuscate/main/hyperion_deobf.py')
elif chon == '5.2': run_tool('https://raw.githubusercontent.com/KhanhNguyen9872/kramer-specter_deobf/main/kramer-specter-deobf.py')
elif chon == '5.3': run_tool('https://raw.githubusercontent.com/KhanhNguyen9872/dump_marshal_py/main/dump_marshal.py')
elif chon == '5.4': run_tool('https://raw.githubusercontent.com/KhanhNguyen9872/Convert_Marshal-PYC/main/cv_marshal_pyc.py')
elif chon == '5.5': run_tool('https://raw.githubusercontent.com/Khanh23047/Encode-MZB/main/en.py')
elif chon == '5.6': run_tool('https://raw.githubusercontent.com/Khanh23047/Encode-Emoji-/main/p.py')
elif chon == '5.7': run_tool('https://raw.githubusercontent.com/Khanh23047/Encode-ejuly-DUYKHANH/main/encode.py')
elif chon == '6.1': run_tool('https://raw.githubusercontent.com/Khanh23047/Golike/main/golike.py')
elif chon == '6.2': run_tool('https://raw.githubusercontent.com/Khanh23047/Golike-ig/main/p.py')
elif chon == '6.3': run_tool('https://raw.githubusercontent.com/Khanh23047/Golike-Twitter-/main/p.py')
elif chon == '7.1': run_tool('https://raw.githubusercontent.com/Khanh23047/Tool-vlong/main/p.py')
elif chon == '7.2': run_tool('https://raw.githubusercontent.com/Khanh23047/Tool-trinh-huong/main/huong.py')
elif chon == '7.3': run_tool('https://raw.githubusercontent.com/Khanh23047/Full-mail/main/vietcode_toolmeow.py')
elif chon == '7.4': run_tool('https://raw.githubusercontent.com/Khanh23047/Tool-hdt/main/p.py')
elif chon == '7.5': run_tool('https://raw.githubusercontent.com/Khanh23047/Tool-lkz/main/p.py')
elif chon == '7.6': run_tool('https://raw.githubusercontent.com/Khanh23047/Tool-jray/main/haha.py')
elif chon == '7.7': run_tool('https://raw.githubusercontent.com/Khanh23047/Beta-tool/main/beta.py')
elif chon == '8.1': run_tool('https://raw.githubusercontent.com/Khanh23047/DOSS-WEB/main/dos.py')
elif chon == '8.2': run_tool('https://raw.githubusercontent.com/Khanh23047/Reg-pro5-vip/main/reg.py')
elif chon == '8.3': run_tool('https://raw.githubusercontent.com/Khanh23047/Rutgonlink/main/10.py')
elif chon == '8.4': run_tool('https://raw.githubusercontent.com/Khanh23047/Phanhoilink/main/10.py')
elif chon == '8.5': run_tool('https://raw.githubusercontent.com/Khanh23047/L-c-Link-T-File/main/10.py')
elif chon == '9.1': run_tool('https://raw.githubusercontent.com/Khanh23047/May-tinh/main/0.py')
elif chon == '9.2': run_tool('https://raw.githubusercontent.com/Khanh23047/May-bay/main/1.py')
else:
    print(f"{do}[!] Lựa chọn không hợp lệ!")
    sleep(2)