from view.view_nilai import cetak, main, tidakada
from view.input_nilai import tambah, ubah, hapus, cari
main()
while True:

    a = input("\nL)lihat    T)tambah    U)ubah    H)hapus     C)cari    K)keluar :")

    if a.lower() == 'k':
        print("\n==================== T E R I M A  K A S I H ====================")
        break

    elif a.lower() == 'l':
        cetak()

    elif a.lower() == 't':
        tambah()

    elif a.lower() == 'u':
        ubah()

    elif a.lower() == 'c':
        cari()

    elif a.lower() == 'h':
        hapus()

    else:
        tidakada()