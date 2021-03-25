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

BSI:  
 * BSI IT Grundschutz Kompendium: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/IT_Grundschutz_Kompendium_Edition2021.html  - (PDF Name: IT_Grundschutz_Kompendium_Edition2021.pdf)
 * BSI 100 zu 200 Migrationstabellen: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/Migrationstabellen.html  - (Archiv Name: Migrationstabellen.zip)


NIS:  
 * NIS Fact Sheet 2018 mit Mapping-Tabelle auf BSI-100: https://www.nis.gv.at/NIS_Fact_Sheet_2018_08_3_0.pdf


## Prerequisites

 * Für das XLSX Script zum Konvertieren der Excel Tabellen nach CSV: https://github.com/dilshod/xlsx2csv
 * Bash
 * Python 3
  * PDF Library: pdftotext - https://pypi.org/project/pdftotext/ - `pip3 install pdftotext`
 * Extrahierte Migrationstabellen in dem Ordner `Migrationstabellen`
 * Manuell konvertierte ODS Dateien, siehe XLSX_to_csv.sh

## XLSX_to_csv.sh

Shellscript das alle xlsx Tabellen in CSV Dateien konvertiert.

Achtung die zwei ODS Dateien `MT_Datenträgerarchiv.ods` und `MT_Datenträgerarchiv.ods` aus dem Archiv müssen manuell via Calc oder Excel zu einem CSV konvertiert und im Ordner Migrationstabellen abgelegt werden.

## BSI-MapMap.py

Durchsucht alle CSV Versionen der Migrationstabellen nach den jeweiligen BSI-100 Kurzschreibweisen und gibt alle Entsprechenden neuen Bezeichnungen nach BSI-200 zurück.
Für jede Kategorie wird die entsprechende Datei `Kategorie-<Zahl>-BSI200.txt` erstellt, in die alle, mittels Regular Expression (Regex) extrahierten, Anforderungsbeschreibungen aus dem PDF reingeschrieben werden.

Die gewünschten BSI-100 Kurzschreibweisen der Maßnahmen müssen händisch gewählt bzw. aus der Mapping Tabelle extrahiert werden.
Zurzeit wird das Mapping aus den Kategorien 1-9 des NIS Fact Sheets 2018 gesucht und die korrespondierenden Anforderungen ausgegeben.


# DISCLAIMER

Ich gebe keine Garantie auf die Vollständigkeit und Korrektheit dieser Software und den daraus entstehenden Outputs.

Die Nutzung dieser Software passiert auf eigene Verantwortung.


Pull Requests werden gerne entgegen genommen und werden auf Basis der GPLv3 eingepflegt.
