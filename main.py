import sqlite3
import ClassPerson
import ClassGuru as gr
import ClassSiswa as sw
import ClassAdmin 
import ClassKursus 
import ClassDetail

databaseName = 'MyDb.db'

#koneksi ke database
conn = sqlite3.connect(databaseName)
#drop tabel
#conn.execute('drop table Person')
#membuat tabel
conn.execute(
    'CREATE TABLE IF NOT EXISTS Person (PersonID string primary key, Nama string, Alamat string, Usia integer , JenisKelamin string)'
)
conn.execute(
    'CREATE TABLE IF NOT EXISTS guru (PersonID string primary key, Nama string, Alamat string, Usia int, JenisKelamin string, Bidang string, JamKerja string, Harga string)'
)
conn.execute(
    'CREATE TABLE IF NOT EXISTS siswa (PersonID string primary key, Nama string, Alamat string, Usia int, JenisKelamin string,  NISN string, Jenjang string)'
)
conn.execute(
    'CREATE TABLE IF NOT EXISTS admin (PersonID string primary key, Nama string, Alamat string, Usia int, JenisKelamin string,  Password string, Shift string)'
)
conn.execute(
    'CREATE TABLE IF NOT EXISTS Detail (JenisPilihan string, HargaPerJam integer, HargaJenis integer, TambahJamBelajar integer, PersonID string, KursusID string)'
)
conn.execute(
    'CREATE TABLE IF NOT EXISTS Kursus (KursusID string primary key, Jenis string, HargaJenis integer)'
)

Kursus1 = [
    ClassKursus.Kursus("1", "Python", 200000),
    ClassKursus.Kursus("2", "Java", 300000),
    ClassKursus.Kursus("3", "PBO", 500000),
    ClassKursus.Kursus("4", "HTML", 520000)
]

#memasukkan data
for k in Kursus1:
    res = conn.execute('select* from Kursus where KursusID=?', (k.get_KursusID(),))
    if res.fetchone() is None:
        conn.execute('insert into Kursus values(?,?,?)', (k.get_KursusID(), k.get_Jenis(), k.get_HargaJenis()))
        conn.commit()

#membaca data
def ReadKursus():
    cursor = conn.cursor().execute('select* from Kursus')
    for row in cursor:
        print(f'{row[0]}, {row[1]}, {row[2]}')

#membaca data kursus berdasarkan kursusid
def ReadByKursusID(KursusID):
    cursor = conn.cursor().execute('select* from Kursus where KursusID=?',(KursusID,))
    for row in cursor:
        print(f'{row[0]}, {row[1]}, {row[2]}')

#Update data
def UpdateByKursusID(Jenis,KursusID):
    conn.execute('update Kursus set Jenis=? where KursusID=?', (Jenis,KursusID))
    conn.commit()
#UpdateByKursusID('SQL','3')
#ReadKursus()
#Detail
def TampilkanDetail():
    JenisPilihan = input('Jenis pilihan: ')
    HargaPerJam = input('Harga per jam: ')
    HargaJenis = input('Harga jenis: ')
    TambahJamBelajar = input('Tambah jam belajar: ')
    PersonID = input('PersonID: ')
    KursusID = input('KursusID: ')
    conn.execute('INSERT INTO Detail(JenisPilihan, HargaPerJam, HargaJenis, TambahJamBelajar, PersonID, KursusID) VALUES ("'+JenisPilihan+'", "'+HargaPerJam+'", "'+HargaJenis+'", "'+TambahJamBelajar+'", "'+PersonID+'", "'+KursusID+'")')
    conn.commit()


def TotalHarga():
    TambahJamBelajar = int(input('TambahJamBelajar: '))
    HargaPerJam = int(input('HargaPerJam: '))
    HargaJenis = int(input('HargaJenis: '))
    TotalHarga = int
    TotalHarga = (TambahJamBelajar* HargaPerJam) + HargaJenis
    print('TotalHarga', TotalHarga)

#TotalHarga()
Guru1 =[
    gr.guru("G1","Mike", "Jl.Mawar", 20, "Laki-laki", "Python", "2 jam", "50000"),
    gr.guru("G2","ali", "Jl.gajah", 23, "Laki-laki", "Java", "2 jam", "50000"),
    
]

Siswa1 =[
    sw.siswa("S1", "Nina", "Jl.Jawa", 16, "Perempuan", "0065289754", "SMA"),
    sw.siswa("S2", "Andi", "Jl.Sumatra", 17, "Laki-Laki", "0043296349", "SMA"),
] 
#memasukkan data guru
for gu in Guru1:
    res = conn.execute("select * from guru where PersonID =? ", (gu.get_PersonID(),))
    if res.fetchone() is None:
        conn.execute('INSERT INTO guru(PersonID, Nama, Alamat,Usia, JenisKelamin, Bidang, JamKerja, Harga) VALUES (?,?,?,?,?,?,?,?)', (gu.get_PersonID() , gu.get_Nama(), gu.get_Alamat(), gu.get_Usia(), gu.get_JenisKelamin(), gu.get_Bidang(), gu.get_JamKerja(), gu.get_Harga()))
        conn.commit()

#membaca data guru
def ReadGuru():
    cursor = conn.cursor().execute('select* from guru')
    for row in cursor:
        print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}')
#ReadGuru()

def readByID(PersonID):
    cursor = conn.cursor().execute("select * from guru where PersonID= ?", (PersonID,))
    for row in cursor:
        print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}')

def deleteByID(PersonID):
    conn.execute("delete from guru where PersonID= ?", (PersonID,))
    conn.commit()

#Tambah Guru():
def tambahGuru():
    PersonID = input('Masukkan personID: ')
    Nama = input('Masukkan Nama Guru : ')
    Alamat = input('Alamat Guru : ')
    Usia = input('Usia Guru : ')
    JenisKelamin = input('Jenis Kelamin guru:')
    Bidang = input('Bidang Guru: ')
    JamKerja = input('Jam Kerja Guru: ')
    Harga = input('masukkan harga per jam:')
    conn.execute('INSERT INTO guru(PersonID, Nama, Alamat, Usia, JenisKelamin, Bidang, JamKerja, Harga) VALUES ("'+PersonID+'", "'+Nama+'","'+Alamat+'", '+Usia+', "'+JenisKelamin+'", "'+Bidang+'", "'+JamKerja+'", "'+Harga+'")')
    conn.commit()

#tambahGuru()
def gaji():
    JamKerja= int(input("masukkan lama Kerja: "))
    Harga= int(input('masukkan harga guru:'))
    tambahJam = int(input('masukkan tambahan jam:'))
    hargaTambah = int(input('masukkan harga tambah jam:'))
    gaji = int
    gaji= (JamKerja* Harga) + (tambahJam* hargaTambah)
    print("Gaji = ", gaji)

#memasukkan data siswa
for si in Siswa1:
    res = conn.execute("select * from siswa where PersonID =? ", (si.get_PersonID(),))
    if res.fetchone() is None:
        conn.execute('INSERT INTO siswa(PersonID, Nama, Alamat,Usia, JenisKelamin, NISN, Jenjang) VALUES (?,?,?,?,?,?,?)', (si.get_PersonID() , si.get_Nama(), si.get_Alamat(), si.get_Usia(), si.get_JenisKelamin(), si.get_NISN(), si.get_Jenjang()))
        conn.commit()

#membaca data guru
def ReadSiswa():
    cursor = conn.cursor().execute('select* from siswa')
    for row in cursor:
        print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')

#ReadSiswa()
# Menambah data siswa
def tambahSiswa():
    PersonID = input('Masukkan personID: ')
    Nama = input('Masukkan Nama Siswa : ')
    Alamat = input('Alamat Siswa : ')
    Usia = input('Usia Siswa : ')
    JenisKelamin = input('Jenis Kelamin Siswa:')
    NISN = input('NISN siswa: ')
    Jenjang = input('Jenjang Pendidikan: ')
    conn.execute('INSERT INTO siswa(PersonID, Nama, Alamat, Usia, JenisKelamin,NISN, Jenjang) VALUES ("'+PersonID+'", "'+Nama+'","'+Alamat+'", '+Usia+', "'+JenisKelamin+'", "'+NISN+'", "'+Jenjang+'")')
    conn.commit()

#tambahSiswa()
def readIDSiswa(PersonID):
    cursor = conn.cursor().execute("select * from siswa where PersonID= ?", (PersonID,))
    for row in cursor:
        print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')

def deleteIDSiswa(PersonID):
    conn.execute("delete from siswa where PersonID= ?", (PersonID,))
    conn.commit()

def tambahAdmin():
    PersonID = input('Masukkan personID: ')
    Nama = input('Masukkan Nama Admin : ')
    Alamat = input('Alamat Admin : ')
    Usia = input('Usia Admin : ')
    JenisKelamin = input('Jenis Kelamin Admin:')
    Password = input('Password Admin: ')
    Shift = input('Shift Admin: ')
    conn.execute('INSERT INTO admin(PersonID, Nama, Alamat, Usia, JenisKelamin, Password, Shift) VALUES ("'+PersonID+'", "'+Nama+'","'+Alamat+'", '+Usia+', "'+JenisKelamin+'", "'+Password+'", "'+Shift+'")')
    conn.commit()

def updateAdmin(PersonID, Shift):
    conn.execute("update Admin set Shift= ? where PersonID= ?",(PersonID,Shift)) 
    conn.commit()


ulang = True
def menu():
    pilih = int(input('''
    ==========PILIHAN MENU==========
    1. Tampilkan Data Kursus
    2. Tampilkan Data Siswa
    3. Tampilkan Data Guru
    4. Daftar
    ================================
    Masukkan pilihan(1/2/3/4): '''
    ))
    if pilih == 1:
        print('Selamat Datang di Halaman Kursus')
        ReadKursus()
    if pilih == 2:
        print('Selamat Datang di Halaman Siswa')
        pilihan = int(input(''' 
        Apa yang ingin anda lakukan?
        1. Tampilkan data siswa
        2. Mencari data siswa
        3. Menghapus data siswa
        pilih : '''))
        if pilihan ==1:
            ReadSiswa()
        if pilihan == 2:
            cari = str(input('masukkan ID data yang akan dicari:'))
            readIDSiswa(cari)
        if pilihan == 3:
            hapus= str(input('Masukkan ID yang akan dihapus:'))
            deleteIDSiswa(hapus)
        #else:
            #print('maaf pilihan anda salah')

    if pilih == 3:
        print('Selamat Datang di Halaman Guru')  
        pilih2 = int(input(''' 
        Apa yang ingin anda lakukan?
        1. Tampilkan data guru
        2. Menambah data
        3. Mencari data
        4. Menghapus data
        5. Gaji 
        pilih : '''))
        if pilih2 ==1:
            ReadGuru()
        if pilih2 == 2:
            tambahGuru()
        if pilih2 == 3:
            cari = str(input('masukkan ID data yang akan dicari:'))
            readByID(cari)
        if pilih2 == 4:
            hapus= str(input('Masukkan ID yang akan dihapus:'))
            deleteByID(hapus)
        if pilih2 == 5:
            gaji()
        #else:
            #print('maaf pilihan anda salah')
    if pilih == 4:
        print('Selamat Datang di Halaman Pendaftaran')
        Pilihan2= int(input('''
        1. Mendaftar
        2. Cek Biaya '''))
        if Pilihan2 == 1:
            tambahSiswa()
            TampilkanDetail()
        if Pilihan2 == 2:
            TotalHarga()   
   # else:
    #    print("Maaf data yang anda masukkan salah")
#menu()
while ulang == True:
    menu()
    inputUser= input('Ulang lagi? (y/n:)?')
    if inputUser == 'y':
        ulang == True
    else:
        ulang == False
        break

#menutup koneksi
conn.close()
