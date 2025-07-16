from modules import wifi_scanner, ip_lookup, file_locker,weather_news,device_scanner

from utils import banner

def show_menu():
    banner.show_logo()
    print("\nChoose a tool:\n")
    print("1. Wi-Fi Scanner 📡")
    print("2. IP Info Lookup 🌐")
    print("3. File Locker/Unlocker 🔐")
    print("4. Weather & News CLI ☁️📰")
    print("5. Device & Port Scanner 🧠")

    print("0. Exit\n")

while True:
    show_menu()
    choice = input("Enter option (0-1): ").strip()
    if choice == '1':
        wifi_scanner.run()
    elif choice == '2':
        ip_lookup.run()
    elif choice == '3':
        file_locker.run()
    elif choice == '4':
        weather_news.run()
    elif choice == '5':
        device_scanner.run()

    elif choice == '0':
        print("Exiting... Stay stealthy, hacker 🐍")
        break
    else:
        print("Invalid input. Try again.")
