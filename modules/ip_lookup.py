# modules/ip_lookup.py

import requests
from colorama import Fore, init
init(autoreset=True)

def run():
    print(Fore.CYAN + "\n🌐 IP Info Lookup Tool by Jihan")
    print(Fore.YELLOW + "[*] Fetching IP and geo info...")

    try:
        res = requests.get("http://ip-api.com/json/", timeout=5)
        data = res.json()

        if data["status"] == "success":
            print(Fore.GREEN + f"\nIP Address     : {data['query']}")
            print(Fore.GREEN + f"ISP            : {data['isp']}")
            print(Fore.GREEN + f"Organization   : {data['org']}")
            print(Fore.GREEN + f"Country        : {data['country']} ({data['countryCode']})")
            print(Fore.GREEN + f"Region         : {data['regionName']}")
            print(Fore.GREEN + f"City           : {data['city']}")
            print(Fore.GREEN + f"ZIP Code       : {data['zip']}")
            print(Fore.GREEN + f"Latitude       : {data['lat']}")
            print(Fore.GREEN + f"Longitude      : {data['lon']}")
            print(Fore.GREEN + f"Timezone       : {data['timezone']}")
        else:
            print(Fore.RED + "[!] Could not fetch IP info.")
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")
