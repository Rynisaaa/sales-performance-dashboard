# Sales Performance Dashboard

**Proyek UTS Visualisasi Data — Ganjil TA 2026/2027**

## Identitas
- Nama: [ISI NAMA]
- NPM: [ISI NPM]
- Program Studi: Sistem Informasi / Manajemen Informatika
- Mata Kuliah: Visualisasi Data

## Deskripsi
Dashboard interaktif untuk menganalisis performa penjualan menggunakan Python Streamlit, Pandas, dan Plotly.

## Dataset
- Nama: Sample Superstore
- Sumber Kaggle: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
- Data yang diberikan: 9,994 baris dan 21 kolom.
- Data setelah pembersihan: 9,994 baris.
- Dataset mencakup variabel kategori dan numerik.

## Fitur
1. KPI: total penjualan, jumlah pesanan unik, dan total keuntungan.
2. Empat grafik: tren bulanan, kategori, wilayah, serta scatter penjualan vs keuntungan.
3. Dua filter interaktif: tahun dan kategori produk.
4. Insight otomatis sesuai filter.
5. Pratinjau dan unduhan data hasil filter.

## Hasil Analisis Awal (seluruh dataset)
- Total penjualan: **$2,297,200.86**
- Jumlah Order ID unik: **5,009**
- Total keuntungan: **$286,397.02**
- Kategori dengan penjualan tertinggi: **Technology**
- Wilayah dengan penjualan tertinggi: **West**

## Struktur
```text
sales-dashboard-uts/
├── app.py
├── clean_data.py
├── requirements.txt
├── README.md
└── data/
    ├── Sample - Superstore.csv
    └── superstore_clean.csv
```

## Menjalankan Lokal
```bash
pip install -r requirements.txt
python clean_data.py
streamlit run app.py
```

## Deployment
1. Upload seluruh isi folder ini ke repository GitHub berstatus **Public**.
2. Buka https://share.streamlit.io dan login dengan GitHub.
3. Pilih repository, branch `main`, dan file `app.py`.
4. Klik Deploy.
5. Tempel URL dashboard aktif di sini: [ISI URL STREAMLIT]
6. URL repository GitHub: [ISI URL GITHUB]

Pastikan nama, NPM, URL dashboard, dan URL GitHub dilengkapi sebelum pengumpulan.
