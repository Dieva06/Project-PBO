from ClassPerson import Person
from ClassGuru import guru


class admin(Person):
    def __init__(self, PersonId, Nama, Alamat, Usia, JenisKelamin, Password , Shift ):
        self.Password = Password
        self.Shift = Shift
        super().__init__(PersonId, Nama, Alamat, Usia, JenisKelamin)

    def set_Password(self,Password_baru):
        self.Password = Password_baru
    
    def get_Password(self):
        return self.Password
    def set_Shift(self,Shift_baru):
        self.Shift = Shift_baru
    
    def get_Shift(self):
        return self.Shift

def tambahGuru():
    pass
def tambahSiswa():
    pass




