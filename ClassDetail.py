class Detail:
    def __init__(self, JenisPilihan, HargaPerJam, HargaJenis, TambahJamBelajar, PersonID, KursusID):
        self.JenisPilihan = JenisPilihan
        self.HargaPerJam = HargaPerJam
        self.HargaJenis = HargaJenis
        self.TambahJamBelajar = TambahJamBelajar
        self.PersonID = PersonID
        self.KursusID = KursusID

    def TotalHarga(self):
        TotalHarga = (TambahJamBelajar*HargaPerJam) + HargaJenis
        return self.TotalHarga

    def TampilkanDetail(self):
        JenisPilihan = input('Jenis pilihan: ')
        HargaPerJam = input('Harga per jam: ')
        HargaJenis = input('Harga jenis: ')
        TambahJamBelajar = input('Tambah jam belajar: ')
        PersonID = input('PersonID: ')
        KursusID = input('KursusID: ')
        pass