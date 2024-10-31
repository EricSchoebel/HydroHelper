# HydroHelper
## Automatisierte Pflanzenbewässerung 

von Eric Schöbel

FIXME

**HydroHelper** automatisiert die Pflanzenbewässerung mithilfe eines Raspberry Pi und einer API zur Wetterabfrage. Für Balkonpflanzen wird täglich der Wetterbericht über eine API abgerufen, und je nach Temperatur und Niederschlag wird entschieden, ob die Pflanzen bewässert werden sollen. Für Innenpflanzen erfolgt die Bewässerung ohne Wetterabfrage.


**Features**

 + Innenbewässerung: Tägliche, automatische Bewässerung einer festgelegten Dauer.
 + Außenbewässerung mit Wetterabhängigkeit:
    ++ Abruf der täglichen Wetterdaten (Temperatur und Niederschlag)
    ++ Keine Bewässerung bei Niederschlag
    ++ Bewässerung ab 20°C oder alle drei Tage bei niedrigeren Temperaturen
 + Dateibasierte Speicherung der letzten Bewässerung für eine adaptive Bewässerung nach Temperatur- und Zeitkriterien


**Anwendung**

Das Projekt basiert auf Python und wird über einen Raspberry Pi Modell B+ ausgeführt. Zwei Skripte – eins für die Innen- und eins für die Außenbewässerung – zur Bedienung der Wasserpumpe werden täglich um 7 Uhr morgens ausgeführt, gesteuert durch Crontab-Einträge.

**Codebestandteile**

+ gpio_init.py: Initialisiert den GPIO-Pin zur Steuerung der Wasserpumpe.
+ irrigation_inside.py: Steuert die Innenbewässerung, aktiviert die Pumpe für eine festgelegte Anzahl an Sekunden.
+ irrigation_outside.py: Steuert die Außenbewässerung, inklusive Abruf von Wetterdaten und Entscheidungslogik zur Bewässerung.

**Bildaufnahmen**

HIER NOCH BILDER EINFÜGEN:

![GUI](./Screenshot_GUI.png "GUI")

**Ausschluss der Haftung**

Jegliche Gewähr oder Haftung wird ausgeschlossen. Die Nutzung des Codes erfolgt auf eigene Verantwortung.


