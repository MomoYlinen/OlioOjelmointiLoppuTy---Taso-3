# Olio-ohjelmoinnin lopputyö taso 3
Tämä ohjelma on tehty kurssia oliot ja tietokannat varten. 
'Tehtävänä oli tehdä pelinhallintasysteemi. Alla on kuvaus ohjelmantoiminnoista ja esimerkkiajot.

## Esimerkkiajo

### Kirjautumisvaihtoehdot
Vaihtoehtoina on uuden käyttäjänluonti tai sisäänkirjautuminen.

![sisaankirjautumisvaihdoehdot](OhjelmanAjoKuvat/sisaankirjautumisvaihtoehdot.png)

##### Käyttäjänluonti
Luodaan käyttäjä. Valitaan käyttäjänimi,salasana,rooli ja tiimi. Kaikilla käyttäjilla tulee olla uniikki käyttäjänimi. Ohjelma tarkistaa tämän tietokannasta.

![Uusikayttaja](OhjelmanAjoKuvat/Uusikayttaja.png)

##### Sisäänkirjautuminen
Sisäänkirjautuessa annetaan käyttäjänimi ja salasana. Nämä lähetetään tarkistettavaksi. Jos kirjautumistiedot löytyvät tietokannasta, palautetaan käyttäjän kaikki tiedot.

![sisaankirjautuminen](OhjelmanAjoKuvat/Sisaankirjautuminen.png)

### Päävalikko

![Paavalikko](OhjelmanAjoKuvat/Paavalikko.png)

##### Näytä Tiedot
Sovellus näyttää käyttäjän tunnuksen,roolin ja tiimin.

##### Näytä tiimikaverit
Sovellus näyttää samassa tiimissä olevat pelaajat.

![NaytaTiimisi](OhjelmanAjoKuvat/NaytaTiimisi.png)

##### Vaihda tiimiä
Käyttäjä voi vaihtaa tiimiä. Uusi tiimi tallennetaan tietokantaan ja KäyttäjäPaneeli-olioon.

![VaihdaTiimia](OhjelmanAjoKuvat/VaihdaTiimia.png)

#### Tavaroiden hallinta

![TavaroidenHallinta](OhjelmanAjoKuvat/TavaroidenHallinta.png)

##### Näytä tavarat
Käyttäjä voi tarkastella omia tavaroitaan. Sovellus näyttää myös tavaroiden arvon, yhteenlasketun arvon ja kappalemäärän. Nämä tiedot haetaan tietokannasta.

![NaytaTavarat](OhjelmanAjoKuvat/OmatTavarat.png)

##### Lisää tavara
Käyttäjä voi lisätä itselleen tavaroita, jotka löytyvät tietokannasta. Käyttäjä kirjoittaa tavaran nimen, jos nimi on oikein lisätään tavara käyttäjälle tietokantaan.

![LisaaTavara](OhjelmanAjoKuvat/TavaranLisays.png)

##### Poista tavara
Käyttäjä voi poistaa omia tavaroitaan. Käyttäjä kirjoittaa tavaran nimen, jos nimi on oikein poistetaan tavara käyttäjältä tietokannasta.

![PoistaTavara](OhjelmanAjoKuvat/TavaranPoisto.png)

### Pääkayttajä
Pääkäyttäjä voi luoda tavaroita, poistaa tavaroita, nähdä kaikki tietokannassa olevat tavarat ja pelaajat. Pääkäyttäjä voi myös luoda tietokantaan taulut käyttäjiä,tavaroita ja käyttäjäntavaroita varten.

##### Sisäänkirjautuminen
pääkäyttäjälle pääsee kirjautumaan valitsemalla 9 kirjautumisvaihtoehdoissa. Tämä on piilotettu käyttäjältä. Pääkäyttäjän salasana on "paakayttaja"

#### Järjestelmänhallinta

##### Näytä kaikki tavarat
Näyttää tietokannassa olevat tavarat

##### Näytä kaikki käyttäjät
Näyttää tietokannassa olevat käyttäjät

##### Lisää tavaroita
Pyytää pääkäyttäjää syöttamään tavaran nimen ja arvon, jonka jälkeen tavara lisätään tietokantaan.

##### Poista tavaroita
Pyytää pääkäyttäjää syöttämään tavaran id:n, jonka jälkeen tavara poistetaan. Tavara poistetaan kokonaan tietokannasta, myös käyttäjien tavaroista.

##### Luo taulut
Pääkäyttäjä pystyy tarvittaessa luomaan taulut tietokantaan. Tämä komento ajetaan vain ensimmäisellä kerralla tai, jos taulut puuttuvat jostain syystä.
