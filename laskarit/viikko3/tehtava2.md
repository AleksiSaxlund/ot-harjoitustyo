```mermaid

---
title: Laajennettu Monopoli
---

classDiagram
    Pelinappulat <-- Pelaajat
    Ruudut <-- Pelinappulat
    Ruudut <-- Pelilauta
    Noppa1 <-- Pelaajat
    Noppa2 <-- Pelaajat
    Aloitusruutu <-- Ruudut
    Vankila <-- Ruudut
    Sattuma <-- Ruudut
    Yhteismaa <-- Ruudut
    Asemat <-- Ruudut
    Laitokset <-- Ruudut
    Kadut <-- Ruudut
    note for Ruudut "Millään kahdella ruudulla\nei voi olla sama id"
    Sattumakortti <-- Sattuma
    Yhteismaakortti <-- Yhteismaa
    Toiminto <--> Aloitusruutu
    Toiminto <-->  Vankila
    Toiminto <-->  Asemat
    Toiminto <--> Laitokset
    Toiminto <--> Kadut

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
        rahaa : float
    }
    class Pelilauta
    class Pelinappulat{
        id : Pelaajat.id
        ruutu : int 0-40
    }
    class Ruudut{
        id : int 0-40
        seuraava : int id + 1 
    }
    class Aloitusruutu{
        id : 0
    }
    class Vankila{
        id : 10
    }
    class Sattuma{
        id : 0-40
    }
    class Yhteismaa{
        id : 0-40
    }
    class Asemat{
        id : 0-40
    }
    class Laitokset{
        id : 0-40
    }
    class Kadut{
        id : 0-40
        nimi : String
        omistaja : int Pelaajat.id
        talot : int 0-4
        bool on_hotelli
    }
    class Sattumakortti{
        toiminto : ___
    }
    class Yhteismaakortti{
        toiminto : ___
    }
    class Toiminto{
        toiminto(ruutu_type)
    }