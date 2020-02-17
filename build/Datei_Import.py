import pandas as pd
import os

#Pfad der Main.py abfragen
def get_pfad():
    pfad = os.getcwd()
    return pfad

#Vorlage für pfad zur abfrage von Source erstellen
def get_vorlage_pfad():
    pfad = get_pfad()
    pfad_split = pfad.split("\\")
    vorlage_pfad = pfad_split[0]
    for i in range(1,len(pfad_split)-1):
        vorlage_pfad = vorlage_pfad + "\\" + pfad_split[i]
    vorlage_pfad = vorlage_pfad + "\\" + "src\\"
    return vorlage_pfad

#Datei einlesen
def datei_einlesen(dateiname):
    vorlage = get_vorlage_pfad()
    datei = pd.read_csv(vorlage + dateiname)
    return datei

