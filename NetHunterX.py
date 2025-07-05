
import socket
import os
from colorama import Fore, Style, init
init(autoreset=True)

def skull_logo():
    os.system("clear")
    print(Fore.RED + "☠️ " * 18 + " NetHunterX v2 - Socket Scan " + " ☠️" * 18)
    print(Fore.LIGHTRED_EX + "              Developed by Encrypter Mafia")
    print(Fore.MAGENTA + "              Telegram: @EncrypterMafia\n")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def scan_network(base_ip):
    print(f"{Fore.YELLOW}🔍 Scanning devices on your network (Port 80)... This may take a few seconds.{Style.RESET_ALL}\n")
    live_count = 0
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
                print(f"{Fore.GREEN}[+] {ip} --> {Fore.CYAN}{hostname}{Style.RESET_ALL}")
                live_count += 1
            sock.close()
        except:
            pass
    print(f"\n{Fore.LIGHTGREEN_EX}✅ Scanning Completed - {live_count} device(s) found. - By Encrypter Mafia{Style.RESET_ALL}\n")

def main():
    skull_logo()
    choice = input(f"{Fore.CYAN}Do you want to scan your network using socket scan? (Y/N): {Style.RESET_ALL}").strip().lower()
    if choice == "y":
        local_ip = get_local_ip()
        base_ip = ".".join(local_ip.split(".")[:-1])
        scan_network(base_ip)
    else:
        print(f"{Fore.LIGHTRED_EX}Aborted by user.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
