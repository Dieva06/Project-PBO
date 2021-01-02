class Person:
    def __init__(self, PersonID, Nama, Alamat, Usia, JenisKelamin):
        self.PersonId = PersonID
        self.Nama = Nama
        self.Alamat = Alamat
        self.Usia = Usia
        self.JenisKelamin = JenisKelamin

    def TampilkanDataPerson(self):
        print('PersonId: ', self.PersonID)
        print('Nama: ', self.Nama)
        print('Alamat: ', self.Alamat)
        print('Usia: ', self.Usia)
        print('JenisKelamin: ', self.JenisKelamin)

    def set_PersonID(self,PersonID_baru):
        self.PersonID=PersonID_baru
    
    def get_PersonID(self):
        return self.PersonID

    def set_Nama(self,Nama_baru):
        self.Nama=Nama_baru
    
    def get_Nama(self):
        return self.Nama

    def set_Alamat(self,Alamat_baru):
        self.Alamat=Alamat_baru
    
    def get_Alamat(self):
        return self.Alamat

    def set_Usia(self,Usia_baru):
        self.Usia=Usia_baru
    
    def get_Usia(self):
        return self.__Usia

    def set_JenisKelamin(self,JenisKelamin_baru):
        self.__JenisKelamin=JenisKelamin_baru
    
    def get_JenisKelamin(self):
        return self.__JenisKelamin
