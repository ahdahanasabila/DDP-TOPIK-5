kendaraan = ["Avanza", "kendaraan darat", "1200", "hitam", "4"]
kendaraan.append("350.000.000")
kendaraan.append("Avanza Transformer")
kendaraan.insert(1,"Toyota")
print(kendaraan)

def hitung_luas_bangun_datar(pilihan):
    match pilihan:
        case 1:
            sisi = int(input("Masukkan panjang sisi persegi: "))
            luas = sisi * sisi
            print(f"Luas persegi adalah {luas}")
        case 2:
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = 3.14 * jari_jari ** 2
            print(f"Luas lingkaran adalah {luas}")
        case 3:
            alas = int(input("Masukkan alas segitiga: "))
            tinggi = int(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga adalah {luas}")
        case _:
            print("Pilihan tidak valid")

pilihan = int(input("Pilih bangun datar (1: Persegi, 2: Lingkaran, 3: Segitiga): "))
hitung_luas_bangun_datar(pilihan)