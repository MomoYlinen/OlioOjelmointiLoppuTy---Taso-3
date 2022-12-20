import sqlite3

class Tietokanta():
    def __init__(self):
        self.conn = sqlite3.connect("kanta.db")
        self.curs = self.conn.cursor()
    
    def luo_tietokanta_kayttajat(self):
        with self.conn:
            self.curs.execute("""CREATE TABLE kayttajat (
                id integer,
                nimi text,
                salasana text,
                tiimi text,
                rooli text)""")
            self.conn.commit()
            
    def luo_tietokanta_tavarat(self):
        with self.conn:
            self.curs.execute("""CREATE TABLE tavarat (
                id integer,
                nimi text,
                arvo integer
                )""")
            self.conn.commit()
            
    def luo_tietokanta_kayttajanTavarat(self):
        with self.conn:
            self.curs.execute("""CREATE TABLE kayttajantavarat (
                id integer,
                kayttajan_id integer,
                tavaran_id integer
                )""")
            self.conn.commit()
            
    def poista_poyta(self):
        with self.conn:
            self.curs.execute(" DROP TABLE kayttajantavarat ")
            self.conn.commit()
            
    
            
class KayttajaTaulu(Tietokanta):
    def __init__(self):
        super().__init__()
        
        
    def lisaa_tietokantaan(self,nimi,salasana,tiimi,rooli):
        with self.conn:
            self.curs.execute("SELECT MAX(id) as maxid FROM kayttajat")
            hae_id = (self.curs.fetchone())
            taulu_id = 1
            if hae_id[0] == None:
                taulu_id = 1
            else:
                taulu_id = hae_id[0]
                taulu_id +=1
            self.curs.execute("INSERT INTO kayttajat VALUES (:id,:nimi,:salasana,:tiimi,:rooli)", {'id': taulu_id,'nimi': nimi,'salasana': salasana,'tiimi': tiimi,'rooli': rooli})
            self.conn.commit()
            
            
    def varmenna_kayttaja(self, nimi, salasana):
        with self.conn:
            self.curs.execute("SELECT id,nimi,tiimi,rooli FROM kayttajat WHERE nimi=:nimi and salasana=:salasana ",{'nimi':nimi,'salasana':salasana})
            vastaus = self.curs.fetchone()
            if vastaus == None:
                return False
            else:
                return list(vastaus)
            
    def vaihda_kayttaja_tiimi(self,kayttajan_id,tiimi):
        with self.conn:
            self.curs.execute("UPDATE kayttajat SET tiimi=:tiimi WHERE id=:kayttajan_id",{'tiimi':tiimi, 'kayttajan_id':kayttajan_id})
            self.conn.commit()
            
            
    def etsi_tietokannasta_nimella(self, etsi_nimi):
        with self.conn:
            self.curs.execute("SELECT * FROM kayttajat WHERE nimi=:nimi",{'nimi':etsi_nimi})
            nimet = self.curs.fetchone()
            if nimet == None:
                return True
            else:
                return False
            
    def etsi_tiimi_kaveri(self, etsi_tiimi):
        with self.conn:
            self.curs.execute("SELECT nimi,rooli FROM kayttajat WHERE tiimi=:tiimi",{'tiimi':etsi_tiimi})
            nimet = list(self.curs.fetchall())
            return nimet
            
    def kaikki_kayttajat(self):
        with self.conn:
            self.curs.execute("SELECT * FROM kayttajat")
            kaikki_kayttajat = list(self.curs.fetchall())
            return kaikki_kayttajat
            
            
            
class TavaraTaulu(Tietokanta):
    def __init__(self):
        super().__init__()
        
        
    def lisaa_tietokantaan_tavara(self,nimi,arvo):
        with self.conn:
            self.curs.execute("SELECT MAX(id) as maxid FROM tavarat")
            hae_id = (self.curs.fetchone())
            taulu_id = 1
            if hae_id[0] == None:
                taulu_id = 1
            else:
                taulu_id = hae_id[0]
                taulu_id+=1
            self.curs.execute("INSERT INTO tavarat VALUES (:id,:nimi,:arvo)", {'id': taulu_id,'nimi': nimi,'arvo':arvo})
            self.conn.commit()
            
            
    def etsi_tietokannasta_tavara(self, etsi_nimi):
        with self.conn:
            self.curs.execute("SELECT * FROM tavarat WHERE nimi=:nimi",{'nimi':etsi_nimi})
            loytyneet= list(self.curs.fetchall())
            if len(loytyneet) == 0:
                return False
            else:
                return list(loytyneet)
            
    def hae_kaikki_tavarat(self):
        with self.conn:
            self.curs.execute("SELECT * FROM tavarat")
            loytyneet = list(self.curs.fetchall())
            return loytyneet
        
    def poista_tavara(self, tavaran_id):
        with self.conn:
            self.curs.execute("DELETE FROM tavarat WHERE id = :id", {'id': tavaran_id})
            self.conn.commit()
            
            
class KayttajanTavaraTaulu(Tietokanta):
    def __init__(self):
        super().__init__()
        
        
    def lisaa_tietokantaan_kayttajanTavara(self,kayttajan_id,tavaran_id):
        print("ID: ",kayttajan_id,tavaran_id)
        with self.conn:
            self.curs.execute("SELECT MAX(id) as maxid FROM kayttajantavarat")
            hae_id = (self.curs.fetchone())
            taulu_id = 1
            if hae_id[0] == None:
                taulu_id = 1
            else:
                taulu_id = hae_id[0]
                taulu_id +=1
            self.curs.execute("INSERT INTO kayttajantavarat VALUES (:id,:kayttajan_id,:tavaran_id)", {'id': taulu_id,'kayttajan_id': kayttajan_id,'tavaran_id':tavaran_id})
            self.conn.commit()
            
    def poista_kayttajan_tavara_tietokannasta(self,kayttajan_id, tavaran_id):
        with self.conn:
            self.curs.execute("DELETE FROM kayttajantavarat WHERE kayttajan_id =:kayttajan_id AND tavaran_id = :tavaran_id", {'kayttajan_id': kayttajan_id, 'tavaran_id': tavaran_id})
            self.conn.commit()
            
            
    def hae_tavaran_id(self,tavaran_nimi):
        with self.conn:
            self.curs.execute("SELECT id FROM tavarat WHERE nimi=:nimi",{'nimi':tavaran_nimi})
            haku= (self.curs.fetchone())
            if haku == None:
                return False
            haetunTavaran_id = haku[0]
            return haetunTavaran_id
            
    def hae_tavara_nimella(self,tavaran_nimi):
        with self.conn:
            self.curs.execute("SELECT * FROM tavarat WHERE nimi=:nimi",{'nimi':tavaran_nimi})
            haku = self.curs.fetchall()
            print("Haku:", haku)
            if len(haku) == 0:
                return False
            else:
                return True
            
    def hae_tavarat_taulusta(self):
        with self.conn:
            self.curs.execute("SELECT nimi,arvo FROM tavarat")
            haku= list(self.curs.fetchall())
            return haku
        
    def hae_kayttajan_tavarat_taulusta(self, kayttajan_id):
        with self.conn:
            self.curs.execute("SELECT tavarat.nimi, tavarat.arvo FROM tavarat JOIN kayttajantavarat ON kayttajantavarat.tavaran_id = tavarat.id  WHERE kayttajantavarat.kayttajan_id =:kayttajan_id", {'kayttajan_id': kayttajan_id})
            loydetyt_tavarat = list(self.curs.fetchall())
            return loydetyt_tavarat
        
    def poista_tavara_taulusta(self,tavaran_id):
        with self.conn:
            self.curs.execute("DELETE FROM kayttajantavarat WHERE tavaran_id =:tavaran_id", {'tavaran_id':tavaran_id})
            self.conn.commit()
            
    def tavaroiden_arvo(self, kayttajan_id):
        with self.conn:
            self.curs.execute("SELECT SUM(tavarat.arvo) FROM tavarat JOIN kayttajantavarat ON kayttajantavarat.tavaran_id = tavarat.id  WHERE kayttajantavarat.kayttajan_id =:kayttajan_id", {'kayttajan_id': kayttajan_id})
            tavarat_arvo = (self.curs.fetchone())
            self.curs.execute("SELECT COUNT(tavarat.arvo) FROM tavarat JOIN kayttajantavarat ON kayttajantavarat.tavaran_id = tavarat.id  WHERE kayttajantavarat.kayttajan_id =:kayttajan_id", {'kayttajan_id': kayttajan_id})
            tavarat_maara = (self.curs.fetchone())
            if tavarat_arvo[0] == None:
                return [0,0]
            else:
                return [tavarat_arvo[0],tavarat_maara[0]]
            