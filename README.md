# # 🧠 Cognitive Trial: Memory Game

Sebuah permainan konsol berbasis Python untuk melatih daya ingat melalui urutan simbol, angka, huruf, hingga kata. Dilengkapi sistem highscore terenkripsi, multi-mode, timer, dan fitur unlockable.

---

## ✨ Fitur Utama
- **3 Mode Permainan**: Classic, Advanced, Extreme  
- **4 Tingkat Kesulitan**: Easy, Normal, Hard, Impossible  
- **Sistem Enkripsi Highscore** (XOR + Base64)  
- **Mode Unlockable** berdasarkan performa pemain  
- **Timer per ronde** (threaded input)  
- **Validasi input otomatis** sesuai tipe challenge  
- **Easter Egg** untuk pencapaian skor tertentu

---

## 🗂️ Struktur & Penjelasan Per Bagian (Detail)
File utama: `main.py`

### 1. Global Variables & Konfigurasi
- `KEY` — dipakai untuk XOR enkripsi/dekripsi.  
- Variabel skor/hiscore tiap mode dan tingkat kesulitan.  
- `difficulty`, `game_mode`, `unlocked_modes` — state permainan.  
- `BOX_WIDTH` — lebar kotak ASCII UI (mudah diubah).

### 2. Enkripsi & Dekripsi
- Fungsi: `encrypt(text)` dan `decrypt(encoded)`.
- Proses: XOR per-byte dengan `KEY` → encode Base64 → disimpan di `scores.dat`.
- Tujuan: mencegah pengubahan skor secara langsung oleh pemain casual.

### 3. Cara Bermain / Tutorial
- `showHowtoPlay(diff)` menampilkan instruksi per tingkat:
  - **Easy**: panah (↑ ↓ ← →) → diinterpretasikan sebagai WASD
  - **Normal**: angka (0–9)
  - **Hard**: huruf A–Z (case-insensitive)
  - **Impossible**: kata (case-sensitive, spasi penting)

### 4. Menu & Mode Permainan
- Menu pilihan: Classic / Advanced / Extreme / Credits / Exit.  
- Pembatasan unlock: Advanced & Extreme terkunci sampai persyaratan terpenuhi.

### 5. Timer Input
- `timed_input(prompt, timeout)` menggunakan `threading.Thread` untuk menunggu input dengan batas waktu.  
- Jika timeout tercapai → mengembalikan `None` (waktu habis).

### 6. UI & Tampilan
- ASCII box layout dengan lebar dinamis (`BOX_WIDTH`).  
- `printRandomColor(text)` memberi warna ANSI acak saat menampilkan sequence.

### 7. Generator Sequence & Rules
- `get_choices()` mengembalikan pilihan berdasarkan `difficulty`.  
  - Easy → panah, Normal → angka, Hard → huruf, Impossible → daftar kata (Indonesia + Jawa Timur + Inggris).  
- Classic & Advanced: sequence bertambah 1 item tiap ronde.  
- Extreme: sequence acak ulang setiap ronde (panjang = nomor ronde).

### 8. Validasi Jawaban
- `validate(answer, user_answer)`:
  - Easy → konversi panah → WASD, case-insensitive.  
  - Normal/Hard → case-insensitive.  
  - Impossible → case-sensitive, harus persis sama.

### 9. Perhitungan Skor
- Dasar: `+1` untuk setiap jawaban benar.  
- Modifier tambahan:
  - Advanced: `+5` per ronde benar.  
  - Extreme: `+10` per ronde benar.  
  - Normal: `+2`, Hard: `+4`, Impossible: `+10`.
- Skor tersimpan ke file terenkripsi setelah setiap perubahan penting.

### 10. Sistem Unlock & Easter Egg
- Unlock Advanced: Classic Impossible **≥ 60**.  
- Unlock Extreme: Advanced Impossible **≥ 90**.  
- Easter Egg (unlock master): Extreme Impossible **≥ 125** — menampilkan credits khusus.

### 11. Penyimpanan Highscore
- File: `scores.dat` (dibuat otomatis bila belum ada).  
- Fungsi: `save_score()` dan `load_scores()` untuk menulis/memulihkan skor terenkripsi.

### 12. Loop Utama
- Program menjalankan `while True: main()` sehingga pemain dapat bermain ulang dan kembali ke menu.

---

## ▶️ Cara Menjalankan
Pastikan Python (3.x) terinstall, lalu jalankan:
```bash
python main.py
```

File `scores.dat` akan dibuat otomatis pada folder tempat program dijalankan.

---

## 👥 Credits
- Developer 1: Rahmad Dwi Syaputra  
- Developer 2: Marcellino Putra Kurniawan  
- SMKN 1 Dlanggu — XII RPL 3 — SpeedRunners
