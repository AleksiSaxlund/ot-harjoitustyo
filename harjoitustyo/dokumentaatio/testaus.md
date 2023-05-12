# Testausdokumentti

Ohjelmistoa on testattu yksikkö- ja integraatiotasolla. Moni luokka on riippuvainen vähintään Entities hakemiston luokista, joten yksikkötesteissä on vähintään ne mukana.


## Testikattavuus

Haarautumakattavuus on 87% käyttöliittymäkerrosta lukuunottamatta.

![testikattavuus](/dokumentaatio/images/coverage_report.png)

## Järjestelmätestaus

Järjestelmätestaus on manuaalisesti käsin suoritettua.

### Asennus

Sovellusta on testatty [käyttöohjeen](/dokumentaatio/kayttoohje.md) opastamalla tavalla Windows 10- sekä Linux ympäristöissä.

### Toiminnallisuuksien testaus

Sovelluksen toiminnallisuudet on testattu syöttämällä virheellisiä, tyhjiä sekä oikeita arvoja syötekenttiin. Sovelluksen laskujen tulokset saattavat olla ajoittain epätarkkoja, mutta se ei johdu siitä, että ohjelmassa olisi virheellistä koodia. Tästä lisää [vaativuusmäärittelyn](/dokumentaatio/vaativuusmaarittely.md) "Ohjelman rajoituksia oluenpanijan näkökulmasta"-osiosta.

## Sovellukseen jääneet tunnetut bugit

- Ainesosia lisätessä niiden oletusmäärä on 0. Tämä määrä pysyy kunnes ainesosan määrä päivitetään vastaavasta syötekentästä.
