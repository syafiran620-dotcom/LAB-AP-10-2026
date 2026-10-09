ALFABET = "abcdefghijklmnopqrstuvwxyz"

C:\Users\LENOVO\Documents\PERT5\Tuprak5\Tugas1.py
def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        if ch.lower() in ALFABET:      
            hasil = hasil + ch        
    return hasil.lower()                


def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)


def inti_palinrome(teks):
    terbaik = ""
    indeks_awal = 0
    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            potongan = teks[i:j]
            simetris, _ = cek_palinrome(potongan)
            if simetris and len(potongan) > len(terbaik):
                terbaik = potongan
                indeks_awal = i
    return {"teks": terbaik, "panjang": len(terbaik), "indeks_awal": indeks_awal}


teks = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(teks)
print()
print("Teks Bersih:", bersih)
print("Output Terharap:", inti_palinrome(bersih))