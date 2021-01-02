from ClassPerson import Person

class siswa(Person):
    def __init__(self, PersonId, Nama, Alamat, Usia, JenisKelamin, NISN, Jenjang):
        self.NISN = NISN
        self.Jenjang = Jenjang
        super().__init__(PersonId, Nama, Alamat, Usia, JenisKelamin)

    def PrintDataSiswa(self):
        print('NISN: ', self.NISN)
        print('Jenjang: ', self.Jenjang)

    def set_NISN(self,NISN_baru):
        self.NISN = NISN_baru
    
    def get_NISN(self):
        return self.NISN

    def set_Jenjang(self,Jenjang_baru):
        self.Jenjang= Jenjang_baru
    
    def get_Jenjang(self):
        return self.Jenjang

def ReadSiswa():
    pass
