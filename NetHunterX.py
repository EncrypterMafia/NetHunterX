
import os
import socket
import platform
import threading
from queue import Queue
from colorama import Fore, Style, init
init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.RED + "╔" + "═" * 65 + "╗")
    print(Fore.RED + "║" + Fore.LIGHTRED_EX + "   ☠️ NetHunterX - Auto Subnet Device Scanner ☠️".center(65) + Fore.RED + "║")
    print(Fore.RED + "╠" + "═" * 65 + "╣")
    print(Fore.RED + "║" + Fore.YELLOW + "       Developed by Encrypter Mafia".center(65) + Fore.RED + "║")
    print(Fore.RED + "║" + Fore.MAGENTA + "       Telegram: @EncrypterMafia".center(65) + Fore.RED + "║")
    print(Fore.RED + "╚" + "═" * 65 + "╝\n")

def get_base_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ".".join(ip.split(".")[:3])
    except:
        return "192.168.1"

def ping(ip, live_hosts):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-W", "1", ip]
    response = os.popen(" ".join(command)).read()
    if "ttl" in response.lower():
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "Unknown Device"
        live_hosts.append((ip, hostname))

def scan_subnet(base_ip, live_hosts):
    q = Queue()
    def threader():
        while not q.empty():
            ip = q.get()
            ping(ip, live_hosts)
            q.task_done()

    for i in range(1, 255):
        q.put(f"{base_ip}.{i}")

    for _ in range(50):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    q.join()

def main():
    banner()
    base_ip = get_base_ip()
    print(Fore.CYAN + f"📡 Detected Local Subnet: {base_ip}.x")
    print(Fore.YELLOW + "\n🔍 Scanning your local subnet for active devices...\n")

    live_hosts = []
    scan_subnet(base_ip, live_hosts)

    print(Fore.GREEN + f"\n📡 {len(live_hosts)} Device(s) Found:")
    print(Fore.LIGHTBLACK_EX + "-" * 60)
    for ip, hostname in live_hosts:
        print(Fore.GREEN + f"[+] {ip} --> {Fore.CYAN}{hostname}")
    print(Fore.LIGHTBLACK_EX + "-" * 60)
    print(Fore.LIGHTGREEN_EX + "\n✅ Auto Subnet Device Scan Finished - By Encrypter Mafia\n")

if __name__ == "__main__":
    main()
