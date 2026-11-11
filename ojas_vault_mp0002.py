import os
import hashlib
import getpass
import shutil

# MP0002 - Ojas-Crypt Secure Vault Directory
VAULT_DIR = os.path.expanduser("~/.ojas_crypt_mp0002")
KEY_FILE = os.path.join(VAULT_DIR, "master.key")

def show_banner():
    print("==================================================")
    print("       C R E A T E D   B Y   O J A S   P R A T A P   S I N G H       ")
    print("==================================================")
    print(" कुछ हाइड करने आया है क्या ब्रो? कर ले सब तेरा ही है! 🔥")
    print("==================================================\n")

def init_vault():
    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR)
        show_banner()
        print("[+] Initializing MP0002 secure vault...")
        
        pin = getpass.getpass("Set your Master PIN: ")
        confirm_pin = getpass.getpass("Confirm your Master PIN: ")
        
        if pin == confirm_pin:
            hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
            with open(KEY_FILE, "w") as f:
                f.write(hashed_pin)
            print("[✓] MP0002 successfully initialized and locked!\n")
        else:
            print("[!] PINs do not match. Run the script again.")
            exit()

def verify_pin():
    if not os.path.exists(KEY_FILE):
        init_vault()
        
    show_banner()
    print("  MP0002: Ojas-Crypt Locked       ")
    print("==================================")
    
    with open(KEY_FILE, "r") as f:
        stored_hash = f.read().strip()
        
    entered_pin = getpass.getpass("Enter your Master PIN to unlock: ")
    hashed_entered = hashlib.sha256(entered_pin.encode()).hexdigest()
    
    if hashed_entered == stored_hash:
        print("[✓] Access Granted!\n")
        return True
    else:
        print("[X] Access Denied! Wrong PIN.")
        return False

def lock_file():
    file_path = input("Enter the path of the file you want to hide/lock: ").strip()
    
    if os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(VAULT_DIR, file_name)
        
        shutil.move(file_path, dest_path)
        print(f"[✓] Success! File '{file_name}' is now safely locked inside MP0002.\n")
    else:
        print("[!] Error: File not found. Check the path and try again.\n")

def list_files():
    files = os.listdir(VAULT_DIR)
    locked_files = [f for f in files if f != "master.key"]
    
    print("\n--- Locked Files Inside MP0002 ---")
    if not locked_files:
        print("[i] Vault is currently empty.")
    else:
        for idx, f in enumerate(locked_files, 1):
            print(f"{idx}. {f}")
    print("----------------------------------\n")

def unlock_file():
    list_files()
    file_name = input("Enter the exact name of the file you want to restore/unlock: ").strip()
    src_path = os.path.join(VAULT_DIR, file_name)
    
    if os.path.exists(src_path) and file_name != "master.key":
        dest_path = os.path.expanduser(f"~/{file_name}")
        shutil.move(src_path, dest_path)
        print(f"[✓] Success! File '{file_name}' has been restored to your home directory.\n")
    else:
        print("[!] Error: File not found inside the vault.\n")

def main():
    if not verify_pin():
        return
        
    while True:
        print("--- MP0002 Dashboard ---")
        print("1. Lock / Hide a File")
        print("2. List Locked Files")
        print("3. Unlock / Restore a File")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            lock_file()
        elif choice == '2':
            list_files()
        elif choice == '3':
            unlock_file()
        elif choice == '4':
            print("Exiting MP0002. Stay secure!")
            break
        else:
            print("[!] Invalid option. Choose between 1 to 4.\n")

if __name__ == "__main__":
    main()

