# Analisis-Transisi-Energi-Hijau-2025-di-Indonesia

Nama: Agus iskandar Darmawan

No Absen: 09.009.DB2025

Week Task

## Analisis Transisi Hijau

### Pendahuluan

Indonesia mengejar target ambisius, yaitu 23% energi terbarukan pada 2025. Namun, Data Kementerian ESDM menunjukkan kita baru mencapai 12% energi terbarukan pada 2023, jauh dari target. 

Pemerintah menerapkan pajak karbon untuk kurangi emisi industri, seperti di sektor tekstil Jawa Barat. Tapi, masih banyak perusahaan melakukan greenwashing, yakni mengklaim ramah lingkungan padahal emisinya tinggi. Hal tersebut menyesatkan investor. Selain itu, di Jawa Tengah dan Sulawesi Selatan, proyek PLTS juga sering memicu konflik lahan dengan petani dan masyarakat adat. 

Permasalahan tersebut butuh solusi cerdas. Dengan menggunakan Python, perhitungan pajak karbon, deteksi greenwashing, dan analisis risiko konflik lahan bisa dibuat. Dari hasil analisi yang didapatkan, akan dihasilkan saran untuk pemerintah agar investasi energi hijau lancar dan konflik minim.

### Permasalahan

Transisi energi hijau 2025 di Indonesia menghadapi tiga masalah utama. Pertama, data emisi perusahaan sering tidak akurat, menyulitkan penerapan pajak karbon, terutama di industri tekstil Jawa Barat. Kedua, greenwashing merajalela. Banyak perusahaan mengklaim hijau, tapi emisinya melebihi batas. KLHK melaporkan 25% klaim hijau tidak terverifikasi. 

Ketiga, konflik lahan menghambat proyek PLTS. Di Jawa Tengah, lahan sawah petani diambil untuk PLTS, memicu 800 konflik lahan pada 2023, menurut WALHI. Ini menghalangi investasi energi hijau dan merugikan komunitas lokal. Tanpa analisis data yang solid, pemerintah kesulitan membuat kebijakan efektif. Kita akan pakai Python untuk menghitung pajak karbon, mendeteksi greenwashing, dan mengevaluasi risiko lahan. Solusi ini membantu capai Net Zero Emission 2060 dan mengurangi konflik sosial. 

### Analisis Python

Analisis Python merupakan analisis data menggunakan Python adalah proses mengeksplorasi, membersihkan, mengubah, dan memodelkan data untuk menemukan informasi yang berguna, menarik kesimpulan, dan mendukung pengambilan keputusan. Anaslisis ini Pandas untuk manipulasi dan analisis data tabular, NumPy untuk komputasi numerik, dan Matplotlib visualisasi data.

### Analisis dan Visualisasi Data

Data yang digunakan merupakan data berbentuk CSV yang didapat dari Walhi. Database terdiri dari tiga tabulasi CSV, yakni emisi_perusahaan.csv yang berisi data emisi perusahaan di Jawa Barat, konflik_lahan.csv yang beriisi data konflik lahan PLTS di Indonesia, dan tren_emisi.csv yang berisi tren emisi perusahaan di jawa barat selama 4 tahun, antara 2000-2024.

![emisi_perusahaan]()

![konflik_lahan]()

![tren_emisi]()

#### Mengecek Status Pajak


Tujuan: Mengecek apakah emisi perusahaan dari CSV melebihi batas pajak karbon (50 ton CO2)
Konsep: If-else, Pandas untuk CSV
Output: Status Pajak (kena atau bebas) untuk Setiap Perusahaan

'''

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
        
'''

Pandas untuk cek kepatuhan pajak karbon dari data CSV. Emisi diambil dari emisi_perusahaan.csv, dibandingkan dengan batas 50 ton CO2 (standar sederhana, misalnya Perpres 98/2021), menggunakan If-else untuk menentukan status pajak.

Output:

![Mengecek kepatuhan pajak]()


#### Menghitung Pajak Karbon

Tujuan: Menghitung Pajak Karbon untuk Perusahaan dari CSV Berdasarkan Emisi 2024
Konsep if-else, Pandas untuk baca csv
Output: Nilai Pajak (RP) untuk Setiap Perusahaan

'''

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
  
  '''
   
7. Solusi bantu capai Net Zero Emission 2060.



---

Workshop: Eco Techno Leader - Analisis Transisi Energi Hijau 2025 di Indonesia 🌱💡

Yuk, jadi pionir transisi energi hijau! 🚀✨ Workshop ini bakal kupas tuntas strategi & inovasi energi terbarukan di Indonesia tahun 2025 🌞🌊💨. Kita akan analisis peluang, tantangan, dan solusi buat masa depan rendah karbon 📊🔍.

Apa yang bakal didapat? 🎁:
🔸 Insight kebijakan terbaru pemerintah 📜🇮🇩
🔸 Teknologi hijau terkini (surya, angin, hidro, dll.) ☀️🍃⚡
🔸 Studi kasus sukses & roadmap implementasi 🗺️✅
🔸 Networking dengan ahli & praktisi energi 🌐🤝

Ditunggu partisipasinya! 🎉 Aksi kecil hari ini = dampak besar untuk bumi 🌍💚. Let’s lead the green revolution! ♻️🚀

#EcoTechnoLeader #EnergiHijau2025 #IndonesiaHijau 🌿✨

---

![ROADMAP](https://github.com/arry-hutomo/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/blob/main/ROADMAP.png)

---
🌟✨ SELAMAT DATANG DI STAGE 2: ECO DATA PIONEERS! ✨🌟

Halo, Eco-Techno Leaders masa depan! 🎉🌱 Bersiaplah masuk ke petualangan baru yang seru banget—kita akan jadi pionir data hijau untuk Indonesia yang lebih sustainable! 💚📊

Di stage ini, kita akan:
🔹 Hitung pajak karbon untuk patuhi regulasi 📜💰
🔹 Deteksi greenwashing pakai data emisi 🕵️♂️🌍
🔹 Analisis risiko lahan kurangi konflik sosial ⚖️🚜
🔹 Belajar Python dari dasar sampai pro (if-else sampai modul!) 🐍💻
🔹 Bikin portofolio keren buat usulan ke pemerintah 🏛️✨

Tools yang akan dipakai:
🛠️ Anaconda + VSCode + Jupyter Notebook
📚 Library: Pandas, NumPy, Matplotlib (siap jadi data wizard!)

Tenang! Tutorial ini ramah pemula, langkah demi langkah, pakai data realistis, dan pastinya—dampaknya nyata! 🚀

"Masa depan hijau dimulai dari langkah kecil kita hari ini. Yuk, bersama-sama wujudkan perubahan!" 🌿🙌

Doa & Semangat:
"Semoga ilmu ini jadi berkah, bermanfaat untuk bumi dan sesama. Aamiin! 🤲✨"


📌 Ready to rock? Klik link di bawah untuk mulai petualanganmu!

[NEXT TO STAGES 2](https://arry-hutomo.github.io/Analisis-Transisi-Energi-Hijau-2025-di-Indonesia/)

#EcoDataPioneers #EnergiHijau2025 #PythonForEarth 💡🌎


**ARRY HUTOMO**  
✨ _**Founder • Nawala Integra Nusantara**_ ✨  

---
