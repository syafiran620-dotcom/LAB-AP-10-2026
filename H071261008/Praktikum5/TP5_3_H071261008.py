ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    posisi = ALFABET.find(ch.lower())
    if posisi == -1:                       
        return ch
    posisi_baru = (posisi + k) % 26        
    huruf_baru = ALFABET[posisi_baru]
    if ch == ch.upper():                   
        return huruf_baru.upper()
    return huruf_baru.lower()


def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil = hasil + cek_sandi(ch, k)
    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

xyzabc = "markas"

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        kandidat = mesin_dekripsi(sandi, k)
        print(kandidat)
        if kandidat.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, kandidat))
    return hasil


sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")
print()
print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))