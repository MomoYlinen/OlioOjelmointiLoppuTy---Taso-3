from kayttaja import Kayttaja,UusiKayttaja
from tavarat import Tavarat
from kayttajan_tavarat import KayttajanTavarat

##################################################
# Kurssi: AT00BT78-3005 Oliot ja tietokannat
# Ohjelmanimi: LT-Taso-3
# Tekijä: Momo Ylinen
#
# Vakuutan, että tämä ohjelma on minun tekemä.
# Työhön olen käyttänyt seuraavia lähteitä, sekä
# saanut apua seuraavilta henkilöiltä:
# - Lähde Stackoverflow,Youtube
# 
##################################################

                
class KayttajaPaneeli():
    def __init__(self,id,nimi,tiimi,rooli):
        self.id = id
        self.nimi = nimi
        self.tiimi = tiimi
        self.rooli = rooli
        self.kayttaja = Kayttaja()
        
    def ohjeet(self):
        print("Valikko")
        print("--------")
        print("")
        print("[1] - Näytä tiedot")
        print("[2] - Näytä tiimikaverit")
        print("[3] - Tavaroiden hallinta")
        print("[4] - Vaihda tiimiä")
        print("")
        print("[0] - Kirjaudu ulos")
        
    def mini_ohjeet(self):
        print("Valinnat: [1] - näytä tiedot [2] - näytä tiimikaverit [3] - Tavaroiden hallinta [4] - Näytä käyttäjän tavarat [0] - Kirjaudu ulos")
        print("")
    
    def tervehdys(self):
        print("")
        print(f"Tervetuloa {self.nimi}!!!")
        print("")
        
    
    def näytä_tiimikaverit(self):
        tulokset = self.kayttaja.etsi_tiimi_kavereita(self.tiimi)
        print(f"Sinun tiimisi: {self.tiimi}")
        print("-----------------------------")
        for n in tulokset:
            print(f"Käyttäjänimi: {n[0]} Rooli: {n[1]}")
            
    def vaihda_tiimia(self):
        self.tiimi = self.valitse_tiimi()
        self.kayttaja.vaihda_tiimi(self.id,self.tiimi)
        print(f"Olet nyt tiimissä {self.tiimi}")
    
    def valitse_tiimi(self):
        print("Mihin tiimiin haluat?")
        print("----------------------")
        print("")
        print("[1] - Muskettisoturit")
        print("[2] - Lohikäärmeet")
        print("[3] - Mustat Koobrat")
        print("[4] - Pimeyden Valtiaat")
        print("")
        valinta = "Ei valittu"
        while True:
            try:
                komento = int(input ("Valitse Tiimisi: "))
            except:ValueError
            if komento == 1:
                valinta = "Muskettisoturit"
                break
            elif komento == 2:
                valinta = "Lohikäärmeet"
                break
            elif komento == 3:
                valinta = "Mustat Koobrat"
                break
            elif komento == 4:
                valinta = "Pimeyden Valtiaat"
                break
            print("")
            print("Valitse tiimi!")
            print("")
        return valinta
    
    
    
    def nayta_tiedot(self):
        print("Käyttäjätiedot")
        print("---------------")
        print("")
        print(f"Käyttäjänimi: {self.nimi}")
        print(f"Tiimi: {self.tiimi}")
        print(f"Rooli: {self.rooli}")
        print("")
    
    def suorita(self):
        self.tervehdys()
        self.ohjeet()
        while True:
            komento = int(input("Valinta: "))
            if komento == 0:
                print("Kirjauduttiin ulos")
                break
            elif komento == 1:
                self.nayta_tiedot()
                print("")
                self.mini_ohjeet()   
            elif komento == 2:
                self.näytä_tiimikaverit()
                print("")
                self.mini_ohjeet() 
            elif komento == 3:
                tiedot_tavaran_hallintaan = TavaroidenHallinta(self.id,self.nimi,self.tiimi,self.rooli)
                tiedot_tavaran_hallintaan.suorita()
                self.mini_ohjeet()
            elif komento == 4:
                self.vaihda_tiimia()
            else:
                self.ohjeet()
                
class TavaroidenHallinta(KayttajaPaneeli):
    def __init__(self, id, nimi, tiimi, rooli):
        super().__init__(id, nimi, tiimi, rooli)
        self.kayttajan_tavarat = KayttajanTavarat()
        
    def ohjeet(self):
        print("")
        print("Tavaroiden hallinta")
        print("---------------------")
        print("")
        print("[1] - Näytä tavarat")
        print("[2] - Lisää tavara")
        print("[3] - Poista tavara")
        print("")
        print("[0] - Palaa päävalikkoon")
        print("")
        
    def mini_ohjeet(self):
        print("Valinnat: [1] -> Näytä tavarat [2] -> Lisää tavara [3] -> Poista tavara [0] -> Päävalikko")
        
    def lisaa_tavara(self):
        kaikki_tavarat = self.kayttajan_tavarat.hae_tavarat()
        print("Minkä tavaran haluat lisätä?")
        print("-------------------------")
        for n in kaikki_tavarat:
            print(f"Esine: {n[0]}  Arvo: {n[1]}")
            print("")
        komento = input("Kirjoita lisättävän tavaran nimi: ")
        loytyyko_tavaraa = self.kayttajan_tavarat.hae_tavara_nimella(komento)
        if loytyyko_tavaraa == True:
            self.kayttajan_tavarat.lisää_tavara_kayttajalle(self.id, komento)
            print("Tavara on nyt lisätty!")
            print("")
        else:
            print("")
            print("Tavaraa ei löytynyt. Tarkista, että nimi on oikein!")
            print("")
            print("")
            

    def tavaroiden_arvo(self):
        tavaroiden_arvon_summa = self.kayttajan_tavarat.hae_kayttajan_tavaroiden_arvo(self.id)
        return tavaroiden_arvon_summa
            
            
    def poista_tavara(self):
        hae_kayttajan_tavarat = self.kayttajan_tavarat.hae_kayttajan_tavarat(self.id)
        print("Minkä tavaran haluat poistaa?")
        print("-------------------------")
        for n in hae_kayttajan_tavarat:
            print(f"Esine: {n[0]}")
            print("")
        komento = input("Kirjoita poistettavan tavaran nimi: ")
        self.kayttajan_tavarat.poista_kayttajan_tavara(self.id, komento)
            
                
            
    def nayta_kayttaja_tavarat(self):
        loydetyt = self.kayttajan_tavarat.hae_kayttajan_tavarat(self.id)
        tavaroiden_arvo_ja_maara = self.tavaroiden_arvo()
        print("")
        print("Omat tavarat")
        print("--------------")
        print("")
        for n in loydetyt:
            print(f"Esine: {n[0]} Arvo: {n[1]}")
            print("")
        print(f"Tavaroiden määrä: {tavaroiden_arvo_ja_maara[1]} kpl")
        print(f"Tavaroiden arvo: {tavaroiden_arvo_ja_maara[0]}")
        print("")
    
    def suorita(self):
        self.ohjeet()
        while True:
            try:
                komento = int(input("Valinta: "))
            except: ValueError
            if komento == 0:
                print("Palataan päävalikkoon")
                print("")
                break
            elif komento == 1:
                self.nayta_kayttaja_tavarat()
                self.mini_ohjeet()
            elif komento == 2:
                self.lisaa_tavara()
                print("")
                self.mini_ohjeet()
            elif komento == 3:
                self.poista_tavara()
                print("")
                self.mini_ohjeet()
            else:
                self.ohjeet()
                
   
class Paakayttaja():
    def __init__(self):
        self.kayttajat = Kayttaja()
        self.tavarat = Tavarat()
        self.kayttajan_tavarat = KayttajanTavarat()
        
    def ohjeet(self):
        print("Järjestelmän hallinta")
        print("---------------------")
        print("")
        print("[1] - Näytä kaikki tavarat")
        print("[2] - Näytä kaikki käyttäjät")
        print("[3] - Lisää tavaroita")
        print("[4] - Poista tavaroita")
        print("[5] - Luo taulut")
        print("")

    def nayta_tietokannan_tavarat(self):
        print("Tietokannassa olevat tavarat")
        print("-------------------------------")
        print("")
        kaikki_tavarat = self.tavarat.hae_kaikki_tavarat()
        for n in kaikki_tavarat:
            print(f"ID: {n[0]}  Esine: {n[1]} Arvo: {n[2]}")
        print("")
        
    def nayta_kaikki_kayttajat(self):
        print("Tietokannassa olevat käyttäjät")
        print("-------------------------------")
        print("")
        kaikki_kayttajat = self.kayttajat.etsi_kaikki_kayttajat()
        for n in kaikki_kayttajat:
            print(f"ID: {n[0]}  Nimi: {n[1]} Tiimi: {n[2]} Rooli: {n[3]}")
        print("")   
        
    def lisaa_tavaroita(self):
        print("Lisää tavara")
        print("-------------")
        print("")
        tavaran_nimi = input("Anna tavaran nimi: ")
        tavaran_arvo = int(input("Anna tavaran arvo: "))
        self.tavarat.lisaa_tavara_tietokantaan(tavaran_nimi,tavaran_arvo)
        print("Tavara lisätty!")
        print("")
        
    def luo_taulut(self):
        self.tavarat.luo_taulut()
        print("Taulut luotu!")
    
    def poista_tavaroita(self):
        print("Minkä tavaran haluat poistaa")
        print("------------------------------")
        print("")
        self.nayta_tietokannan_tavarat()
        try:
            komento = int(input("Anna tavaran ID: " ))
        except: ValueError
        self.kayttajan_tavarat.poista_tavara_kayttajanTavaraTaulusta(komento)
        self.tavarat.poista_tavara_tavaraTaulusta(komento)
        print("Tavara on poistettu")
        print("")
    
    def suorita(self):
        self.ohjeet()
        while True:
            komento = int(input("Valinta: "))
            if komento == 0:
                print("Poistutaan")
                print("")
                break
            elif komento == 1:
                self.nayta_tietokannan_tavarat()
                self.ohjeet()
                print("")
            elif komento == 2:
                self.nayta_kaikki_kayttajat()
                print("")
                self.ohjeet()
            elif komento == 3:
                self.lisaa_tavaroita()
                print("")
                self.ohjeet()
                print("")
            elif komento == 4:
                self.poista_tavaroita()
                print("")
                self.ohjeet()
                print("")
            elif komento == 5:
                print("")
                self.luo_taulut()
                self.ohjeet()
            else:
                self.ohjeet()
                print("")
        
        


             
class Main():
    
    def __init__(self):
        self.kayttaja = Kayttaja()
    
    
    def ohjeet(self):
        print("")
        print("Tervetuloa pelisovellukseen")
        print("")
        print("Komennot")
        print("----------------------")
        print("[1] Tee uusi käyttäjä")
        print("[2] Kirjaudu sisään")
        print("")
        print("[0] Lopeta ohjelma")
        print("")
        
    def uusi_kayttaja(self):
        while True:
            kayttajanimi = input("Anna käyttäjänimi: ")
            uniikki_nimi = self.uniikki_käyttäjä_nimi(kayttajanimi)
            if uniikki_nimi == True:
                break
            else:
                print("Käyttäjä nimi on varattu")
        salasana = input("Anna salasana: ")
        tiimi = self.valitse_tiimi()
        rooli = self.valitse_rooli()
        uusi_kayttaja = UusiKayttaja(kayttajanimi,salasana,tiimi,rooli)
        uusi_kayttaja.lisaa_kayttaja_tietokantaan()
        return [kayttajanimi,salasana]
    
    def uniikki_käyttäjä_nimi(self, kayttajanimi):
        uniikki = self.kayttaja.hae_kayttaja_nimella(kayttajanimi)
        return uniikki
    
    def valitse_rooli(self):
        print("Minkä roolin haluat?")
        print("----------------------")
        print("")
        print("[1] - Ritari")
        print("[2] - Noituri")
        print("[3] - Velho")
        print("[4] - Loitsija")
        print("[5] - Örkki")
        print("")
        valinta = "Ei valittu"
        while True:
            try:
                komento = int(input ("Valitse Rooli: "))
            except:ValueError
            if komento == 1:
                valinta = "Ritari"
                break
            elif komento == 2:
                valinta = "Noituri"
                break
            elif komento == 3:
                valinta = "Velho"
                break
            elif komento == 4:
                valinta = "Loitsija"
                break
            elif komento == 5:
                valinta = "Örkki"
                break
            print("")
            print("Valitse rooli")
            print("")
        return valinta
    
    def valitse_tiimi(self):
        print("Mihin tiimiin haluat?")
        print("----------------------")
        print("")
        print("[1] - Muskettisoturit")
        print("[2] - Lohikäärmeet")
        print("[3] - Mustat Koobrat")
        print("[4] - Pimeyden Valtiaat")
        print("")
        valinta = "Ei valittu"
        while True:
            try:
                komento = int(input ("Valitse Tiimisi: "))
            except:ValueError
            if komento == 1:
                valinta = "Muskettisoturit"
                break
            elif komento == 2:
                valinta = "Lohikäärmeet"
                break
            elif komento == 3:
                valinta = "Mustat Koobrat"
                break
            elif komento == 4:
                valinta = "Pimeyden Valtiaat"
                break
            print("")
            print("Valitse tiimi!")
            print("")
        return valinta
        
    def kirjaudu(self):
        kayttajanimi = input("Anna käyttäjänimi: ")
        salasana = input("Anna salasana: ")
        return [kayttajanimi,salasana]

    
    def suorita(self):
        self.ohjeet()
        while True:
            try:
                komento = int(input("Komento: "))
            except:ValueError
            if komento == 0:
                print("Näkemiin!!!")
                break
            elif komento == 1:
                kayttajatunnukset = self.uusi_kayttaja()
                kayttajan_tiedot = self.kayttaja.kirjaudu_sisaan(kayttajatunnukset[0],kayttajatunnukset[1])
                kayttajapaneeli = KayttajaPaneeli(kayttajan_tiedot[0],kayttajan_tiedot[1],kayttajan_tiedot[2],kayttajan_tiedot[3])
                kayttajapaneeli.suorita()
                self.ohjeet()
            elif komento == 2:
                while True:
                    kirjautuminen = self.kirjaudu()
                    kayttajan_tiedot = self.kayttaja.kirjaudu_sisaan(kirjautuminen[0],kirjautuminen[1])
                    if kayttajan_tiedot != None:
                        break
                kayttajapaneeli = KayttajaPaneeli(kayttajan_tiedot[0],kayttajan_tiedot[1],kayttajan_tiedot[2],kayttajan_tiedot[3])
                kayttajapaneeli.suorita()
                self.ohjeet()
                
            elif komento == 9:
                while True:
                    salasana = input("Anna salasana: ")
                    if salasana == "paakayttaja":
                        break
                    print("Salasana on väärin")
                Paakayttaja().suorita()
                self.ohjeet()
                
            else:
                self.ohjeet()
                
                
                
Main().suorita()