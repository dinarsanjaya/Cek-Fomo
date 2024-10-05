import requests
import json
import colorama
from colorama import Fore, Style
import time

# Inisialisasi colorama
colorama.init(autoreset=True)

# Masukkan API key di sini
API_KEY = ""

# Token yang dicari
TOKEN_TYPE = "0xa340e3db1332c21f20f5c08bef0fa459e733575f9a7e2f5faca64f72cd5a54f2::fomo::FOMO"

# Fungsi untuk mengecek apakah wallet berisi token dan menampilkan jumlahnya
def check_wallet(wallet_address):
    url = f"https://sui-mainnet.blockvision.org/v1/{API_KEY}"  # URL dengan API key
    headers = {
        "Content-Type": "application/json"
    }
    
    # Payload untuk memanggil Sui API, untuk mendapatkan koin yang dimiliki oleh wallet
    payload = {
        "jsonrpc": "2.0",
        "method": "suix_getCoins",
        "params": [wallet_address, TOKEN_TYPE, None, 50],  # Menggunakan list untuk params
        "id": 1
    }

    while True:
        # Request ke API
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Jika request berhasil
        if response.status_code == 200:
            data = response.json()
            if "result" in data and data["result"]["data"]:
                total_fomo = 0
                # Loop melalui data koin dan tambahkan jumlahnya
                for coin in data["result"]["data"]:
                    total_fomo += int(coin["balance"])
                
                # Format jumlah FOMO dengan pemisah ribuan menggunakan titik
                formatted_fomo = f"{total_fomo:,}".replace(",", ".")
                
                # Tampilkan jumlah FOMO yang ditemukan
                print(f"{Fore.GREEN}Wallet {wallet_address} berisi {formatted_fomo} FOMO.")
                return total_fomo  # Kembalikan total FOMO dari wallet ini
            else:
                print(f"{Fore.RED}Wallet {wallet_address} tidak berisi token FOMO.")
                return 0  # Jika tidak ada token, kembalikan 0
            break
        elif response.status_code == 429:
            print(f"{Fore.YELLOW}Rate limit tercapai. Menunggu 5 detik sebelum mencoba lagi...")
            time.sleep(5)  # Tunggu 5 detik sebelum mencoba lagi
        else:
            print(f"{Fore.YELLOW}Gagal mengakses wallet {wallet_address}. Status code: {response.status_code}")
            return 0  # Jika gagal, kembalikan 0

# Baca daftar wallet dari file wallet.txt
total_fomo_all_wallets = 0  # Inisialisasi total FOMO untuk semua wallet
with open("wallet.txt", "r") as file:
    wallets = file.readlines()

# Cek tiap wallet di file
for wallet in wallets:
    wallet = wallet.strip()  # Menghapus spasi atau newline
    total_fomo_all_wallets += check_wallet(wallet)  # Tambahkan total FOMO dari wallet ini
    time.sleep(1)  # Tambahkan delay 1 detik antara setiap request

# Format dan tampilkan total FOMO dari semua wallet
formatted_total_fomo = f"{total_fomo_all_wallets:,}".replace(",", ".")
print(f"{Fore.BLUE}Total FOMO dari semua wallet: {formatted_total_fomo} FOMO.")
