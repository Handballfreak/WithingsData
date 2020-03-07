import Datei_Import
import pandas as pd
from datetime import date, datetime
from sklearn.linear_model import LinearRegression

activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, \
raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, \
raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, \
raw_vertical_radius = Datei_Import.get_dataframe()

# sepperate weekdays
day_7 = steps["value"].tolist()[0::7]
day_6 = steps["value"].tolist()[1::7]
day_5 = steps["value"].tolist()[2::7]
day_4 = steps["value"].tolist()[3::7]
day_3 = steps["value"].tolist()[4::7]
day_2 = steps["value"].tolist()[5::7]
day_1 = steps["value"].tolist()[6::7]

# correct order
day_7 = day_7[::-1]
day_6 = day_6[::-1]
day_5 = day_5[::-1]
day_4 = day_4[::-1]
day_3 = day_3[::-1]
day_2 = day_2[::-1]
day_1 = day_1[::-1]

#list to array

lst_7=[]
for i in range(0,len(day_7)):
    lst_7.append(i)
lst_7=lst_7.reshape(-1,1)
# model for each day in a week
model_7 = LinearRegression()
model_7.fit(lst_7, day_7)

lst_6=[]
for i in range(len(day_6)):
    lst_6.append(i)
lst_6=lst_6.reshape(-1,1)
model_6 = LinearRegression()
model_6.fit(lst_6, day_6)

lst_5=[]
for i in range(len(day_5)):
    lst_5.append(i)
lst_5=lst_5.reshape(-1,1)
model_5 = LinearRegression()
model_5.fit(lst_5, day_5)

lst_4=[]
for i in range(len(day_4)):
    lst_4.append(i)
lst_4=lst_4.reshape(-1,1)
model_4 = LinearRegression()
model_4.fit(lst_4, day_4)

lst_3=[]
for i in range(len(day_3)):
    lst_3.append(i)
lst_3=lst_3.reshape(-1,1)
model_3 = LinearRegression()
model_3.fit(lst_3, day_3)

lst_2=[]
for i in range(len(day_2)):
    lst_2.append(i)
lst_2=lst_2.reshape(-1,1)
model_2 = LinearRegression()
model_2.fit(lst_2, day_2)

lst_1=[]
for i in range(len(day_1)):
    lst_1.append(i)
lst_1=lst_1.reshape(-1,1)
model_1 = LinearRegression()
model_1.fit(lst_1, day_1)

print(sum(steps.value))
def predict_step(goal):
    return 0