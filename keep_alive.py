#!/usr/bin/env python3
"""
Script untuk menjaga sesi Binder tetap aktif
Dijalankan secara background
"""

import requests
import time
import os
import threading
from datetime import datetime

def ping_server():
    """Mengirim ping ke server untuk mencegah idle timeout"""
    try:
        # URL internal Binder
        base_url = os.environ.get('JUPYTERHUB_SERVICE_PREFIX', '')
        if base_url:
            health_url = f"http://localhost:8888{base_url}api/status"
            response = requests.get(health_url, timeout=5)
            
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] Ping successful - Status: {response.status_code}")
            
            # Simulasi aktivitas dengan membuat file kecil
            with open('/tmp/last_ping.txt', 'w') as f:
                f.write(current_time)
                
    except Exception as e:
        print(f"Ping failed: {str(e)}")

def keep_alive_loop():
    """Loop utama untuk menjaga koneksi"""
    print("=== Binder Keep-Alive Started ===")
    print("Session will auto-refresh every 5 minutes")
    
    while True:
        try:
            ping_server()
            # Ping setiap 5 menit (lebih pendek dari timeout Binder)
            time.sleep(300)  # 300 detik = 5 menit
        except KeyboardInterrupt:
            print("Keep-alive stopped")
            break
        except Exception as e:
            print(f"Error in keep-alive: {e}")
            time.sleep(60)

if __name__ == "__main__":
    # Jalankan di background thread
    keep_thread = threading.Thread(target=keep_alive_loop, daemon=True)
    keep_thread.start()
    
    # Tahan program utama tetap berjalan
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
