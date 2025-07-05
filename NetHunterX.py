
import socket
import os
import threading
import time
from colorama import Fore, Style, init
init(autoreset=True)

def skull_logo():
    os.system("clear")
    print(Fore.RED + "╔" + "═" * 65 + "╗")
    print(Fore.RED + "║" + Fore.LIGHTRED_EX + "         ☠️  NETHUNTERX: ENCRYPTER MAFIA HACKER TOOL ☠️".center(65) + Fore.RED + "║")
    print(Fore.RED + "╠" + "═" * 65 + "╣")
    print(Fore.RED + "║" + Fore.YELLOW + "               Developed by Encrypter Mafia".center(65) + Fore.RED + "║")
    print(Fore.RED + "║" + Fore.MAGENTA + "               Telegram: @EncrypterMafia".center(65) + Fore.RED + "║")
    print(Fore.RED + "╚" + "═" * 65 + "╝\n")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def scan_network(base_ip, live_hosts, finished_flag):
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((ip, 80))
            if result == 0:
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except:
                    hostname = "Unknown Device"
                live_hosts.append((ip, hostname))
            sock.close()
        except:
            pass
    finished_flag.append(True)

def satellite_animation(finished_flag):
    spinner = ['🛰️ ', ' 🛰️', ' 🛰️', '🛰️ ']
    dots = ["", ".", "..", "...", "...."]
    i = 0
    while not finished_flag:
        print(Fore.CYAN + f"\r{spinner[i % len(spinner)]} " + Fore.YELLOW + f"Scanning in progress {dots[i % len(dots)]}", end="")
        time.sleep(0.3)
        i += 1
    print(Fore.GREEN + "\r✅ Scanning completed!                             ")

def main():
    skull_logo()
    choice = input(f"{Fore.LIGHTCYAN_EX}Do you want to scan your network using socket scan? (Y/N): {Style.RESET_ALL}").strip().lower()
    if choice == "y":
        local_ip = get_local_ip()
        base_ip = ".".join(local_ip.split(".")[:-1])
        live_hosts = []
        finished_flag = []

        scan_thread = threading.Thread(target=scan_network, args=(base_ip, live_hosts, finished_flag))
        scan_thread.start()

        satellite_animation(finished_flag)

        scan_thread.join()

        print(Fore.LIGHTMAGENTA_EX + "\n📡 Discovered Devices:")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        for ip, hostname in live_hosts:
            print(f"{Fore.GREEN}[+] {ip} --> {Fore.CYAN}{hostname}")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(f"\n{Fore.LIGHTGREEN_EX}✅ Network Scan Finished - By Encrypter Mafia{Style.RESET_ALL}\n")
    else:
        print(f"{Fore.LIGHTRED_EX}Aborted by user.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
