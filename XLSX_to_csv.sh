#!/bin/bash

# Konvertiere alle XLSX zu CSV um sie durchsuchbar zu machen
# Muss im Ordner ausgführt werden wo die Migrationstabellen Ordner vorhandne ist aus dem ZIP

# 2 Files sind nicht konvertierbar, da sie ODS Files sind.
# - OPS.2.2_Cloud-Nutzung.ods
# - MT_Datenträgerarchiv.ods


mkdir Migrationstabellen_CSV

for csvfiles in Migrationstabellen/*
do
    #echo ${csvfiles}
    echo "Converting: `basename ${csvfiles}`"
    CSV_FILE=`basename ${csvfiles}`
    xlsx2csv2 "${csvfiles}" > Migrationstabellen_CSV/"${CSV_FILE}".csv
    echo "============================="
done

echo "DONE - bye bye"

