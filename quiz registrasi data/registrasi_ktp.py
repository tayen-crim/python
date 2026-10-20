"""
Registrasi Data ala KTP - versi Terminal (tanpa GUI, tanpa library tambahan)
Jalankan: python registrasi_ktp_terminal.py
"""

from datetime import datetime

LEBAR = 74

AGAMA = ["Islam", "Kristen", "Katolik", "Hindu", "Buddha", "Konghucu"]
GOL_DARAH = ["-", "A", "B", "AB", "O"]
STATUS = ["Belum Kawin", "Kawin", "Cerai Hidup", "Cerai Mati"]
JENIS_KELAMIN = ["LAKI-LAKI", "PEREMPUAN"]
KEWARGANEGARAAN = ["WNI", "WNA"]


# ------------------------------------------------------------------ INPUT
def input_teks(label, wajib=True, default=None):
    while True:
        teks = f"{label}" + (f" [{default}]" if default else "") + " : "
        nilai = input(teks).strip()
        if not nilai and default:
            return default
        if nilai or not wajib:
            return nilai
        print("  ! Tidak boleh kosong.")


def input_nik():
    while True:
        nik = input("NIK (16 digit) : ").strip()
        if nik.isdigit() and len(nik) == 16:
            return nik
        print("  ! NIK harus terdiri dari 16 digit angka.")


def input_tanggal(label):
    while True:
        tgl = input(f"{label} (DD-MM-YYYY) : ").strip()
        try:
            datetime.strptime(tgl, "%d-%m-%Y")
            return tgl
        except ValueError:
            print("  ! Format salah. Contoh: 17-08-1995")


def input_rt_rw():
    while True:
        nilai = input("RT/RW (contoh 001/002) : ").strip()
        bagian = nilai.split("/")
        if len(bagian) == 2 and all(b.isdigit() for b in bagian):
            return f"{int(bagian[0]):03d}/{int(bagian[1]):03d}"
        print("  ! Format salah. Contoh: 001/002")


def input_pilihan(label, pilihan):
    print(f"{label}:")
    for i, p in enumerate(pilihan, 1):
        print(f"  {i}. {p}")
    while True:
        nilai = input("  Pilih nomor : ").strip()
        if nilai.isdigit() and 1 <= int(nilai) <= len(pilihan):
            return pilihan[int(nilai) - 1]
        print(f"  ! Masukkan angka 1 - {len(pilihan)}.")


# ----------------------------------------------------------- ISI FORMULIR
def isi_formulir():
    print("\n" + "=" * LEBAR)
    print("FORMULIR REGISTRASI DATA KTP".center(LEBAR))
    print("=" * LEBAR)

    d = {}
    d["provinsi"] = input_teks("Provinsi", default="SUMATERA UTARA")
    d["kota"] = input_teks("Kota/Kabupaten", default="MEDAN")
    d["nik"] = input_nik()
    d["nama"] = input_teks("Nama Lengkap")
    d["tempat_lahir"] = input_teks("Tempat Lahir")
    d["tgl_lahir"] = input_tanggal("Tanggal Lahir")
    d["jenis_kelamin"] = input_pilihan("Jenis Kelamin", JENIS_KELAMIN)
    d["gol_darah"] = input_pilihan("Golongan Darah", GOL_DARAH)
    d["alamat"] = input_teks("Alamat")
    d["rt_rw"] = input_rt_rw()
    d["kel_desa"] = input_teks("Kelurahan/Desa")
    d["kecamatan"] = input_teks("Kecamatan")
    d["agama"] = input_pilihan("Agama", AGAMA)
    d["status"] = input_pilihan("Status Perkawinan", STATUS)
    d["pekerjaan"] = input_teks("Pekerjaan")
    d["kewarganegaraan"] = input_pilihan("Kewarganegaraan", KEWARGANEGARAAN)
    d["berlaku"] = input_teks("Berlaku Hingga", default="SEUMUR HIDUP")
    return d


# ----------------------------------------------------------- TAMPILAN KTP
def baris(teks=""):
    """Satu baris di dalam kotak kartu."""
    return "║ " + teks.ljust(LEBAR - 4) + " ║"


def tampilkan_ktp(d):
    garis_atas = "╔" + "═" * (LEBAR - 2) + "╗"
    garis_tengah = "╟" + "─" * (LEBAR - 2) + "╢"
    garis_bawah = "╚" + "═" * (LEBAR - 2) + "╝"

    def item(label, isi):
        return baris(f"{label:<19}: {isi}")

    print("\n" + garis_atas)
    print("║" + f"PROVINSI {d['provinsi'].upper()}".center(LEBAR - 2) + "║")
    print("║" + f"KOTA {d['kota'].upper()}".center(LEBAR - 2) + "║")
    print(garis_tengah)
    print(baris(f"NIK                : {d['nik']}"))
    print(garis_tengah)
    print(item("Nama", d["nama"].upper()))
    print(item("Tempat/Tgl Lahir", f"{d['tempat_lahir'].upper()}, {d['tgl_lahir']}"))
    print(item("Jenis Kelamin", f"{d['jenis_kelamin']}   Gol. Darah: {d['gol_darah']}"))
    print(item("Alamat", d["alamat"].upper()))
    print(item("   RT/RW", d["rt_rw"]))
    print(item("   Kel/Desa", d["kel_desa"].upper()))
    print(item("   Kecamatan", d["kecamatan"].upper()))
    print(item("Agama", d["agama"].upper()))
    print(item("Status Perkawinan", d["status"].upper()))
    print(item("Pekerjaan", d["pekerjaan"].upper()))
    print(item("Kewarganegaraan", d["kewarganegaraan"]))
    print(item("Berlaku Hingga", d["berlaku"].upper()))
    print(garis_bawah)


# ------------------------------------------------------------------- MAIN
def main():
    while True:
        data = isi_formulir()
        tampilkan_ktp(data)

        lagi = input("\nRegistrasi data lain? (y/n) : ").strip().lower()
        if lagi != "y":
            print("Terima kasih.")
            break


if __name__ == "__main__":
    main()
