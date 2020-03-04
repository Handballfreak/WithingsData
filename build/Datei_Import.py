import pandas as pd
import os
import ast
import math


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
    #Data columns
    activities["calories"] = activities.Data.apply(lambda x: key_value_of_string("calories", x))
    activities["device_startdate"] = activities.Data.apply(lambda x: key_value_of_string("device_startdate", x))
    activities["device_enddate"] = activities.Data.apply(lambda x: key_value_of_string("device_enddate", x))
    activities["pause_duration"] = activities.Data.apply(lambda x: key_value_of_string("pause_duration", x))
    activities["steps"] = activities.Data.apply(lambda x: key_value_of_string("steps", x))
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

    #GPS columns
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

    return activities


def get_walking(activities):
    activities = clean_activities(activities)
    walking = activities[activities['Activity type']=="Walking"].reset_index()
    walking["distance"] = walking["manual_distance"] + walking["distance"]
    walking["calories"] = walking["manual_calories"] + walking["calories"]
    walking = walking[["von","bis","from (manual)", "to (manual)", "Timezone", "calories", "intensity", "distance", "hr_average","hr_min","hr_max","hr_zone_0","hr_zone_1","hr_zone_2","hr_zone_3","pause_duration","steps","elevation","metcumul","device_startdate","device_enddate","end_coordinate_latitude","end_coordinate_longitude","region_center_latitude","region_center_longitude","span_latitude_delta","span_longitude_delta", 'start_coordinate_latitude',"start_coordinate_longitude", "avg_speed", "max_speed", "min_speed"]]
    return walking


def get_multisport(activities):
    activities = clean_activities(activities)
    multi =  activities[activities['Activity type']=="Multi Sport"].reset_index()
    multi = multi[["von","bis","from (manual)", "to (manual)", "Timezone","end_coordinate_latitude", "end_coordinate_longitude", "region_center_latitude", "region_center_longitude", "span_latitude_delta", "span_longitude_delta", "start_coordinate_latitude", "start_coordinate_longitude", "avg_speed", "distance", "max_speed", "min_speed"]]
    return multi


def get_pingpong(activities):
    activities = clean_activities(activities)
    pingpong = activities[activities['Activity type'] == "Ping Pong"].reset_index()
    pingpong["distance"] = pingpong["manual_distance"] + pingpong["distance"]
    pingpong["calories"] = pingpong["manual_calories"] + pingpong["calories"]
    pingpong = pingpong[
        ["von", "bis", "from (manual)", "to (manual)", "Timezone", "calories", "intensity", "distance", "hr_average",
         "hr_min", "hr_max", "hr_zone_0", "hr_zone_1", "hr_zone_2", "hr_zone_3", "pause_duration", "steps", "elevation",
         "metcumul"]]
    return pingpong


def get_rowing(activities):
    activities = clean_activities(activities)
    rowing = activities[activities['Activity type']=="Rowing"].reset_index()
    rowing["distance"] = rowing["manual_distance"] + rowing["distance"]
    rowing["calories"] = rowing["manual_calories"] + rowing["calories"]
    rowing = rowing[["von","bis","from (manual)", "to (manual)", "Timezone", "calories", "intensity", "distance", "hr_average","hr_min","hr_max","hr_zone_0","hr_zone_1","hr_zone_2","hr_zone_3","pause_duration","steps","elevation","metcumul","device_startdate","device_enddate","end_coordinate_latitude","end_coordinate_longitude","region_center_latitude","region_center_longitude","span_latitude_delta","span_longitude_delta", 'start_coordinate_latitude',"start_coordinate_longitude", "avg_speed", "max_speed", "min_speed"]]
    return rowing


def get_gym(activities):
    activities = clean_activities(activities)
    gym = activities[activities['Activity type']=="Gym class"].reset_index()
    gym["distance"] = gym["manual_distance"] + gym["distance"]
    gym["calories"] = gym["manual_calories"] + gym["calories"]
    gym = gym[["von","bis","from (manual)", "to (manual)", "Timezone", "calories", "intensity", "distance", "hr_average","hr_min","hr_max","hr_zone_0","hr_zone_1","hr_zone_2","hr_zone_3","pause_duration","steps","elevation","metcumul","device_startdate","device_enddate","end_coordinate_latitude","end_coordinate_longitude","region_center_latitude","region_center_longitude","span_latitude_delta","span_longitude_delta", 'start_coordinate_latitude',"start_coordinate_longitude", "avg_speed", "max_speed", "min_speed"]]
    return gym


def get_swimming(activities):
    activities = clean_activities(activities)
    swimming = activities[activities['Activity type']=="Swimming"].reset_index()
    swimming = swimming[["von","bis","from (manual)", "to (manual)", "Timezone", "calories", "hr_average", "hr_min", "hr_max", "hr_zone_0", "hr_zone_1", "hr_zone_2", "hr_zone_3", "pause_duration", "device_startdate", "device_enddate", "laps", "mvts", "pool_length", "version", "type"]]
    return swimming


def get_running(activities):
    activities = clean_activities(activities)
    running = activities[activities['Activity type']=="Running"].reset_index()
    running["distance"] = running["manual_distance"] + running["distance"]
    running["calories"] = running["manual_calories"] + running["calories"]
    running = running[["von","bis","from (manual)", "to (manual)", "Timezone", "calories", "intensity", "distance", "hr_average","hr_min","hr_max","hr_zone_0","hr_zone_1","hr_zone_2","hr_zone_3","pause_duration","steps","elevation","metcumul","device_startdate","device_enddate","end_coordinate_latitude","end_coordinate_longitude","region_center_latitude","region_center_longitude","span_latitude_delta","span_longitude_delta", 'start_coordinate_latitude',"start_coordinate_longitude", "avg_speed", "max_speed", "min_speed"]]
    return running


def key_value_of_string(key, dictionary):
    if not pd.isnull(dictionary):
        if key in dictionary:
            return ast.literal_eval(dictionary).get(key)
