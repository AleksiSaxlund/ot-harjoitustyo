# Homebrewing Calculator

## Dokumentaatio

- [tyoaikakirjanpito.md](./harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)
- [changelog.md](./harjoitustyo/dokumentaatio/changelog.md)
- [vaativuusmaarittely.md](./harjoitustyo/dokumentaatio/vaativuusmaarittely.md)
- [arkkitehtuuri.md](./harjoitustyo/dokumentaatio/arkkitehtuuri.md)

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