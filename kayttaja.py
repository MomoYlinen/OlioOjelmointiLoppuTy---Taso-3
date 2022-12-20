from tietokanta import KayttajaTaulu

class Kayttaja():
    def __init__(self):
        self.kayttajataulu = KayttajaTaulu()
        
        
    def lisaa_kayttaja_tietokantaan(self):
        self.kayttajataulu.lisaa_tietokantaan(self.nimi,self.salasana,self.tiimi,self.rooli)
        print("Uusi käyttäjä luotu!")
        
    def hae_kayttaja_nimella(self,hae_nimi):
        hae_nimi = self.kayttajataulu.etsi_tietokannasta_nimella(hae_nimi)
        return hae_nimi
           
    def kirjaudu_sisaan(self, nim, sal):
        kirjautuminen = self.kayttajataulu.varmenna_kayttaja(nim,sal)
        if kirjautuminen == False:
            print("Sisäänkirjautuminen epäonnistui")
        else:
            print("Kirjauduttu onnistuneesti!")
            return kirjautuminen
        
    def etsi_tiimi_kavereita(self, etsi_tiimi):
        tulokset = self.kayttajataulu.etsi_tiimi_kaveri(etsi_tiimi)
        return tulokset
    
    def etsi_kaikki_kayttajat(self):
        kaikki_kayttajat = self.kayttajataulu.kaikki_kayttajat()
        return kaikki_kayttajat
    
    def vaihda_tiimi(self,kayttajan_id,tiimi):
        self.kayttajataulu.vaihda_kayttaja_tiimi(kayttajan_id,tiimi)
            

class UusiKayttaja(Kayttaja):
    def __init__(self,nimi,salasana,tiimi,rooli):
        super().__init__()
        self.nimi = nimi
        self.salasana = salasana
        self.tiimi = tiimi
        self.rooli = rooli