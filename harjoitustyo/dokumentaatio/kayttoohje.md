# Käyttöohje

Aloita lataamalla viimeisimmän [releasen](https://github.com/AleksiSaxlund/ot-harjoitustyo/releases) lähdekoodi.

## Ohjelman käynnistäminen

Ensimmäisellä käynnistyskerralla asenna riippuvuudet komennolla:

```
poetry install
```

Ohjelma ei vaadi erillistä konfigurointia. Voit käynnistää sen suoraan komennolla:

```
poetry run invoke start
```

## Huomioitavaa

Ohjelma ei toimi, jos */src/* tai */data/* hakemistojen sisällä olevia tiedostoja poistetaan, tai niiden nimiä muutetaan.

## Ohjelman käyttäminen

Sovellus aukeaa suoraan reseptinsuunnittelu näkymään:

![](./images/picture1.png)

Uusia ainesosia voi lisätä reseptiin pudotusvalikoista:

![](./images/picture2.png)

Ainesosia voi etsiä kirjoittamalla ainesosan nimi pudotusvalikkoon:

![](./images/picture3.png)

Ainesosien määriä voi muuttaa kirjoittamalla uuden määrän pudotusvalikon viereiseen tekstikenttään:

![](./images/picture4.png)

Uusia ainesosia voi lisätä painamalla "Add new" nappia: 

![](./images/picture5.png)

Ainesosat voi poistaa painamalla pudotusvalikon oikeanpuolista "Remove" nappia:

![](./images/picture6.png)

Reseptin kokoa voi muuttaa kirjoittamalla uuden määrän "Volume:" otsikon alapuolella olevaan tekstikenttään:

![](./images/picture7.png)

Kuten kuvista huomaa, reseptille lasketut arvot muuttuvat jokaisen muutoksen jälkeen vastaamaan uusia arvoja.
