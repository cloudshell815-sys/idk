# Persistent Binder Session

Repositori ini dikonfigurasi untuk memperpanjang masa hidup sesi Binder.

## 🚀 Cara Menggunakan
1. Klik badge di bawah untuk memulai:
   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/username/repo/HEAD)

2. Session akan:
   - Auto-ping setiap 5 menit
   - Membuat notebook contoh otomatis
   - Mempertahankan koneksi lebih lama

## ⚠️ Batasan
- **Bukan benar-benar 24/7** - Binder tetap timeout setelah ~12 jam
- **Harus restart manual** setelah timeout
- **Data tidak persist** antar sesi (selalu download hasil kerja)

## 🔧 Konfigurasi
Script utama:
- `keep_alive.py` - Mengirim ping otomatis
- `start` - Script startup
- `requirements.txt` - Dependencies

## 💾 Menyimpan Data
Selalu download file penting:
```python
from IPython.display import FileLinks
FileLinks('.')  # Tampilkan semua file untuk download
