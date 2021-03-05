#!/bin/bash

# Konvertiere alle XLSX zu CSV um sie durchsuchbar zu machen
# Muss im Ordner ausgführt werden wo die Migrationstabellen Ordner vorhandne ist aus dem ZIP



mkdir Migrationstabellen_CSV

# DANKE SAP - IFS auf Newline only wegen dem APP4.2 Dokument...
IFS=$'\n'

for csvfiles in Migrationstabellen/*.xlsx
do
    #echo ${csvfiles}
    echo "Converting: `basename ${csvfiles}`"
    CSV_FILE=`basename ${csvfiles}`
    xlsx2csv2 "${csvfiles}" > Migrationstabellen_CSV/"${CSV_FILE}".csv
    echo "============================="
done

# 2 Files sind nicht mit dem xlsx2csv2 Tool konvertierbar, da sie ODS Files sind.
# - OPS.2.2_Cloud-Nutzung.ods
# - MT_Datenträgerarchiv.ods

# TODO Diese zwei ODS Dateien in CSV konvertieren - Vielleicht mache ich das im Python File

echo "DONE - bye bye"

