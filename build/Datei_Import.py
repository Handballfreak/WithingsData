import pandas as pd
import os
import ast


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
    activities["calories"] = activities.Data.apply(lambda x: key_value_of_string("calories", x))
    activities["device_startdate"] = activities.Data.apply(lambda x: key_value_of_string("device_startdate", x))
    activities["device_enddate"] = activities.Data.apply(lambda x: key_value_of_string("device_enddate", x))
    activities["pause_duration"] = activities.Data.apply(lambda x: key_value_of_string("pause_duration", x))
    activities["steps"] = activities.Data.apply(lambda x: key_value_of_string("steps", x))

    activities["end_coordinate_latitude"] = activities.GPS.apply(
        lambda x: key_value_of_string("end_coordinate_latitude", x))
    activities["end_coordinate_longitude"] = activities.GPS.apply(
        lambda x: key_value_of_string("end_coordinate_longitude", x))
    activities["region_center_latitude"] = activities.GPS.apply(
        lambda x: key_value_of_string("region_center_latitude", x))
    activities["region_center_longitude"] = activities.GPS.apply(
        lambda x: key_value_of_string("region_center_longitude", x))
    activities["span_latitude_delta"] = activities.GPS.apply(
        lambda x: key_value_of_string("span_latitude_delta", x))
    activities["span_longitude_delta"] = activities.GPS.apply(
        lambda x: key_value_of_string("span_longitude_delta", x))
    activities["start_coordinate_latitude"] = activities.GPS.apply(
        lambda x: key_value_of_string("start_coordinate_latitude", x))
    activities["start_coordinate_longitude"] = activities.GPS.apply(
        lambda x: key_value_of_string("start_coordinate_longitude", x))
    activities["avg_speed"] = activities.GPS.apply(
        lambda x: key_value_of_string("avg_speed", x))
    activities["distance"] = activities.GPS.apply(
        lambda x: key_value_of_string("distance", x))
    activities["max_speed"] = activities.GPS.apply(
        lambda x: key_value_of_string("max_speed", x))
    activities["min_speed"] = activities.GPS.apply(
        lambda x: key_value_of_string("min_speed", x))

    activities["intensity"] = activities.Data.apply(lambda x: key_value_of_string("intensity", x))
    activities["manual_distance"] = activities.Data.apply(lambda x: key_value_of_string("manual_distance", x))
    activities["manual_calories"] = activities.Data.apply(lambda x: key_value_of_string("manual_calories", x))
    activities["hr_average"] = activities.Data.apply(lambda x: key_value_of_string("hr_average", x))
    activities["hr_min"] = activities.Data.apply(lambda x: key_value_of_string("hr_min", x))
    activities["hr_max"] = activities.Data.apply(lambda x: key_value_of_string("hr_max", x))
    activities["hr_zone_0"] = activities.Data.apply(lambda x: key_value_of_string("hr_zone_0", x))
    activities["hr_zone_1"] = activities.Data.apply(lambda x: key_value_of_string("hr_zone_1", x))
    activities["hr_zone_2"] = activities.Data.apply(lambda x: key_value_of_string("hr_zone_2", x))
    activities["hr_zone_3"] = activities.Data.apply(lambda x: key_value_of_string("hr_zone_3", x))
    activities["pause_duration"] = activities.Data.apply(lambda x: key_value_of_string("pause_duration", x))
    activities["steps"] = activities.Data.apply(lambda x: key_value_of_string("steps", x))
    activities["distance"] = activities.Data.apply(lambda x: key_value_of_string("distance", x))
    activities["elevation"] = activities.Data.apply(lambda x: key_value_of_string("elevation", x))
    activities["metcumul"] = activities.Data.apply(lambda x: key_value_of_string("metcumul", x))
    activities["device_startdate"] = activities.Data.apply(lambda x: key_value_of_string("device_startdate", x))
    activities["device_enddate"] = activities.Data.apply(lambda x: key_value_of_string("device_enddate", x))
    activities["laps"] = activities.Data.apply(lambda x: key_value_of_string("laps", x))
    activities["mvts"] = activities.Data.apply(lambda x: key_value_of_string("mvts", x))
    activities["pool_length"] = activities.Data.apply(lambda x: key_value_of_string("pool_length", x))
    activities["version"] = activities.Data.apply(lambda x: key_value_of_string("version", x))
    activities["type"] = activities.Data.apply(lambda x: key_value_of_string("type", x))
    return activities


def key_value_of_string(key, dictionary):
    if key in ast.literal_eval(dictionary):
        return ast.literal_eval(dictionary).get(key)
