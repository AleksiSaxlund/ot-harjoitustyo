```mermaid

---
title: Machine
---

sequenceDiagram
    actor User
    participant Machine
    participant FuelTank
    participant Engine
    User ->> Machine: Machine()
    Activate Machine
    Machine ->> FuelTank: FuelTank()
    activate FuelTank
    FuelTank -->> Machine: ""
    deactivate FuelTank
    Machine ->> FuelTank: fill(40)
    activate FuelTank
    FuelTank -->> Machine: ""
    deactivate FuelTank
    Machine ->> Engine: Engine(FuelTank)
    activate Engine
    Engine -->> Machine: ""
    deactivate Engine
    Machine -->> User: ""
    deactivate Machine
    User ->> Machine: drive()
    activate Machine
    Machine ->> Engine: start()
    activate Engine
    Engine ->> FuelTank: consume(5)
    activate FuelTank
    FuelTank -->> Engine: ""
    deactivate FuelTank
    Engine -->> Machine: ""
    deactivate Engine
    Machine ->> Engine: is_running()
    activate Engine
    Engine ->> FuelTank: _fuel_contents > 0
    activate FuelTank
    FuelTank ->> Engine: True
    deactivate FuelTank
    Engine ->> Machine: True
    deactivate Engine
    Machine ->> Engine: use_energy()
    activate Engine
    Engine ->> FuelTank: consume(10)
    activate FuelTank
    FuelTank -->> Engine: ""
    deactivate FuelTank
    Engine -->> Machine: ""
    deactivate Engine
    Machine -->> User: ""
    deactivate Machine