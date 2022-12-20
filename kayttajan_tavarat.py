from tietokanta import KayttajanTavaraTaulu

class KayttajanTavarat():
    def __init__(self):
        self.kayttajanTavaraTaulu = KayttajanTavaraTaulu()
        
        
    def hae_tavarat(self):
        kaikki_tavarat = self.kayttajanTavaraTaulu.hae_tavarat_taulusta()
        return kaikki_tavarat
    
    def hae_tavara_nimella(self,tavaran_nimi):
        loytyyko = self.kayttajanTavaraTaulu.hae_tavara_nimella(tavaran_nimi)
        if loytyyko == False:
            return False
        return True
    
    def lisää_tavara_kayttajalle(self, kayttajan_id,tavaran_nimi):
        hae_tavaran_id = self.kayttajanTavaraTaulu.hae_tavaran_id(tavaran_nimi)
        if hae_tavaran_id == False:
            return print("Tavaraa ei voida lisätä")
        self.kayttajanTavaraTaulu.lisaa_tietokantaan_kayttajanTavara(kayttajan_id,hae_tavaran_id)
        
    def hae_kayttajan_tavarat(self,kayttajan_id):
        loydetyt_tavarat = self.kayttajanTavaraTaulu.hae_kayttajan_tavarat_taulusta(kayttajan_id)
        return loydetyt_tavarat
    
    def hae_kayttajan_tavaroiden_arvo(self, kayttajan_id):
        tavaroiden_arvo = self.kayttajanTavaraTaulu.tavaroiden_arvo(kayttajan_id)
        return tavaroiden_arvo
    
    def poista_kayttajan_tavara(self, kayttajan_id,tavaran_nimi):
        hae_tavaran_id = self.kayttajanTavaraTaulu.hae_tavaran_id(tavaran_nimi)
        self.kayttajanTavaraTaulu.poista_kayttajan_tavara_tietokannasta(kayttajan_id,hae_tavaran_id)
        
    def poista_tavara_kayttajanTavaraTaulusta(self, tavaran_id):
        self.kayttajanTavaraTaulu.poista_tavara_taulusta(tavaran_id)