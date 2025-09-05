
import os
import subprocess
import time
from scapy.all import rdpcap, IP
from collections import defaultdict
import socket

from colorama import init, Fore, Style

def display_watermark():
    init(autoreset=True)  # Initialize colorama (resets color after each print automatically)

    print(Fore.GREEN + Style.BRIGHT + r"""
.___   _____      _____    ___________________  _____________________    _____  _________  ____  __._____________________ 
|   | /     \    /  _  \  /  _____/\_   _____/  \__    ___/\______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \
|   |/  \ /  \  /  /_\  \/   \  ___ |    __)_     |    |    |       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/
|   /    Y    \/    |    \    \_\  \|        \    |    |    |    |   \/    |    \     \___|    |  \  |        \ |    |   \
|___\____|__  /\____|__  /\______  /_______  /    |____|    |____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  /
            \/         \/        \/        \/                     \/         \/        \/        \/        \/         \/  

                   >>> IMAGE TRACKER - Created by: IRUMOS ("Komal") <<<
    """ + Style.RESET_ALL)


def capture_traffic(interface, duration, output_file="traffic_https.pcap"):
    print(f"[+] Capturing traffic on interface '{interface}' for {duration} seconds...")
    command = ["tcpdump", "-i", interface, "-w", output_file]
    proc = subprocess.Popen(["sudo"] + command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(duration)
    proc.terminate()
    print("[+] Capture complete.")

def analyze_https_traffic(pcap_file):
    print(f"[+] Analyzing traffic from {pcap_file}...")
    try:
        packets = rdpcap(pcap_file)
    except Exception as e:
        print(f"[!] Failed to read pcap file: {e}")
        return

    destinations = defaultdict(int)

    for pkt in packets:
        if IP in pkt:
            ip_dst = pkt[IP].dst
            pkt_len = len(pkt)
            destinations[ip_dst] += pkt_len

    sorted_dests = sorted(destinations.items(), key=lambda x: x[1], reverse=True)

    print("\n[*] Top connections by data sent during image upload:")
    for ip, total_bytes in sorted_dests[:10]:
        try:
            domain = socket.gethostbyaddr(ip)[0]
        except:
            domain = "Unknown"
        print(f" - {ip} ({domain}) : {total_bytes} bytes")

def main():
    display_watermark()
    print("--- HTTPS Image Tracker ---")
    interface = input("Enter network interface to monitor (e.g., wlan0, eth0): ").strip()
    duration = int(input("Enter duration of capture in seconds: ").strip())
    pcap_file = "traffic_https.pcap"

    capture_traffic(interface, duration, pcap_file)
    analyze_https_traffic(pcap_file)

if __name__ == "__main__":
    main()
