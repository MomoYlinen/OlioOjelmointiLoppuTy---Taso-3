from tietokanta import TavaraTaulu

class Tavarat():
    def __init__(self):
        self.tavaraTaulu = TavaraTaulu()
        
        
    
    def lisaa_tavara_tietokantaan(self, nimi, arvo):
        uniikki = self.tavaraTaulu.etsi_tietokannasta_tavara(nimi)
        if uniikki == False:
            self.tavaraTaulu.lisaa_tietokantaan_tavara(nimi,arvo)
            print("Tavara on lisätty tietokantaan")
        else:
            print("Tavara on jo tietokannassa")
        
    def hae_tavara(self,tavaran_nimi):
        loytyneet = self.tavaraTaulu.etsi_tietokannasta_tavara(tavaran_nimi)
        if loytyneet == False:
            print("Hakemaasi tavaraa ei löytynyt")
        else:
            print(loytyneet)
            
    def hae_tavaran_Id(self,tavaran_nimi):
        tavaranId = self.tavaraTaulu.hae_tavaranId(tavaran_nimi)
        
    def hae_kaikki_tavarat(self):
        kaikki_tavarat = self.tavaraTaulu.hae_kaikki_tavarat()
        return kaikki_tavarat
        
    def poista_tavara_tavaraTaulusta(self, tavaran_id):
        self.tavaraTaulu.poista_tavara(tavaran_id)
        
    def luo_taulut(self):
        self.tavaraTaulu.luo_tietokanta_tavarat()
        self.tavaraTaulu.luo_tietokanta_kayttajat()
        self.tavaraTaulu.luo_tietokanta_kayttajanTavarat()