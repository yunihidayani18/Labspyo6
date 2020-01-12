def tambah():
    from model.daftar_nilai import tambah_daftar
    while True:
        nama = input("Nama   : ")
        if nama == '':
            print('Masukan Nama')
        else:
            break
    while True:
        try:
            nim = int(input("NIM    : "))
            if nim == '':
                print("Masukan NIM")
        except ValueError:
            print("Masukan dengan Angka")
        else:
            break
    while True:
        try:
            tugas = int(input("Tugas  : "))
            if tugas == '':
                print('Masukan Nilai Tugas')
        except ValueError:
            print('Masukan dengan Angka')
        else:
            break
    while True:
        try:
            uts = int(input("UTS    : "))
            if uts == '':
                print('Masukan Nilai UTS ')
        except ValueError:
            print('Masukan dengan Angka')
        else:
            break
    while True:
        try:
            uas = int(input("UAS    : "))
            if uas == '':
                print('Masukan Nilai UAS')
        except ValueError:
            print('Masukan dengan Angka')
        else:
            break
    tambah_daftar(nama, nim, tugas, uts, uas)
def ubah():
    from model.daftar_nilai import ubah_daftar
    ubah_daftar(nama=input("Masukan Nama : "))

def hapus():
    from model.daftar_nilai import hapus_daftar
    hapus_daftar(nama=input("Masukan nama : "))

def cari():
    from model.daftar_nilai import cari_daftar
    cari_daftar(nama=input("Masukan nama : "))