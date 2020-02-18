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


def get_dataframe():
    activities = datei_einlesen("activities.csv")
    calories_earned = datei_einlesen("aggregates_calories_earned.csv")
    calories_passive = datei_einlesen("aggregates_calories_passive.csv")
    distance = datei_einlesen("aggregates_distance.csv")
    elevation = datei_einlesen("aggregates_elevation.csv")
    steps = datei_einlesen("aggregates_steps.csv")
    sleep = datei_einlesen("sleep.csv")
    raw_altitude = datei_einlesen("raw_tracker_altidude.csv")
    raw_calories_earned = datei_einlesen("raw_tracker_calories_earned.csv")
    raw_distance = datei_einlesen("raw_tracker_distance.csv")
    raw_elevation = datei_einlesen("raw_tracker_elevation.csv")
    raw_gps_speed = datei_einlesen("raw_tracker_gps-speed.csv")
    raw_horizontal_radius = datei_einlesen("raw_tracker_horizontal-radius.csv")
    raw_hr = datei_einlesen("raw_tracker_hr.csv")
    raw_lap_pool = datei_einlesen("raw_tracker_lap-pool.csv")
    raw_latitude = datei_einlesen("raw_tracker_latitude.csv")
    raw_longtitude = datei_einlesen("raw_tracker_longtitude.csv")
    raw_sleep_state = datei_einlesen("raw_tracker_sleep-state.csv")
    raw_steps = datei_einlesen("raw_tracker_steps.csv")
    raw_vertical_radius = datei_einlesen("raw_tracker_vertical-radius.csv")

