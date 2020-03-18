import Datei_Import
import pandas as pd
import numpy as np
from datetime import date, datetime
from sklearn.linear_model import LinearRegression

activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, \
raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, \
raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, \
raw_vertical_radius = Datei_Import.get_dataframe()


def get_day(train_help):
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

    if (train_help == -1):
        train_help = len(day_1)
    day_7 = day_7[len(day_7) - train_help:]
    day_6 = day_6[len(day_6) - train_help:]
    day_5 = day_5[len(day_5) - train_help:]
    day_4 = day_4[len(day_4) - train_help:]
    day_3 = day_3[len(day_3) - train_help:]
    day_2 = day_2[len(day_2) - train_help:]
    day_1 = day_1[len(day_1) - train_help:]

    return day_7, day_6, day_5, day_4, day_3, day_2, day_1


def train_steps(train_help):
    day_7, day_6, day_5, day_4, day_3, day_2, day_1 = get_day(train_help)
    # train Linear Regression Models
    lst_7 = []
    for i in range(0, len(day_7)):
        lst_7.append(i)
    lst_7 = np.array(lst_7)
    lst_7 = lst_7.reshape(-1, 1)
    # model for each day in a week
    model_7 = LinearRegression()
    model_7.fit(lst_7, day_7)

    lst_6 = []
    for i in range(len(day_6)):
        lst_6.append(i)
    lst_6 = np.array(lst_6)
    lst_6 = lst_6.reshape(-1, 1)
    model_6 = LinearRegression()
    model_6.fit(lst_6, day_6)

    lst_5 = []
    for i in range(len(day_5)):
        lst_5.append(i)
    lst_5 = np.array(lst_5)
    lst_5 = lst_5.reshape(-1, 1)
    model_5 = LinearRegression()
    model_5.fit(lst_5, day_5)

    lst_4 = []
    for i in range(len(day_4)):
        lst_4.append(i)
    lst_4 = np.array(lst_4)
    lst_4 = lst_4.reshape(-1, 1)
    model_4 = LinearRegression()
    model_4.fit(lst_4, day_4)

    lst_3 = []
    for i in range(len(day_3)):
        lst_3.append(i)
    lst_3 = np.array(lst_3)
    lst_3 = lst_3.reshape(-1, 1)
    model_3 = LinearRegression()
    model_3.fit(lst_3, day_3)

    lst_2 = []
    for i in range(len(day_2)):
        lst_2.append(i)
    lst_2 = np.array(lst_2)
    lst_2 = lst_2.reshape(-1, 1)
    model_2 = LinearRegression()
    model_2.fit(lst_2, day_2)

    lst_1 = []
    for i in range(len(day_1)):
        lst_1.append(i)
    lst_1 = np.array(lst_1)
    lst_1 = lst_1.reshape(-1, 1)
    model_1 = LinearRegression()
    model_1.fit(lst_1, day_1)

    return model_7, model_6, model_5, model_4, model_3, model_2, model_1


def predict_step(goal):
    trigger_min = False
    sum_steps = sum(steps.value)
    difference = goal - sum_steps

    # goal already achieved
    if goal <= sum_steps:
        return -1, trigger_min

    if (difference <= 100000):
        train_help = 4
        model_7, model_6, model_5, model_4, model_3, model_2, model_1 = train_steps(4)
    else:
        train_help = -1
        model_7, model_6, model_5, model_4, model_3, model_2, model_1 = train_steps(-1)

    day_7, day_6, day_5, day_4, day_3, day_2, day_1 = get_day(train_help)
    len_day_7 = len(day_7)
    len_day_7 = np.array(len_day_7)
    len_day_7 = len_day_7.reshape(-1, 1)
    len_day_6 = len(day_6)
    len_day_6 = np.array(len_day_6)
    len_day_6 = len_day_6.reshape(-1, 1)
    len_day_5 = len(day_5)
    len_day_5 = np.array(len_day_5)
    len_day_5 = len_day_5.reshape(-1, 1)
    len_day_4 = len(day_4)
    len_day_4 = np.array(len_day_4)
    len_day_4 = len_day_4.reshape(-1, 1)
    len_day_3 = len(day_3)
    len_day_3 = np.array(len_day_3)
    len_day_3 = len_day_3.reshape(-1, 1)
    len_day_2 = len(day_2)
    len_day_2 = np.array(len_day_2)
    len_day_2 = len_day_2.reshape(-1, 1)
    len_day_1 = len(day_1)
    len_day_1 = np.array(len_day_1)
    len_day_1 = len_day_1.reshape(-1, 1)

    count_steps = sum_steps
    count_days = 0
    min_steps = min(steps.value) + 1
    while count_steps < goal:
        len_day_1 += 1
        count_days += 1
        steps_day_1 = model_1.predict(len_day_1)
        if steps_day_1 < min_steps:
            trigger_min = True
            steps_day_1 = min_steps
        count_steps += steps_day_1
        if (count_steps >= goal):
            return count_days, trigger_min
        len_day_2 += 1
        count_days += 1
        steps_day_2 = model_2.predict(len_day_2)
        if steps_day_2 < min_steps:
            trigger_min = True
            steps_day_2 = min_steps
        count_steps += steps_day_2
        if (count_steps >= goal):
            return count_days, trigger_min
        len_day_3 += 1
        count_days += 1
        steps_day_3 = model_3.predict(len_day_3)
        if steps_day_3 < min_steps:
            trigger_min = True
            steps_day_3 = min_steps
        count_steps += steps_day_3
        if (count_steps >= goal):
            return count_days, trigger_min
        len_day_4 += 1
        count_days += 1
        steps_day_4 = model_1.predict(len_day_4)
        if steps_day_4 < min_steps:
            trigger_min = True
            steps_day_4 = min_steps
        count_steps += steps_day_4
        if (count_steps >= goal):
            return count_days, trigger_min
        len_day_5 += 1
        count_days += 1
        steps_day_5 = model_5.predict(len_day_5)
        if steps_day_5 < min_steps:
            trigger_min = True
            steps_day_5 = min_steps
        count_steps += steps_day_5
        if (count_steps >= goal):
            return count_days, trigger_min
        len_day_6 += 1
        count_days += 1
        steps_day_6 = model_6.predict(len_day_6)
        if steps_day_6 < min_steps:
            trigger_min = True
            steps_day_6 = min_steps
        count_steps += steps_day_6
        if (count_steps >= goal):
            return count_days, trigger_min
        len_day_7 += 1
        count_days += 1
        steps_day_7 = model_7.predict(len_day_7)
        if steps_day_7 < min_steps:
            trigger_min = True
            steps_day_7 = min_steps
        count_steps += steps_day_7
        if (count_steps >= goal):
            return count_days, trigger_min

    return count_days, trigger_min


def predict_step_evaluation(goal):
    count_days, trigger_min = predict_step(goal)
    string_evaluation = ""
    date_steps = steps.date.tolist()[::-1]
    if count_days == -1:
        max_steps = goal
        count_steps = 0
        value_steps = steps.value.tolist()[::-1]
        i = 0
        while count_steps <= max_steps:
            count_steps += value_steps[i]
            i += 1
        date = date_steps[i - 1]
        string_evaluation = "You already reached that goal at the " + date + "!"
    else:
        success_date = pd.to_datetime(date_steps[-1]) + pd.DateOffset(days=count_days)
        string_evaluation = "If you keep going you will propably achieve your goal on the " + success_date.strftime(
            "%d/%m/%Y"+".")
    if trigger_min == True:
        string_evaluation += "\nOn at least one day a week you show a negative trend in your activity."
    return string_evaluation
