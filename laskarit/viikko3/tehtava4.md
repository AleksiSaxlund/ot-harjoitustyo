```mermaid

---
title: HSL
---

sequenceDiagram
    actor main
    participant laitehallinto
    participant rautatietori
    participant ratikka6
    participant bussi244
    participant lippu_luukku
    participant uusi_kortti
    
    main ->> laitehallinto: HKLLaitehallinto()
    laitehallinto -->> main: ""
    main ->> rautatietori: Lataajalaite()
    rautatietori -->> main: ""
    main ->> ratikka6: Lukijalaite()
    ratikka6 -->> main: ""
    main ->> bussi244: Lukijalaite()
    bussi244 -->> main: ""
    main ->> laitehallinto: lisaa_lataaja(rautatietori)
    activate laitehallinto
    laitehallinto -->> main: ""
    deactivate laitehallinto
    main ->> laitehallinto: lisaa_lukija(ratikka6)
    activate laitehallinto
    laitehallinto ->> ratikka6: append(ratikka6)
    activate ratikka6
    ratikka6 ->> laitehallinto: ratikka6
    deactivate ratikka6
    laitehallinto -->> main: ""
    deactivate laitehallinto
    main ->> laitehallinto: lisaa_lukija(bussi244)
    activate laitehallinto
    laitehallinto ->> bussi244: append(bussi244)
    activate bussi244
    bussi244 ->> laitehallinto: bussi244
    deactivate bussi244
    laitehallinto -->> main: ""
    deactivate laitehallinto
    main ->> lippu_luukku: Kioski()
    lippu_luukku -->> main: ""
    main ->> lippu_luukku: osta_matkakortti("Kalle")
    activate lippu_luukku
    lippu_luukku ->> kallen_kortti: Matkakortti("Kalle")
    kallen_kortti -->> lippu_luukku: ""
    lippu_luukku -->> main: kallen_kortti
    deactivate lippu_luukku
    main ->> rautatietori: lataa_arvoa(kallen_kortti, 3)
    activate rautatietori
    rautatietori ->> kallen_kortti: kasvata_arvoa(3)
    activate kallen_kortti
    kallen_kortti -->> rautatietori: ""
    deactivate kallen_kortti
    rautatietori -->> main: ""
    deactivate rautatietori
    main ->> ratikka6: osta_lippu(kallen_kortti, 0)
    activate ratikka6
    ratikka6 ->> kallen_kortti: arvo < hinta
    activate kallen_kortti
    kallen_kortti ->> ratikka6: False
    deactivate kallen_kortti
    ratikka6 ->> kallen_kortti: vahenna_arvoa(1.5)
    activate kallen_kortti
    kallen_kortti -->> ratikka6: ""
    deactivate kallen_kortti
    ratikka6 ->> main: True
    deactivate ratikka6
    main ->> bussi244: osta_lippu(kallen_kortti, 2)
    activate bussi244
    bussi244 ->> kallen_kortti: arvo < hinta
    activate kallen_kortti
    kallen_kortti ->> bussi244: True
    deactivate kallen_kortti
    bussi244 ->> main: False
    deactivate bussi244