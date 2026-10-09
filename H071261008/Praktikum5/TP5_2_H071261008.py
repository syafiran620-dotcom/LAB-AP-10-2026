ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    daftar = []
    teks = teks.lower()
    kata = kata.lower()
    posisi = teks.find(kata, 0)
    while posisi != -1:
        daftar.append(posisi)
        posisi = teks.find(kata, posisi + 1)
    return daftar

def cek_batas_kata(teks, i, panjang):
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False
    if i + panjang < len(teks) and teks[i + panjang].lower() in ALFABET:
        return False
    return True

def sensor_kata(teks, kata, simbol):
    hasil = ""
    awal = 0
    indeks = []
    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, len(kata)):
            hasil = hasil + teks[awal:i] + simbol * len(kata)
            print(hasil)
            awal = i + len(kata)
            indeks.append(i)
    hasil = hasil + teks[awal:]
    return (hasil, len(indeks), indeks)

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)