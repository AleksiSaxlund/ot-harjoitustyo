# Homebrewing Calculator

Homebrewing Calculator on sovellus, jonka avulla oluen kotipanemista harrastava voi suunnitella reseptejä. Sovelluksella voi lisätä reseptiin ainesosia ja se laskee aina ainesosien muuttuessa eri arvoja, jotka auttavat reseptin suunnittelussa.

## Dokumentaatio

- [tyoaikakirjanpito.md](./harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)
- [changelog.md](./harjoitustyo/dokumentaatio/changelog.md)
- [vaativuusmaarittely.md](./harjoitustyo/dokumentaatio/vaativuusmaarittely.md)
- [arkkitehtuuri.md](./harjoitustyo/dokumentaatio/arkkitehtuuri.md)

## Asennusohjeet:

Suorita komento `poetry install` /harjoitustyo/ kansiossa. Tämän jälkeen sovellus käynnistyy `poetry run invoke start` komennolla.

## Komentorivitoiminnot

### Ohjelman käynnistys:

	poetry run invoke start

### Ohjelman käynnistys GUI:n kanssa:
HUOM. Vain rajallinen toimivuus

    poetry run invoke start-gui

### Testien suoritus:

    poetry run invoke test

### Testien kattavuus:

    poetry run invoke coverage-report

### Pylint tarkastus:

    poetry run invoke lint
