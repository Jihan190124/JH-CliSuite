# modules/weather_news.py

import requests
from colorama import Fore, init
init(autoreset=True)

def get_weather(city):
    try:
        print(Fore.CYAN + f"\n☁️  Weather in {city}:\n")
        url = f"https://wttr.in/{city}?format=3"
        res = requests.get(url, timeout=5)
        print(Fore.GREEN + res.text)
    except:
        print(Fore.RED + "[!] Failed to fetch weather info.")

def get_news():
    try:
        print(Fore.CYAN + "\n📰 Top News Headlines:\n")
        res = requests.get("https://inshortsapi.vercel.app/news?category=technology", timeout=5)
        news = res.json().get("data", [])[:5]

        for i, item in enumerate(news, 1):
            print(Fore.YELLOW + f"{i}. {item['title']}")
            print(Fore.WHITE + f"   {item['content']}\n")
    except:
        print(Fore.RED + "[!] Failed to fetch news.")

def run():
    print(Fore.MAGENTA + "\n🌐 Weather & News CLI by Jihan")
    city = input(Fore.YELLOW + "Enter city name (default: Ahmedabad): ").strip()
    if not city:
        city = "Ahmedabad"

    get_weather(city)
    get_news()
