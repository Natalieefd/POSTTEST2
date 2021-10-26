'''
!!catatan!!
Buat    lah program sederhana konversi suhu dengan
menggunakan bahasa pemograman Python. Dengan kriteria
1. Fahrenheit ke Celsius
2. Kelvin ke Celsius
3. Reamur ke Celsius
Gunakan Variabel dan operasi Aritmatika

!!poin plus!!
Memiliki Menu tampilan (Ada Pilihan Keluar dan menghitung kembali)
'''

from judul_menu_konversi_suhu import judul, menu, exit

#fahrenheit ke celcius
def fahrenheit():
    print('\nMengkonversi Fahrenheit ke Celcius')
    print('--------------------------------')
    suhu = float(input("Masukkan suhu awal: "))
    F = ((9 * suhu)/ 5 + 32)
    print(suhu,"F", "=", F,"C")

    pilihan = str(input('\n(yes/no)\nIngin menghitung kembali? \n'))
    if pilihan == "yes":
        judul()
        menu()
        pil = int(input("Masukkan Pilihan: "))
        if pil == 2:
            kelvin()
        elif pil == 3:
            reamur()
    elif pilihan == "no":
        exit()

#kelvin ke celcius
def kelvin():
    print("\nMengkonversi Kelvin ke Celcius")
    print("------------------------------")
    suhu = float(input("Masukkan suhu awal: "))
    K = (suhu + 273.15)
    print(suhu,"K", "=", K,"C")

    pilihan = str(input('\n(yes/no)\nIngin menghitung kembali? \n'))
    if pilihan == ("yes"):
        judul()
        menu()
        pil = int(input("Masukkan Pilihan: "))
        if pil == 1:
            fahrenheit()
        elif pil == 3:
            reamur()
    elif pilihan == ("no"):
        exit()


#reamur ke celcius
def reamur():
    print('\nMengkonversi Reamur Ke Celcius')
    print('--------------------------------')
    suhu = float(input("Masukkan suhu awal: "))
    R = ((5/4) * suhu)
    print(suhu,"R", "=", R,"C")

    pilihan = str(input('\n(yes/no)\nIngin menghitung kembali? \n'))
    if pilihan == ("yes"):
        judul()
        menu()
        pil = int(input("Masukkan Pilihan: "))
        if pil == 1:
            fahrenheit()
        elif pil == 2:
            kelvin()
    elif pilihan == ("no"):
        exit()


judul()
menu()

pill = int(input("contoh > 1/2/3\nMasukkan Pilihan: "))

if pill == 1:
    fahrenheit()
elif pill == 2:
    kelvin()
elif pill == 3:
    reamur()
else:
    exit()