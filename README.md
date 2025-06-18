# Analisis-Transisi-Energi-Hijau-2025-di-Indonesia
---

**Nama: Agus Iskandar Darmawan**

**No Absen: 09.009.DB2025**

**Week Task**

---

### ✏️ Pendahuluan

Indonesia mengejar target ambisius, yaitu 23% energi terbarukan pada 2025. Namun, Data Kementerian ESDM menunjukkan kita baru mencapai 12% energi terbarukan pada 2023, jauh dari target. 

Pemerintah menerapkan pajak karbon untuk kurangi emisi industri, seperti di sektor tekstil Jawa Barat. Tapi, masih banyak perusahaan melakukan greenwashing, yakni mengklaim ramah lingkungan padahal emisinya tinggi. Hal tersebut menyesatkan investor. Selain itu, di Jawa Tengah dan Sulawesi Selatan, proyek PLTS juga sering memicu konflik lahan dengan petani dan masyarakat adat. 

Permasalahan tersebut butuh solusi cerdas. Dengan menggunakan Python, perhitungan pajak karbon, deteksi greenwashing, dan analisis risiko konflik lahan bisa dibuat. Dari hasil analisi yang didapatkan, akan dihasilkan saran untuk pemerintah agar investasi energi hijau lancar dan konflik minim.

### 📝 Permasalahan

Transisi energi hijau 2025 di Indonesia menghadapi tiga masalah utama. Pertama, data emisi perusahaan sering tidak akurat, menyulitkan penerapan pajak karbon, terutama di industri tekstil Jawa Barat. Kedua, greenwashing merajalela. Banyak perusahaan mengklaim hijau, tapi emisinya melebihi batas. KLHK melaporkan 25% klaim hijau tidak terverifikasi. 

Ketiga, konflik lahan menghambat proyek PLTS. Di Jawa Tengah, lahan sawah petani diambil untuk PLTS, memicu 800 konflik lahan pada 2023, menurut WALHI. Ini menghalangi investasi energi hijau dan merugikan komunitas lokal. Tanpa analisis data yang solid, pemerintah kesulitan membuat kebijakan efektif. Kita akan pakai Python untuk menghitung pajak karbon, mendeteksi greenwashing, dan mengevaluasi risiko lahan. Solusi ini membantu capai Net Zero Emission 2060 dan mengurangi konflik sosial. 

### 📈 Analisis Python

Analisis Python merupakan analisis data menggunakan Python adalah proses mengeksplorasi, membersihkan, mengubah, dan memodelkan data untuk menemukan informasi yang berguna, menarik kesimpulan, dan mendukung pengambilan keputusan. Anaslisis ini Pandas untuk manipulasi dan analisis data tabular, NumPy untuk komputasi numerik, dan Matplotlib visualisasi data.

### </> Analisis dan Visualisasi Data

Data yang digunakan merupakan data berbentuk CSV yang didapat dari Walhi. Database terdiri dari tiga tabulasi CSV, yakni emisi_perusahaan.csv yang berisi data emisi perusahaan di Jawa Barat, konflik_lahan.csv yang beriisi data konflik lahan PLTS di Indonesia, dan tren_emisi.csv yang berisi tren emisi perusahaan di jawa barat selama 4 tahun, antara 2000-2024. Perhitunan dan analisis ini dibagi menjadi queri untuk memudahkan proses coding.

Data Emisi Perusahaan

![emisi_perusahaan](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/emisi_perusahaan.png)

Data Konflik Lahan

![konflik_lahan](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/konflik_lahan.png)

Data Tren Emisi 2020-2023

![tren_emisi](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/tren_emisi.png)

#### Query 1: Mengecek Status Pajak


Tujuan: Mengecek apakah emisi perusahaan dari CSV melebihi batas pajak karbon (50 ton CO2)

Konsep: If-else, Pandas untuk CSV

Output: Status Pajak (kena atau bebas) untuk Setiap Perusahaan

```

import pandas as pd

df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')

batas = 50

for index, row in df.iterrows():
    emisi = row['Emisi_2024']
    perusahaan = row['Nama_Perusahaan']
    if emisi > batas:
        print(f"{perusahaan} kena pajak karbon dengan emisi {emisi} ton")
    else:
        print(f"{perusahaan} bebas pajak karbon dengan emisi {emisi} ton")
        
```

Queri ini menggunakan Pandas untuk cek kepatuhan pajak karbon dari data CSV. Emisi diambil dari emisi_perusahaan.csv, dibandingkan dengan batas 50 ton CO2 (standar sederhana, misalnya Perpres 98/2021), menggunakan If-else untuk menentukan status pajak.

Output:

![Mengecek kepatuhan pajak](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/status%20pajak%202.png)


#### Query 2: Menghitung Pajak Karbon

Tujuan: Menghitung Pajak Karbon untuk Perusahaan dari CSV Berdasarkan Emisi 2024

Konsep if-else, Pandas untuk baca csv

Output: Nilai Pajak (RP) untuk Setiap Perusahaan

```

import pandas as pd
df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')
batas = 50
tarif = 20000

for index, row in df.iterrows():
    emisi = row['Emisi_2024']
    perusahaan = row['Nama_Perusahaan']
    if emisi > batas:
        pajak = (emisi - batas) * tarif
        print(f"{perusahaan} kena pajak karbon Rp {pajak}")
    else:
        print(f"{perusahaan} bebas kena karbon")
  
```

Output:

![Hitung_Pajak](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/status%20pajak.png)

Query ini menghitung pajak karbon dari CSV. Kalau emisi lebih dari 50 ton, kita hitung Rp20.000 per ton kelebihan. Pakai if-else dan Pandas, ini bantu patuh regulasi karbon.

#### Query 3: Menyimpan Data Emisi dalam List

Tujuan: Menyimpan Emisi Perusahaan dari CSV ke dalam List untuk Analisis

Konsep: List dan for loop, Pandas untuk Baca CSV

Output: List Berisi Emisi Perusahaan 

```

import pandas as pd

df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')

emisi_list = []

for index, row in df.iterrows():

    emisi = row['Emisi_2024']

    emisi_list.append(emisi)

print("Data emisi perusahaan:", emisi_list)

```

Output:

![Data_dalam_list](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/emisi%20dalam%20list.png)

Query ini menggunakna list untuk menyimpan emisi dari emisi_perusahaan.csv, langkah awal mengelola data regulasi karbon. For loop dan append() digunakan untuk mengumpulkan data, cocok untuk pemula. Emisi diambil dari kolom Emisi_2024, realistis untuk industri menengah. Query ini kembangkan Query 2, beralih ke struktur data massal, mempersiapkan analisis lebih kompleks. Batas 50 ton (standar lingkungan) jadi acuan. Hasilnya bantu pemerintah verifikasi emisi, membangun portofolio dengan struktur data dasar, mendukung usulan verifikasi.


#### Query 4: Analisis Kepatuhan Emisi dengan Metode LIST

Tujuan: Mengecek Kepatuhan Emisi Perusahaan dari list berdasarkan Batas Pajak

Konsep: List, for Loof, if-else, Pandas untuk Baca CSV

Output: Status Pajak untuk Setiap Emisi

```

import pandas as pd

df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')

emisi_list = []

for index, row in df.iterrows():
    emisi = row['Emisi_2024']
    emisi_list.append(emisi)

batas = 50

for i, emisi in enumerate(emisi_list):
    perusahaan = df.iloc[i]['Nama_Perusahaan']
    if emisi > batas:
        print(f"{perusahaan} kena pajak dengan emisi {emisi} ton!")
    else:
        print(f"{perusahaan} bebas kena pajak dengan emisi {emisi} ton")

```
Output:

![Mengecek kepatuhan pajak](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/status%20pajak%202.png)

#### Query 5: Menyimpan Data Emisi dalam Dictionary

Tujuan: Menyimpan emisi perusahaan dari CSV ke dictionary dengan nama sebagai kunci.

Konsep: Dictionary (Chapter 8), Pandas untuk baca CSV.

Output: Dictionary berisi emisi perusahaan.

```

import pandas as pd

df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')

emisi_dict = {}

for index, row in df.iterrows():

    perusahaan = row['Nama_Perusahaan']

    emisi = row['Emisi_2024']

    emisi_dict[perusahaan] = emisi

print("Data emisi perusahaan: ", emisi_dict)

```

Output:

![data emisi dalam dict](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/emisi%20perusahaan%20dalam%20dictionary.png)

#### Query 6: Deteki Greenwashing dengan Dictionary

Tujuan: Mendeteksi greenwashing dari CSV berdasarkan klaim hijau dan emisi.

Konsep: Dictionary, if-else (Chapter 8, 5), Pandas untuk baca CSV.

Output: Status greenwashing untuk setiap perusahaan.

```

import pandas as pd

df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')

emisi_dict = {}

for index, row in df.iterrows():
    perusahaan = row['Nama_Perusahaan']
    emisi_dict[perusahaan] = {
        'emisi':row['Emisi_2024'],
        'klaim':row['Klaim_Hijau']
    }

for perusahaan, data in emisi_dict.items():
    if data['klaim']== 'ya' and data['emisi']>50:
        print(f"{perusahaan} TERDETEKSI GREENWASHING dengan emisi {data['emisi']} ton")
    else:
        print(f"{perusahaan} tidak terdeteksi greenwashing")

```

Output:

![Deteksi_Greenwashing](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/deteksi%20greenwashing.png)

#### Query 7: Menghitung Pajak Karbon dengan Fungsi

Tujuan: Membuat fungsi untuk menghitung pajak karbon dari CSV.
Konsep: Fungsi, if-else, Pandas untuk Baca CSV.
Outpu: Nilai pajak untuk setiap perusahaan.

```

import pandas as pd

def hitung_pajak(emisi, batas=50, tarif=20000):
    if emisi > batas:
        pajak = (emisi-batas)*tarif
        return pajak
    return 0

df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')

for index, row in df.iterrows():
    perusahaan = row['Nama_Perusahaan']
    emisi = row['Emisi_2024']
    pajak = hitung_pajak(emisi)
    if pajak > 0:
        print(f"{perusahaan} kena pajak karbon Rp {pajak}")
    else:
        print(f"{perusahaan} bebas pajak karbon")

```

Output:

![Menghitung pajak karbon dengan fungsi](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/status%20pajak%203.png)

#### Query 8: Deteksi Greenwashing dengan Fungsi

Tujuan: Membuat Fungsi untuk Mendeteksi Greenwashing dari CSV

Konsep: Fungsi, Dictionary, if-else, Pandas untuk baca CSV.

Output: Status Greenwashing untuk setiap perusahaan.

```

import pandas as pd

def cek_greenwashing(emisi_dict):
    for perusahaan, data in emisi_dict.items():
        if data['klaim'] == 'ya' and data['emisi']>50:
            print(f"{perusahaan} terdeteksi greenwashing dengan emisi {data['emisi']} ton")
        else:
            print(f"{perusahaan} tidak terdeteksi greenwashing.")

df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')

emisi_dict = {}

for index, row in df.iterrows():
    perusahaan = row['Nama_Perusahaan']
    emisi_dict[perusahaan] = {
        'emisi': row['Emisi_2024'],
        'klaim': row['Klaim_Hijau']
    }

cek_greenwashing(emisi_dict)

```

Output:

![Deteksi Greenwashing dengan fungsi](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/deteksi%20greenwashing%203.png)

#### Query 9: Analisi Konflik Lahan dengan Modul

Tujuan: Membuat Modul untuk Menganalisis Risiko Konflik Lahan Proyek PLTS dari CSV

Konsep: Modul, dictionary, if-else, Pandas untuk baca CSV.

Output: Status Risiko untuk Setiap Proyek

```
from konflik_lahan import cek_konflik

import pandas as pd

df = pd.read_csv('C:/EnergiHijau2025/konflik_lahan.csv')
lahan_dict = {}
for index, row in df.iterrows():
    proyek = row['Nama_Proyek']
    lahan_dict[proyek] = {
        'luas':row['Luas_Lahan'],
        'konflik':row['Status_Konflik']
    }

cek_konflik(lahan_dict)

```

Output:

![Analisis konflik lahan dengan modul](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/status%20konflik.png)


#### Query 10: Bar Chart Emisi Perusahaan

Tujuan: Menvisualisasikan Emisi Perusahaan dari CSV dalam Bar Chart

Konsep: Metplotlib, dictionary, Pandas untuk Baca CSV

Output: Bar Chart Emisi Perusahaan dengan Batas Pajak

```

import pandas as pd
import matplotlib.pyplot as plt

def plot_emisi(emisi_dict):
    perusahaan = list(emisi_dict.keys())
    emisi = [data['emisi'] for data in emisi_dict.values()]
    plt.bar(perusahaan, emisi, color = 'green')
    plt.xlabel('Perusahaan')
    plt.ylabel('Emisi(ton CO2)')
    plt.title('Emisi Karbon Perusahaan 2024')
    plt.axhline(y=50, color = 'red', linestyle = '--', label = 'Batas Pajak (50 ton)')
    plt.legend()
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.show()

df = pd.read_csv('C:/EnergiHijau2025/emisi_perusahaan.csv')
emisi_dict = {}
for index, row in df.iterrows():
    perusahaan = row['Nama_Perusahaan']
    emisi_dict[perusahaan] = {'emisi': row['Emisi_2024']}

plot_emisi(emisi_dict)

```

Output:

![Bar Chart Emisi Perusahaan](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/output%20bar.png)

#### Query 11: Pie Chart Distribusi Konflik Lahan

Tujuan: Menvisualisasikan Proporsi Konflik Lahan dari CSV

Konsep: Matplotlib, Dictionary, Pandas untuk Baca CSV

Output: Pie Cart proporsi risiko konflik

```
import pandas as pd
import matplotlib.pyplot as plt

def plot_konflik(lahan_dict):
    risiko = sum(1 for data in lahan_dict.values() if data ['luas'] > 500 or data ['konflik'] == 'ya')
    aman = len(lahan_dict) - risiko
    labels = ['Berisiko', 'Aman']
    sizes = [risiko, aman]
    colors = ['red', 'green']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%' )
    plt.title('Distribusi Risiko Konflik Lahan Proyek PLTS')
    plt.show()

df=pd.read_csv('C:/EnergiHijau2025/konflik_lahan.csv')

lahan_dict = {}

for index, row in df. iterrows():
    proyek = row['Nama_Proyek']
    lahan_dict[proyek] = {
        'luas':row['Luas_Lahan'],
        'konflik':row['Status_Konflik']
    }
plot_konflik(lahan_dict)

```

Output:

![Pie chart distribusi konflik lahan](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/output%20pie.png)

#### Query 12: Line Chart Tren Emisi

Tujuan: Memviualisasikan Tren Emisi Perusahaan dari 2020-2-23 dari CSV

Konsep: Matplotlib, dictionary, Pandas untuk Baca CSV

Tujuan: Line Chart Statistik dan Kenapa Dipilih

```

import pandas as pd
import matplotlib.pyplot as plt

def plot_tren_emisi(emisi_dict):
    tahun = [2020, 2021, 2022, 2023]

    for perusahaan, emisi_list in emisi_dict.items():
        plt.plot(tahun, emisi_list, marker = 'o', label = perusahaan)
    plt.xlabel('Tahun')
    plt.ylabel('Emisi (ton CO2)')
    plt.title('Tren Emisi Karbon Perusahaan 2020-2023')
    plt.axhline(y=50, color = 'red', linestyle = '--', label = 'Batas Pajak(50 ton)' )
    plt.legend(bbox_to_anchor=(1.05,1), loc = 'upper left')
    plt.tight_layout()
    plt.show()

df = pd.read_csv('C:/EnergiHijau2025/tren_emisi.csv')

emisi_dict = {}

for index, row in df.iterrows():
    perusahaan = row['Nama_Perusahaan']
    emisi_list = [row['Emisi_2020'], row['Emisi_2021'], row['Emisi_2022'], row['Emisi_2023']]
    emisi_dict[perusahaan] = emisi_list

plot_tren_emisi(emisi_dict)   

```

Output:

![Tren Emisi](https://github.com/Agus-Iskandar-D/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/Weekly-Task_Agus-ID/output%20line.png)


### 💡Kesimpulan dan Saran

**Dari analisis di atas dihasilkan beberapa hal:**
1. Tren menunjukan emisi yang dihasilkan menurun dari 2020 hingga 2023
2. Masih banyak yang melakukan greenwashing
3. 19 dari 31 perusahaan masih menghasilkan emisi di atas batas emisi yang ditentukan
4. 70% Proyek PLTS masih berisiko

**Saran untuk stakeholder agar transisi hijau di Indonesia efektif dan efisien:**
1. Monitoring dan evaluasi terhadap kepatuhan perusahaan untuk meminimalisir praktik Granwashing.
2. Mediasi anatara Pemerintah, Masyarakat, dan BUMN yang menjalankan proyek PLTS, serta ahli lingkungan untuk menarai solusi terbaik untuk lingkungan dan masyarakat tanpa mengambaikan kemajuan pembangunan.
3. Menerapkan pajak yang lebih besar namun tidak mengganggu iklim investasi di Indonesia agar emisi yang dihasilkan dari perusahaan bisa diminimalisir.

Semoga bermanfaat🌳

---
