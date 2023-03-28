```mermaid

---
title: Rajattu Monopoli
---

classDiagram
    Pelinappulat <-- Pelaajat
    Ruudut <-- Pelinappulat
    Ruudut <-- Pelilauta
    Noppa1 <-- Pelaajat
    Noppa2 <-- Pelaajat

    class Noppa1{
        luku : int 1-6
    }
    class Noppa2{
        luku : int 1-6
    }
    class Pelaajat{
        id : int 2-8
        heita_noppaa(Noppa1, Noppa2) int
        liiku_silmälukujen_verran(Pelinappulat)
    }
    class Pelilauta
    class Ruudut{
        id : int 0-40
        seuraava : int id + 1 
    }
    class Pelinappulat{
        id : Pelaajat id
        ruutu : int 0-40
    }