def cek_konflik(lahan_dict):
    for proyek, data in lahan_dict.items():
        if data['luas']> 500 or data['konflik'] == 'ya':
            print(f"Proyek {proyek} berisiko konflik lahan")
        else:
            print(f"Proyek {proyek} aman dari konflik")