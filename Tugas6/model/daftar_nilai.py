daftar = {}

def tambah_daftar(nama, nim, tugas, uts, uas):
    a = tugas * 30 / 100
    b = uts * 35 / 100
    c = uas * 35 / 100
    akhir = a + b + c
    daftar[nama] = [nama, nim, tugas, uts, uas, akhir]

def ubah_daftar(nama):
    print("\nUbah data ")
    if nama in daftar.keys():
        del daftar[nama]
        from view.input_nilai import tambah
        tambah()

    else:
        print("Data {} tidak ditemukan ".format(nama))

def cari_daftar(nama):
    if nama in daftar.keys():
        print("\n_____________________________________________________________________")
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("|____________________________________________________________________|")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(nama, daftar[nama][1], daftar[nama][2], daftar[nama][3], daftar[nama][4], daftar[nama][5]))
        print("|____________________________________________________________________|")
    else:
        print("Data {} tidak ditemukan ".format(nama))


def hapus_daftar(nama):
    if nama in daftar.keys():
        del daftar[nama]
        return True
    else:
        print("Data {} tidak ditemukan ".format(nama))
        return False