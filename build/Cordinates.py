import Datei_Import
from matplotlib import pyplot as plt
from ipyleaflet import Map


activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, \
raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, \
raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, \
raw_vertical_radius = Datei_Import.get_dataframe()

m = Map(center=(52.204793, 360.121558), zoom=4, scroll_wheel_zoom=True)
print(m)

