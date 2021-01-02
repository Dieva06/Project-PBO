class Kursus:
    def __init__(self, KursusID, Jenis, HargaJenis):
        self.KursusID = KursusID
        self.Jenis = Jenis
        self.HargaJenis = HargaJenis

    def set_KursusID(self,KursusID_baru):
        self.KursusID=KursusID_baru
    
    def get_KursusID(self):
        return self.KursusID

    def set_Jenis(self,Jenis_baru):
        self.Jenis=Jenis_baru
    
    def get_Jenis(self):
        return self.Jenis

    def set_HargaJenis(self,HargaJenis_baru):
        self.HargaJenis=HargaJenis_baru
    
    def get_HargaJenis(self):
        return self.HargaJenis
