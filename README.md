# Cek-Fomo
========

**Cek-Fomo** adalah script Python untuk memeriksa saldo token FOMO dalam wallet Sui Network dengan memanfaatkan BlockVision RPC API. Script ini akan membaca daftar wallet dari file `wallet.txt` dan menampilkan jumlah token FOMO yang dimiliki oleh setiap wallet, serta menangani rate limit API secara otomatis.

Persyaratan
-----------

*   Python 3.x
*   `requests`: Untuk mengirim permintaan HTTP ke API.
*   `colorama`: Untuk menampilkan hasil dengan warna di terminal.

Instalasi
---------

1.  Clone repositori ini:
    
        git clone https://github.com/dinarsanjaya/Cek-Fomo
    
2.  Masuk ke direktori proyek:
    
        cd Cek-Fomo
    
3.  Install dependensi:
    
        pip install -r requirements.txt
    
4.  Buat file `wallet.txt` yang berisi daftar alamat wallet Sui yang ingin diperiksa, satu alamat per baris. Contoh:
    
        0xf11f64f84fa9df7d50912432795xxxxxxxxxxxxxxxxxxx
        0x1ae9d2965a02b4b1253b1e62f82xxxxxxxxxxxxxxxxxxx
    

Konfigurasi API
---------------

1.  Dapatkan **API key** dari BlockVision dengan mendaftar di [BlockVision](https://blockvision.org/).
2.  Edit script Python di `line 11` untuk memasukkan API key Anda:
    
        API_KEY = "masukkan-api-key-anda-di-sini"
    

Menjalankan Script
------------------

Setelah API key sudah ditambahkan dan `wallet.txt` telah dibuat, kamu bisa menjalankan script dengan perintah berikut:

    python app.py

Hasil akan ditampilkan di terminal, dengan detail jumlah token FOMO untuk setiap wallet yang ada di `wallet.txt`.

Contoh Output
-------------

    Wallet 0xf11f64f84fa9df7d50912432795xxxxxxxxxxxxxxxxxxx berisi 937.565.673.680 FOMO.
    Wallet 0x1ae9d2965a02b4b1253b1e62f82xxxxxxxxxxxxxxxxxxx tidak berisi token FOMO.

Penanganan Rate Limit
---------------------

Jika API mengalami **rate limit** (status code 429), script akan menunggu selama 5 detik dan mencoba lagi secara otomatis.

Lisensi
-------

Proyek ini dilisensikan di bawah lisensi MIT.
