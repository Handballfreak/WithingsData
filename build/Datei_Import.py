import pandas as pd
import os


# Path of Main.py
def get_pfad():
    pfad = os.getcwd()
    return pfad


# get path for sources
def get_vorlage_pfad():
    pfad = get_pfad()
    pfad_split = pfad.split("\\")
    vorlage_pfad = pfad_split[0]
    for i in range(1, len(pfad_split) - 1):
        vorlage_pfad = vorlage_pfad + "\\" + pfad_split[i]
    vorlage_pfad = vorlage_pfad + "\\" + "src\\"
    return vorlage_pfad


# read sources
def datei_einlesen(dateiname):
    vorlage = get_vorlage_pfad()
    datei = pd.read_csv(vorlage + dateiname)
    return datei


# read sources
def get_dataframe():
    activities = datei_einlesen("activities.csv")
    calories_earned = datei_einlesen("aggregates_calories_earned.csv")
    calories_passive = datei_einlesen("aggregates_calories_passive.csv")
    distance = datei_einlesen("aggregates_distance.csv")
    elevation = datei_einlesen("aggregates_elevation.csv")
    steps = datei_einlesen("aggregates_steps.csv")
    sleep = datei_einlesen("sleep.csv")
    raw_altitude = datei_einlesen("raw_tracker_altitude.csv")
    raw_calories_earned = datei_einlesen("raw_tracker_calories-earned.csv")
    raw_distance = datei_einlesen("raw_tracker_distance.csv")
    raw_elevation = datei_einlesen("raw_tracker_elevation.csv")
    raw_gps_speed = datei_einlesen("raw_tracker_gps-speed.csv")
    raw_horizontal_radius = datei_einlesen("raw_tracker_horizontal-radius.csv")
    raw_hr = datei_einlesen("raw_tracker_hr.csv")
    raw_lap_pool = datei_einlesen("raw_tracker_lap-pool.csv")
    raw_latitude = datei_einlesen("raw_tracker_latitude.csv")
    raw_longtitude = datei_einlesen("raw_tracker_longitude.csv")
    raw_sleep_state = datei_einlesen("raw_tracker_sleep-state.csv")
    raw_steps = datei_einlesen("raw_tracker_steps.csv")
    raw_vertical_radius = datei_einlesen("raw_tracker_vertical-radius.csv")
    return activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, raw_vertical_radius


def clean_activities(activities):
    activities['new_Data'] = activities.Data.str.strip("{")
    activities["new_Data"] = activities.new_Data.str.strip("}")
    new_Data_split = activities.new_Data.str.split(",")
    activities["calories"] = help_clean_activities("calories", new_Data_split)
    return activities


def help_clean_activities(row, split_Data):
    value = 0
    for i in range(len(split_Data)):
        if row in split_Data.str.get(i):
            value += int(i[len(row)+1:])
    return value