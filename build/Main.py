# import pandas as pd
import Datei_Import
import Visualization

# Visualization.distance_graph()
# Visualization.step_graph()
activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, raw_vertical_radius = Datei_Import.get_dataframe()

activities = Datei_Import.clean_activities(activities)
print(activities)
# print(Datei_Import.help_clean_activities("calories", ["data", "calories":]))
