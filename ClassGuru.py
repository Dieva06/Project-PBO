from ClassPerson import Person

class guru(Person):
    def __init__(self, PersonID, Nama, Alamat, Usia, JenisKelamin, Bidang, JamKerja, Harga):
        self.Bidang = Bidang
        self.JamKerja = JamKerja
        self.Harga = Harga
        super().__init__(PersonID, Nama, Alamat, Usia, JenisKelamin)
        
    def printGuru(self):
        print('Bidang:', self.Bidang)
        print('JamKerja:', self.JamKerja)
        print('Harga:', self.Harga)

    def set_Bidang(self,Bidang_baru):
        self.Bidang = Bidang_baru
    
    def get_Bidang(self):
        return self.Bidang

    def set_JamKerja(self,JamKerja_baru):
        self.JamKerja = JamKerja_baru
    
    def get_JamKerja(self):
        return self.JamKerja

    def set_Harga(self,Harga_baru):
        self.Harga = Harga_baru
    
    def get_Harga(self):
        return self.Harga

def gaji():
    pass
def ReadGuru():
    pass
