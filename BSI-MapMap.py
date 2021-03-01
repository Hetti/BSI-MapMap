#!/usr/bin/env python3
# BSI-MapMap Tool

import os
import csv

mappingsign = "x"

# CSV Parsing: https://docs.python.org/3/library/csv.html

def getmapping(filelist, mapvalue):

    result = []
    print("Checking Maßnahme " + mapvalue)
    for file in filelist:
        #print("checking file: " + file)
        # opening the CSV file
        with open(file, mode='r') as csvfile:

            spamreader = csv.reader(csvfile, delimiter=',')
            datalist = list(spamreader)
            #print(datalist)
            #print(datalist[2])
            if mapvalue in datalist[2]:
                print(f"{mapvalue} in Datei {file} gefunden")
                indexval = (datalist[2].index(mapvalue))
                for lists in datalist:
                    try:
                        if lists[indexval] == mappingsign:
                            print(lists[0])
                            result.append(lists[0])
                    except:
                        continue

    print(f"\nGefundene Mappings für {mapvalue}: " + str(result) + "\n")
    return result


Kategorie_1 = ["M 2.10", "M 2.162", "M 2.205", "M 2.217", "M 2.236", "M 2.337", "M 2.340", "M 2.550",
               "M 3.2", "M 4.99", "M 2.64", "M 2.199", "M 4.81", "M 2.214", "B 1.0", "B 1.13", "B 1.2", "B 1.3",
               "B 1.8", "M 2.1", "M 2.192", "M 2.193", "M 2.225", "M 2.226", "M 2.30", "M 2.312", "M 2.336", "M 2.337",
               "M 2.35", "M 2.39", "M 2.5", "M 2.550", "M 3.1", "M 3.2", "M 3.62", "M 3.33", "M 3.5", "M 3.50", "M 3.6",
               "M 3.96", "M 6.59", "M 6.61", "M 6.65"]

Kategorie_2 = ["B 1.11", "B 1.17", "M 2.250", "M 2.251", "M 2.253", "M 2.254", "M 2.356", "M 2.4",
               "M 2.475", " M 2.516", "M 2.517", "M 2.539", "M 2.541", "M 2.554", "M 3.55", "M 5.33",
               "M 5.87", "M 5.88", "B 1.11", "B 1.14", "B 1.17", "B 5.23", "M 2.221", "M 2.256", "M 2.34"]

Kategorie_3 = ["B 1.10", "B 1.9", "B 4.2", "B 5.25", "M 2.1", "M 2.201", "M 2.219", "M 2.62", "B 1.0", "B 1.1",
               "M 1.33", "M 1.34", "M 2.139", "M 2.195", "M 2.217", "M 2.218", "M 2.225", "M 2.226", "M 2.235",
               "M 2.309", "M 3.6", "M 5.88", "B 3.301", "B 4.1", "B 4.2", "B 4.4", "B 4.5", "M 2.141", "M 2.143",
               "M 2.169", "M 2.279", "M 2.38", "M 2.576", "M 2.577", "M 2.579", "M 4.133", "M 4.79", "M 4.80", "M 4.81",
               "M 4.82", "M 5.61", "M 5.62", "M 5.68", "M 5.7", "M 5.71", "M 5.77", "M 5.8", "M 5.9", "B 1.10", "B 1.14",
               "B 1.9", "B 5.25", "M 2.216", "M 2.273", "M 2.35", "M 2.62", "M 2.85", "B 1.15", "B 1.2", "B 1.4", "B 1.6",
               "B 1.7", "B 1.8", "B 3.402", "B 3.403", "B 3.404", "B 3.405", "B 3.406", "B 5.14", "B 5.19", "B 5.2",
               "B 5.3", "M 2.112", "M 2.154", "M 2.161", "M 2.164", "M 2.217", "M 2.218", "M 2.226", "M 2.3", "M 2.35",
               "M 2.37", "M 2.393", "M 2.398", "M 2.4", "M 2.431", "M 2.44", "M 2.45", "M 2.455", "M 2.46", "M 2.5",
               "M 2.9", "M 3.2", "M 3.55", "M 4.1", "M 4.2", "M 4.234", "M 5.108", "M 5.23", "M 5.54", "M 5.56", "M 5.88",
               "M 6.20", "M 6.23", "M 6.32", "M 6.41"]

Kategorie_4 = ["M 2.220", "M 2.20", "M 2.38", "M 4.312", "M 2.11", "M 2.217", "M 2.220", "M 2.30", "M 2.321",
               "M 2.322", "M 2.378", "M 2.8", "M 3.18", "M 4.133", "M 4.135", "M 4.15", "M 4.16", "M 4.2", "M 4.41",
               "M 4.494", "M 5.61", "M 5.62", "M 5.77"]

Kategorie_5 = ["B 1.18", "B 4.4", "B 4.5", "B 5.15", "M 2.169", "M 2.214", "M 2.220", "M 2.30", "M 2.457",
               "M 2.5", "M 2.7", "M 2.71", "M 2.8", "B 1.18", "M 2.11", "M 2.199", "M 2.20", "M 2.22", "M 2.220",
               "M 2.226", "M 2.30", "M 2.31", "M 2.38", "M 2.402", "M 2.5", "M 2.586", "M 2.63", "M 3.26", "M 3.5",
               "M 4.133", "M 4.312", "M 4.7", "M 5.34"]

Kategorie_6 = ["B 1.10", "B 1.11", "B 1.14", "B 1.7", "B 1.9", "B 5.21", "B 5.24", "B 5.25", "B 5.27", "B 5.4",
               "M 2.162", "M 2.164", "M 2.172", "M 2.216", "M 2.217", "M 2.220", "M 2.251", "M 2.252", "M 2.253",
               "M 2.254", "M 2.256", "M 2.34", "M 2.4", "M 2.487", "M 2.546", "M 2.568", "M 2.62", "M 2.66", "M 2.80",
               "M 2.85", "M 2.9", "M 4.176", "M 4.494", "M 4.65", "M 4.78", "M 4.93", "M 4.94", "M 5.150", "M 5.87",
               "M 5.88", "B 2.10", "B 3.203", "B 3.404", "B 3.405", "B 5.8", "M 1.33", "M 2.218", "M 2.309"]

Kategorie_7 = ["B 2.3", "B 1.15", "B 2.1", "B 2.10", "B 2.12", "B 2.2", "B 2.3", "B 3.203", "B 3.406",
               "B 5.8", "M 1.1", "M 1.12", "M 1.13", "M 1.16", "M 1.17", "M 1.18", "M 1.19", "M 1.2", "M 1.22",
               "M 1.28", "M 1.29", "M 1.33", "M 1.45", "M 1.46", "M 1.49", "M 1.53", "M 1.55", "M 1.56", "M 1.58",
               "M 1.6", "M 1.61", "M 1.75", "M 1.78", "M 1.79", "M 1.80", "M 2.112", "M 2.16", "M 2.17", "M 2.18",
               "M 2.218", "M 2.309", "M 2.37", "M 2.4", "M 2.431", "M 2.6", "M 2.90", "M 3.26", "M 4.1", "M 4.2",
               "M 4.234", "M 4.29", "M 5.4", "M 5.5"]

Kategorie_8 = ["B 1.6", "B 1.8", "B 5.22", "M 2.110", "M 2.133", "M 2.154", "M 2.220", "M 2.273", "M 2.35",
               "M 2.500", "M 2.568", "M 2.64", "M 2.9", "M 4.135", "M 4.227", "M 4.25", "M 4.34", "M 4.430", "M 4.5",
               "M 4.81", "M 4.93", "M 5.150", "M 5.9", "M 6.23", "B 5.22", "M 2.110", "M 2.133", "M 2.220", "M 2.500",
               "M 2.64", "M 4.135", "M 4.227", "M 4.25", "M 4.34", "M 4.430", "M 4.5", "M 4.81", "M 4.93"]

Kategorie_9 = ["B 1.6", "B 1.8", "M 2.154", "M 2.35", "M 2.9", "M 3.6", "M 6.121", "M 6.23", "M 6.58",
               "M 6.59", "M 6.60", "M 6.64", "M 6.65", "B 1.3", "B 1.8", "M 6.59", "M 6.61", "M 6.64", "M 6.65",
               "B 1.8", "M 6.122", "M 6.127", "M 6.66", "M 6.68"]

Kategorien = [Kategorie_1, Kategorie_2, Kategorie_3, Kategorie_4,
              Kategorie_5, Kategorie_6, Kategorie_7, Kategorie_8, Kategorie_9]

# Example for all files in folder used from https://pythonguides.com/python-get-all-files-in-directory/#Python_get_all_files_in_directory

path = "./Migrationstabellen_CSV"

CSV_Tabellen = []
for root, dirs, files in os.walk(path):
	for file in files:
		CSV_Tabellen.append(os.path.join(root, file))

Kategorienum = 1
for Subkategorie in Kategorien:
    kategoriegesamt = []
    print(
        f"""\n\n===========================
=   Mapping Kategorie {str(Kategorienum)}   =
===========================\n"""
    )

    for Element in Subkategorie:
        #print(Element)
        mapped = getmapping(CSV_Tabellen, Element)
        kategoriegesamt.append(mapped)

    print(f"Kapitel {Kategorienum} Resultat: " + str(kategoriegesamt) + "\n")
    empty = "|"
    for x in range(0, len(Subkategorie)):
        if not kategoriegesamt[x]:
            empty += f" {Subkategorie[x]} |"
        else:
            print(f"Maßnahme {Subkategorie[x]} Mapping: {kategoriegesamt[x]}\n")
    print("Kein Mapping für: " + empty)
    Kategorienum += 1
