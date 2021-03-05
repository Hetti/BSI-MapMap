# BSI-MapMap
Ein Tool zum Mappen von BSI-100 Maßnahmen auf BSI-200 basierend auf den offiziellen BSI Migrationstabellen.


Insbesondere mappt der Code die BSI-100 Maßnahmen der Kategorien 1-9 des österreichischen NIS Fact Sheets 2018 auf die entsprechenden BSI-200 Kapitel basierend auf den offiziellen BSI Migrationstabellen.

Folgende NIS Kategorien werden gemappt:

1. Governance und Risikomanagement
2. 	Umgang mit Dienstleistern, Lieferanten und Dritten
3. 	Sicherheitsarchitektur
4. 	Systemadministration
5. 	Identitäts- und Zugriffsmanagement
6. 	Systemwartung und Betrieb
7. 	Physische Sicherheit
8. 	Erkennung von Vorfällen
9. 	Vorfallsreaktion

Ausgangsbasis:

BSI Migrationstabellen: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/Migrationstabellen.html

NIS:
NIS Fact Sheet 2018 mit Mapping-Tabelle auf BSI-100: https://www.nis.gv.at/NIS_Fact_Sheet_2018_08_3_0.pdf


## XLSX_to_csv.sh

Shellscript das alle xlsx Tabellen in CSV Dateien konvertiert.

## BSI-MapMap.py

Durchsucht alle CSV Versionen der Migrationstabellen nach den jeweiligen BSI-100 Kurzschreibweisen und gibt alle Entsprechenden neuen Bezeichnungen nach BSI-200 zurück.

Die gewünschten BSI-100 Kurzschreibweisen der Maßnahmen müssen händisch gwählt bzw. aus der Mapping Tabelle extrahiert werden.


# DISCLAIMER

Ich gebe keine Garantie auf die Vollständigkeit und Korrektheit dieser Software und den daraus entstehenden Outputs.

Die Nutzung dieser Software passiert auf eigene Verantwortung.


Pull Requests werden gerne entgegen genommen und werden auf Basis der GPLv3 eingepflegt.
