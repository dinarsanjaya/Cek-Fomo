  Cek-Fomo body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; padding: 20px; background-color: #f4f4f4; } h1, h2, h3 { color: #333; } pre { background: #eaeaea; padding: 10px; border-radius: 5px; overflow: auto; } code { background: #eaeaea; padding: 2px 4px; border-radius: 4px; }

Cek-Fomo
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
    
        git clone https://github.com/username/Cek-Fomo.git
    
2.  Masuk ke direktori proyek:
    
        cd Cek-Fomo
    
3.  Install dependensi:
    
        pip install -r requirements.txt
    
4.  Buat file `wallet.txt` yang berisi daftar alamat wallet Sui yang ingin diperiksa, satu alamat per baris. Contoh:
    
        0xf11f64f84fa9df7d509124327957a5bf21fca45d051f2d858b1c3d4d42262efb
        0x1ae9d2965a02b4b1253b1e62f8234f524875802b122ed55160297f2a8ab7ddce
    

Konfigurasi API
---------------

1.  Dapatkan **API key** dari BlockVision dengan mendaftar di [BlockVision](https://blockvision.org/).
2.  Edit script Python di `line 11` untuk memasukkan API key Anda:
    
        API_KEY = "masukkan-api-key-anda-di-sini"
    

Menjalankan Script
------------------

Setelah API key sudah ditambahkan dan `wallet.txt` telah dibuat, kamu bisa menjalankan script dengan perintah berikut:

    python cek_fomo.py

Hasil akan ditampilkan di terminal, dengan detail jumlah token FOMO untuk setiap wallet yang ada di `wallet.txt`.

Contoh Output
-------------

    Wallet 0xf11f64f84fa9df7d509124327957a5bf21fca45d051f2d858b1c3d4d42262efb berisi 937.565.673.680 FOMO.
    Wallet 0x1ae9d2965a02b4b1253b1e62f8234f524875802b122ed55160297f2a8ab7ddce tidak berisi token FOMO.

Penanganan Rate Limit
---------------------

Jika API mengalami **rate limit** (status code 429), script akan menunggu selama 5 detik dan mencoba lagi secara otomatis.

Lisensi
-------

Proyek ini dilisensikan di bawah lisensi MIT.
