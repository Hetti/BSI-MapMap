# BSI-MapMap
Ein Tool zum Mappen von NIS auf BSI-100 auf BSI-200


Insbesondere mappt der Code die BSI-100 Maßnahmen des österreichischen NIS Fact Sheets 2018 auf die entsprechenden BSI-200 Kapitel auf Basis der offiziellen BSI Migrationstabellen.

Maßnahmen 1-9 

Ausgangsbasis:
NIS Fact Sheet 2018 mit Mapping-Tabelle auf BSI-100: https://www.nis.gv.at/NIS_Fact_Sheet_2018_08_3_0.pdf

BSI Migrationstabellen: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/Migrationstabellen.html

## XLSX_to_csv.sh

Shellscript das alle xlsx Tabellen in CSV Dateien konvertiert.

## BSI-MapMap.py

Durchsucht alle CSV Versionen der Migrationstabellen nach den jeweiligen BSI-100 Kurzschreibweisen und gibt alle Entsprechenden neuen Bezeichnungen nach BSI-200 zurück.

Die gewünschten BSI-100 Kurzschreibweisen der Maßnahmen müssen händisch gwählt bzw. aus der Mapping Tabelle extrahiert werden.
