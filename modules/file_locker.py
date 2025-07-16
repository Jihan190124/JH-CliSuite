# modules/file_locker.py

from cryptography.fernet import Fernet
import os
from colorama import Fore, init
init(autoreset=True)

KEY_FILE = "data/lock.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as keyfile:
        keyfile.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE) or os.path.getsize(KEY_FILE) != 44:
        return generate_key()
    with open(KEY_FILE, "rb") as keyfile:
        return keyfile.read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        print(Fore.GREEN + f"[+] File '{filename}' encrypted successfully!")
    except Exception as e:
        print(Fore.RED + f"[!] Encryption failed: {e}")

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(filename, "wb") as dec_file:
            dec_file.write(decrypted)

        print(Fore.GREEN + f"[+] File '{filename}' decrypted successfully!")
    except Exception as e:
        print(Fore.RED + f"[!] Decryption failed: {e}")

def run():
    print(Fore.CYAN + "\n🔐 File Locker/Unlocker by Jihan\n")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Choose option (1-2): ").strip()

    if choice in ['1', '2']:
        path = input("Enter file path: ").strip()
        if not os.path.exists(path):
            print(Fore.RED + "[!] File not found.")
            return
        if choice == '1':
            encrypt_file(path)
        else:
            decrypt_file(path)
    else:
        print(Fore.RED + "[!] Invalid choice.")
