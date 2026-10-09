def deteksi_anomali_email(email):
    masalah = []

    if email.count("@") != 1:
        masalah.append("Harus memiliki tepat satu karakter @.")
        return masalah

    indeks_at = email.find("@")
    local = email[:indeks_at]
    domain = email[indeks_at + 1:]

    if local == "" or domain == "":
        masalah.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        masalah.append("Tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        masalah.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if "." not in domain:
        masalah.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        masalah.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        masalah.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return masalah


def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    lebar = terpanjang + 2                       
    garis = "+" + karakter_border * lebar + "+"

    hasil = garis + "\n"
    for email in daftar_email_valid:
        spasi = " " * (terpanjang - len(email))  
        hasil = hasil + "| " + email + spasi + " |\n"
    hasil = hasil + garis
    return hasil


print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
if border == "":
    border = "="
border = border[0]

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []
while True:
    email = input("Masukkan email: ")
    if email.lower() == "tutup":
        break

    masalah = deteksi_anomali_email(email)
    if len(masalah) > 0:
        print(">> Email DITOLAK karena:")
        for m in masalah:
            print("   -", m)
    elif email in daftar_valid:
        print(">> Email DITOLAK karena:")
        print("   - Email sudah terdaftar (Duplikat).")
    else:
        daftar_valid.append(email)
        print(">> Email VALID!")

print()
print("--- HASIL EMAIL VALID ---")
if len(daftar_valid) == 0:
    print("Belum ada email yang valid.")
else:
    print(cetak_daftar(daftar_valid, border))