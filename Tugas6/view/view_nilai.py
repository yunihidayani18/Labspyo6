from model.daftar_nilai import daftar

def main():
    ("\nL)lihat     T)tambah      U)ubah      H)hapus     C)cari      K)keluar: ")

def tidakada():
    print("Pilih Menu yang Ada ")

def cetak():
    print("\n__________________________________________________________________________")
    print("|                          DAFTAR NILAI MAHASISWA                         |")
    print("|_________________________________________________________________________|")
    print("| NO |      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
    print("|_________________________________________________________________________|")
    no = 1
    for tabel in daftar.values():
        print("|{0:3} | {1:15} | {2:16} | {3:5} | {4:5} | {5:5} | {6:5} |"
              .format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
        print("|_________________________________________________________________________|".format(tabel[0][:6]))
        no += 1
    if daftar == {}:
         print ("|                              TIDAK ADA DATA                             |")
         print ("|_________________________________________________________________________|")