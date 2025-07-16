# 🇮🇩 Stress Test Ekspor – Web App

Sebuah aplikasi web ringan berbasis Python Flask untuk melakukan simulasi cepat terhadap dampak tarif ekspor (misalnya tarif baru dari AS) terhadap sektor-sektor ekspor utama Indonesia.

### Tujuan
Aplikasi ini bertujuan membantu pengambil kebijakan, peneliti, atau pengamat ekonomi untuk:
- Menghitung potensi penurunan ekspor akibat kenaikan tarif,
- Memperkirakan nilai ekspor yang hilang,
- Memprediksi risiko PHK di sektor terkait,
- Menyediakan data visualisasi dan hasil simulasi yang bisa diunduh dalam format CSV.

---

## Fitur Utama

- Upload file data sektor ekspor (CSV/Excel)
- Input nilai tarif tambahan (%)
- Tabel hasil simulasi: Penurunan Ekspor, Nilai Hilang, Estimasi PHK
- Visualisasi dengan Chart.js
- Tombol download hasil simulasi (CSV)

---

## Cara Menjalankan Aplikasi

### 1. Clone repositori ini

```bash
git clone https://github.com/namamu/stress-test-ekspor-indonesia.git
cd stress-test-ekspor-indonesia

### 2. Buat environment dan install dependencies
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt

### 3. Jalankan aplikasi
```bash
python app.py
