# NIS-BSI-MapMap
Ein Tool zum Mappen von NIS auf BSI-100 auf BSI-200

Ausgangsbasis:
NIS Fact Sheet 2018 mit Mapping-Tabelle auf BSI-100: https://www.nis.gv.at/NIS_Fact_Sheet_2018_08_3_0.pdf

BSI Migrationstabellen: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/Migrationstabellen.html

## Initales Tool

Konvertieren aller xlsx Tabellen in CSV Dateien.

## MapMap.py

Durchsucht alle CSV Versionen der Migrationstabellen nach den jeweiligen BSI-100 Kurzschreibweisen und gibt alle Entsprechenden neuen Bezeichnungen nach BSI-200 zurück.

Die entsprechenden Kurzschreibweisen der Maßnahmen müssen händsich aus der Mapping Tabelle extrahiert werden.
