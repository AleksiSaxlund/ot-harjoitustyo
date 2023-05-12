# Homebrewing Calculator

Homebrewing Calculator on sovellus, jonka avulla oluen kotipanemista harrastava voi suunnitella reseptejä. Sovelluksella voi lisätä reseptiin ainesosia ja se laskee aina ainesosien muuttuessa eri arvoja, jotka auttavat reseptin suunnittelussa.

## Release

- [release](https://github.com/AleksiSaxlund/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

- [käyttoohje.md](./harjoitustyo/dokumentaatio/kayttoohje.md)
- [tyoaikakirjanpito.md](./harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)
- [changelog.md](./harjoitustyo/dokumentaatio/changelog.md)
- [vaativuusmaarittely.md](./harjoitustyo/dokumentaatio/vaativuusmaarittely.md)
- [arkkitehtuuri.md](./harjoitustyo/dokumentaatio/arkkitehtuuri.md)

## Komentorivitoiminnot

### Ohjelman käynnistys:

	poetry run invoke start

### Testien suoritus:

    poetry run invoke test

### Testien kattavuus:

    poetry run invoke coverage-report

### Pylint tarkastus:

    poetry run invoke lint
