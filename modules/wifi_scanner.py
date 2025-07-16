# modules/wifi_scanner.py

import subprocess
import re
import time
import os
from colorama import Fore, init

init(autoreset=True)

AIRPORT = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"

def clear():
    os.system("clear")

def banner():
    print(Fore.GREEN + r"""⚡ WiFiNers - Scanner Module by Jihan ⚡""")

def scan_wifi():
    result = subprocess.run([AIRPORT, "-s"], stdout=subprocess.PIPE)
    output = result.stdout.decode()

    networks = []
    lines = output.strip().splitlines()

    if lines and "SSID" in lines[0]:
        lines = lines[1:]

    for line in lines:
        try:
            line = re.sub(r'\s{2,}', '\t', line.strip())
            parts = line.split('\t')
            if len(parts) < 5:
                continue
            ssid = parts[0]
            bssid = parts[1]
            rssi = parts[2]
            channel = parts[3]
            security = parts[4] if len(parts) >= 5 else "?"
            networks.append((ssid, bssid, rssi, channel, security))
        except:
            continue

    return networks

def detect_evil_twins(networks):
    ssid_map = {}
    for ssid, bssid, *_ in networks:
        if ssid in ssid_map:
            ssid_map[ssid].add(bssid)
        else:
            ssid_map[ssid] = set([bssid])

    suspicious = {ssid: list(bssids) for ssid, bssids in ssid_map.items() if len(bssids) > 1}
    return suspicious

def display_networks(networks):
    print(Fore.YELLOW + f"{'SSID':<25}{'BSSID':<20}{'RSSI':<6}{'CH':<4}{'SECURITY'}")
    print(Fore.YELLOW + "-" * 70)
    for ssid, bssid, rssi, channel, security in networks:
        try:
            rssi_int = int(rssi)
            rssi_color = (
                Fore.RED if rssi_int < -70 else
                Fore.GREEN if rssi_int > -50 else
                Fore.YELLOW
            )
        except:
            rssi_color = Fore.WHITE

        print(f"{Fore.WHITE}{ssid:<25}{bssid:<20}{rssi_color}{rssi:<6}{Fore.MAGENTA}{channel:<4}{Fore.CYAN}{security}")

def run():
    try:
        while True:
            clear()
            banner()
            print(Fore.BLUE + "[*] Scanning nearby Wi-Fi networks...\n")
            networks = scan_wifi()
            display_networks(networks)

            evil_twins = detect_evil_twins(networks)
            if evil_twins:
                print(Fore.RED + "\n[!] ⚠️ Possible Evil Twin Networks Found:")
                for ssid, bssids in evil_twins.items():
                    print(Fore.LIGHTRED_EX + f"   → SSID: '{ssid}' has {len(bssids)} BSSIDs: {bssids}")

            print(Fore.WHITE + "\n[CTRL+C to exit] Refreshing in 5 seconds...")
            time.sleep(5)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Exiting WiFiHunter. Stay stealthy 🥷")
