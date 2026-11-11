#!/usr/bin/env python3
import http.server
import socket
import socketserver
import os
import sys

PORT = 8080

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():
    os.system('clear')
    
    # Stylish ASCII Banner & Design Box
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                  ⚡ LOCALDROP UTILITY ⚡                 ║")
    print("║              Fast & Secure File Sharing Tool             ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(" 🎨 Creator : Ojas Pratap Singh")
    print("════════════════════════════════════════════════════════════")
    
    my_ip = get_ip()
    current_dir = os.getcwd()
    
    print(f"\n 📂 Sharing Folder : {current_dir}")
    print(f" 🚀 Server Status  : Active & Running Smoothly")
    print(f" 🔗 Access URL     : http://{my_ip}:{PORT}")
    
    print("\n" + "═" * 60)
    print(" 📌 HOW TO USE THIS TOOL:")
    print(" ----------------------------------------------------------")
    print(" 1. Keep this Termux session active in the background.")
    print(" 2. Connect your PC, Laptop or another phone to same Wi-Fi/Hotspot.")
    print(" 3. Open the above Access URL in any web browser.")
    print(" 4. Download, view and share your files instantly without internet!")
    print("═" * 60)
    print("\n ⚠️ [!] Press 'Ctrl + C' anytime to stop the server safely.\n")

    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n╔══════════════════════════════════════════════════════════╗")
            print("║     [!] LocalDrop Server Stopped Successfully. Bye!      ║")
            print("╚══════════════════════════════════════════════════════════╝\n")
            sys.exit(0)

if __name__ == '__main__':
    main()

