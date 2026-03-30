import os
import time
import requests
import sys
import platform
import hashlib
from time import sleep
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama requests")
    sys.exit()

CYAN = Fore.CYAN + Style.BRIGHT
WHITE = Fore.WHITE + Style.BRIGHT
GOLD = Fore.YELLOW + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT

# Đường dẫn lưu key
SAVE_PATH = os.path.join(os.path.dirname(os.__file__), "moew_cfg.dat")

LIST_KEY_VIP = {
    'KEY15DAY': {'id': '367', 'exp': '2026-04-15'},
    'MOEW-PRO-888': {'id': 'ANY', 'exp': '2026-12-31'},
    'ADMIN': {'id': 'C8FAAF8BA3CD', 'exp': '2099-01-01'}
}

def get_device_id():
    raw_id = platform.node() + platform.processor() + platform.machine()
    return hashlib.md5(raw_id.encode()).hexdigest().upper()[:12]

def get_short_link(url):
    try:
        api_token = "69bc2b39247a221941623266"
        api_url = f"https://link4m.co/api-shorten/v2?api={api_token}&url={url}"
        res = requests.get(api_url, timeout=15).json()
        return res.get('shortenedUrl') or url
    except:
        return url

def print_banner(my_id):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""
{CYAN} ███╗   ███╗ ██████╗ ███████╗██╗    ██╗    ██╗      ██████╗ ██╗   ██╗███████╗██████╗ 
{CYAN} ████╗ ████║██╔═══██╗██╔════╝██║    ██║    ██║     ██╔═══██╗██║   ██║██╔════╝██╔══██╗
{CYAN} ██╔████╔██║██║   ██║█████╗  ██║ █╗ ██║    ██║     ██║   ██║██║   ██║█████╗  ██████╔╝
{CYAN} ██║╚██╔╝██║██║   ██║██╔══╝  ██║███╗██║    ██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
{CYAN} ██║ ╚═╝ ██║╚██████╔╝███████╗╚███╔███╔╝    ███████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
{CYAN} ╚═╝     ╚═╝ ╚═════╝ ╚══════╝ ╚══╝╚══╝     ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
{WHITE} ───────────────────────────────────────────────────────────────────────────────────
{GOLD} [➤] ID MÁY: {my_id}
{WHITE} ───────────────────────────────────────────────────────────────────────────────────""")

def check_valid_key(input_key, my_id):
    # 1. Kiểm tra VIP
    if input_key in LIST_KEY_VIP:
        v = LIST_KEY_VIP[input_key]
        exp_date = datetime.strptime(v['exp'], '%Y-%m-%d').date()
        if (v['id'] == my_id or v['id'] == 'ANY') and exp_date >= datetime.now().date():
            return True
            
    # 2. Kiểm tra FREE (Logic gốc: timestamp % 10000)
    # Quét trong khoảng 2000 giây gần nhất để đảm bảo tự động vào tool mượt mà
    now = int(time.time())
    mix = sum(ord(c) for c in my_id)
    for i in range(-2000, 2001, 1): 
        if input_key == f"FREE-{mix}-{(now + i) % 10000}":
            return True
    return False

def run_main_tool():
    print(f"{GREEN}[✓] Xác thực thành công! Đang tải Tool...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(
            'https://raw.githubusercontent.com/kieth7199-png/Toolgop/refs/heads/main/moewlover.py',
            timeout=30, headers=headers
        )
        if response.status_code == 200:
            exec(response.text, globals())
            sys.exit()
    except Exception as e:
        print(f"{RED}[!] Lỗi: {e}")
    input(f"\n{CYAN}Nhấn Enter để quay lại...")

def main():
    my_id = get_device_id()
    
    # --- TỰ ĐỘNG VÀO TOOL (DÀNH CHO CẢ FREE VÀ VIP) ---
    if os.path.exists(SAVE_PATH):
        try:
            with open(SAVE_PATH, "r") as f:
                saved_key = f.read().strip()
            if check_valid_key(saved_key, my_id):
                print_banner(my_id)
                print(f"{GREEN}[✓] Tìm thấy Key hợp lệ. Đang tự động vào tool...")
                sleep(1.2)
                run_main_tool()
                return
        except: pass

    while True:
        print_banner(my_id)
        print(f"{CYAN}[1] {WHITE}Lấy Key Free")
        print(f"{GOLD}[2] {WHITE}Nhập Key (VIP/FREE)")
        print(f"{RED}[3] {WHITE}Thoát")
        
        choice = input(f"\n{CYAN}[➤] Chọn: ").strip()
        
        if choice == "1":
            timestamp = int(time.time())
            mix = sum(ord(c) for c in my_id)
            raw_key_free = f"FREE-{mix}-{timestamp % 10000}"
            
            url_goc = f"https://webcodebot.blogspot.com/2026/03/key-ngay-hom-nay-la-function-updatetime_29.html?ma={raw_key_free}"
            short_url = get_short_link(url_goc)
            
            print(f"\n{CYAN}[➤] Link Key: {GOLD}{short_url}")
            input_key = input(f"{CYAN}[?] Nhập Key: ").strip()
            
            if check_valid_key(input_key, my_id):
                with open(SAVE_PATH, "w") as f: f.write(input_key)
                run_main_tool()
            else:
                print(f"{RED}[!] Key sai hoặc đã hết hạn!")
                sleep(2)

        elif choice == "2":
            input_key = input(f"{GOLD}[?] Nhập Key: ").strip()
            if check_valid_key(input_key, my_id):
                with open(SAVE_PATH, "w") as f: f.write(input_key)
                run_main_tool()
            else:
                print(f"{RED}[!] Key không hợp lệ!")
                sleep(2)
        
        elif choice == "3":
            sys.exit()

if __name__ == '__main__':
    main()