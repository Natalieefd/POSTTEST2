'''
!!catatan!!
Buatlah Program sederhana tentang data Mahasiswa dengan
minimal 5 variabel inputan. contoh
1. Nama
2. Nim
3. dan seterusnya
Gunakan tipe data STR,INT,dan Float (wajib di pakai semua)
Simpan data mahasiswa di dalam list

!!poin plus!!
Memiliki Menu tampilan dan memakai dictionary
'''

from judul_menu_data_mahasiswa import judul, menu1, exit

nama = []
NIM = []
fakultas = []
prodi = []
matkul = []
kehadiran = []
nilaikehadiran = []


def menu():
    print("                MENU                  ")
    print("--------------------------------------")
    print(" [1] Tambah Data Mahasiswa")
    print(" [2] Lihat Data Mahasiswa")
    print(" [3] Hapus Data Mahasiswa")
    print(" [4] Exit")
    print("--------------------------------------")
    pil =  int(input("\nPilih Menu: "))

    if pil == 1:
        tambah()
    elif pil == 2:
        lihat()
    elif pil == 3:
        hapus()
    elif pil == 4:
        exit()
    else:
        print('--------------------------------------')
        print("     Pilihan anda tidak tersedia")
        print('--------------------------------------')
        judul()
        menu()

def tambah():
    print("\n--------------------------------------")
    print("       Menambah Data Mahasiswa")
    print("--------------------------------------")
    nama.append (input("Nama: "))
    NIM.append (input("NIM: "))
    fakultas.append (input("Fakultas: "))
    prodi.append (input("Prodi: "))
    matkul.append (input("Mata Kuliah: "))
    kehadiran.append (input("Absen: "))
    nilaikehadiran.append (input("Nilai Kehadiran: "))

    print("\n--------------------------------------")
    print("            Data Tersimpan")
    print("--------------------------------------\n")
    pil = str(input('\n(yes/no)\ningin menambahkan data mahasiswa lagi?'))
    if pil == 'yes':
        tambah()
    elif pil == 'no':
        kembali = input('Back\n[Tekan Enter]')
        judul()
        menu()


def lihat():
    print("\n--------------------------------------")
    print("       Tampilkan Data Mahasiswa")
    print("--------------------------------------")
    print('\nDATA MAHASISWA 1')
    print('Nama            : ', nama[0])
    print('NIM             : ', NIM[0])
    print('Fakultas        : ', fakultas[0])
    print('Prodi           : ', prodi[0])
    print('Mata Kuliah     : ', matkul[0])
    print('Absen           : ', kehadiran[0])
    print('Nilai Kehadiran : ', nilaikehadiran[0])
    
    print('\nDATA MAHASISWA 2')
    print('Nama            : ', nama[1])
    print('NIM             : ', NIM[1])
    print('Fakultas        : ', fakultas[1])
    print('Prodi           : ', prodi[1])
    print('Mata Kuliah     : ', matkul[1])
    print('Absen           : ', kehadiran[1])
    print('Nilai Kehadiran : ', nilaikehadiran[1])

    kembali = input('Back\n[Tekan Enter]')
    judul()
    menu()


def hapus():
    print("\n--------------------------------------")
    print("       Menghapus Data Mahasiswa")
    print("--------------------------------------")
    masnim = input('Masukkan NIM:')
    if masnim == NIM[0]:
        del nama[0]
        del NIM[0]
        del fakultas[0]
        del prodi[0]
        del kehadiran[0]
        del nilaikehadiran[0]
        print('\n--------------------------------------')
        print('         Data sudah terhapus')
        print('--------------------------------------')
        pil = str(input('\n(yes/no)\ningin menghapus data mahasiswa lagi?'))
        if pil == 'yes':
            hapus()
        elif pil == 'no':
            kembali = input('Back\n[Tekan Enter]')
            judul()
            menu()
    elif masnim == NIM[1]:
        del nama[1]
        del NIM[1]
        del fakultas[1]
        del prodi[1]
        del kehadiran[1]
        del nilaikehadiran[1]
        print('\n--------------------------------------')
        print('         Data sudah terhapus')
        print('--------------------------------------')
        pil = str(input('\n(yes/no)\ningin menghapus data mahasiswa lagi?'))
        if pil == 'yes':
            hapus()
        elif pil == 'no':
            kembali = input('Back\n[Tekan Enter]')
            judul()
            menu()
    else:
        print('\n--------------------------------------')
        print('        Data tidak ditemukan')
        print('   Harap masukkan NIM dengan benar')
        print('--------------------------------------')
        hapus()


judul()
menu()
pil =  int(input("\nPilih Menu: "))

if pil == 1:
    tambah()
elif pil == 2:
    lihat()
elif pil == 3:
    hapus()
elif pil == 4:
    exit()
else:
    print('--------------------------------------')
    print("     Pilihan anda tidak tersedia")
    print('--------------------------------------')
    judul()
    menu()