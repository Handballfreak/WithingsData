from matplotlib import pyplot as plt
import Datei_Import
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import time
import datetime
from datetime import date
from tkinter import *
from tkinter.messagebox import showerror


activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, \
raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, \
raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, \
raw_vertical_radius = Datei_Import.get_dataframe()
activities = Datei_Import.clean_activities(activities)
calories = Datei_Import.get_calories()


# numbers to Month names
def optimize_date(date_list):
    number_months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    complete_date_list = []
    for date in date_list:
        split_date = date.split("-")
        month = number_months.get(split_date[1])
        complete_date = split_date[2] + " " + month + " " + split_date[0]
        complete_date_list.append(complete_date)
    return complete_date_list


# reducing date x ticks
def date_xtick(date_list):
    date_length = len(date_list)
    if date_length <= 31:
        date_xtick = date_list
    elif date_length <= 92:
        date_xtick = date_list[::7]
    elif date_length <= 730:
        date_xtick = date_list[::31]
    else:
        date_xtick = date_list[::365]
    return date_xtick


def timeline_opt(datatype, timerange, ax1):
    now = time.localtime()
    # Series to list
    datelist = datatype.date.tolist()
    datelist.reverse()

    # no specification
    if timerange == "kein Limit":
        ax1.bar(datelist[::], datatype.value[::])
        ax1.set_xticks(date_xtick(datelist[::]))
        ax1.set_xticklabels(optimize_date(date_xtick(datelist[::])), rotation=15, fontsize=10)

    # in the following it is assumed that the values were recorded every day without gaps
    # last year
    elif timerange == "last year":
        last_year = now.tm_year - 1
        start_date = str(last_year) + "-01-01"
        end_date = str(now.tm_year) + "-01-01"
        # the data must contain values since the last year indicated
        try:
            start_index = datelist.index(start_date)
            end_index = datelist.index(end_date) + 1
        except:
            print("gaps in data")
            Tk().withdraw()
            showerror(title="Error", message="Gaps in data")
            return FALSE
            # end_index = len(datelist)
            # start_index = 0
        ax1.bar(datelist[start_index:end_index], datatype.value[start_index:end_index])
        ax1.set_xticks(date_xtick(datelist[start_index:end_index]))
        ax1.set_xticklabels(optimize_date(date_xtick(datelist[start_index:end_index])), rotation=15, fontsize=10)
    # last month
    elif timerange == "last month":
        last_month = now.tm_mon - 1
        this_month = now.tm_mon
        # in case of january
        if (last_month == 0):
            last_month = 12
        # add the zero to the month
        if (len(str(last_month)) < 2):
            last_month = "0" + str(last_month)
        if (len(str(this_month)) < 2):
            this_month = "0" + str(this_month)
        start_date = str(now.tm_year) + "-" + str(last_month) + "-01"
        end_date = str(now.tm_year) + "-" + str(this_month) + "-01"
        # the data must contain values since the last month indicated
        try:
            start_index = datelist.index(start_date)
            end_index = datelist.index(end_date)
        except:
            print("gaps in data")
            Tk().withdraw()
            showerror(title="Error", message="Gaps in data")
            # start_index = 0
            # end_index = len(datelist)
            return FALSE

        ax1.bar(datelist[start_index:end_index], datatype.value[start_index:end_index])
        ax1.set_xticks(date_xtick(datelist[start_index:end_index]))
        ax1.set_xticklabels(optimize_date(date_xtick(datelist[start_index:end_index])), rotation=15,
                            fontsize=10)
    # last week
    elif timerange == "last week":
        # date.today().weekday() == 0 is true if today is a monday

        step_to_monday = datetime.timedelta(days=date.today().weekday())
        week = datetime.timedelta(days=7)
        mondaydate_of_current_week = datetime.datetime.now() - step_to_monday
        mondaydate_of_last_week = mondaydate_of_current_week - week
        monday_of_current_week = mondaydate_of_current_week.day
        monday_of_last_week = mondaydate_of_last_week.day

        if (len(str(monday_of_last_week)) < 2):
            monday_of_last_week = "0" + str(monday_of_last_week)
        if (len(str(monday_of_current_week)) < 2):
            monday_of_current_week = "0" + str(monday_of_current_week)
        month = now.tm_mon
        if (len(str(month)) < 2):
            month = "0" + str(month)
        last_week_month = mondaydate_of_last_week.month
        if (len(str(last_week_month)) < 2):
            last_week_month = "0" + str(last_week_month)
        start_date = str(now.tm_year) + "-" + str(last_week_month) + "-" + str(monday_of_last_week)
        end_date = str(now.tm_year) + "-" + str(month) + "-" + str(monday_of_current_week)
        # the data must contain values since the last week indicated
        try:
            start_index = datelist.index(start_date)
            end_index = datelist.index(end_date) + 1
        except:
            print("gaps in data")
            Tk().withdraw()
            showerror(title="Error", message="Gaps in data")
            #start_index = 0
            # end_index = len(datelist)
            return FALSE
        ax1.bar(datelist[start_index:end_index], datatype.value[start_index:end_index])
        ax1.set_xticks(date_xtick(datelist[start_index:end_index]))
        ax1.set_xticklabels(optimize_date(date_xtick(datelist[start_index:end_index])), rotation=15,
                            fontsize=10)
    return TRUE


def distance_graph(timerange):
    sns.set_context("notebook")
    sns.set_style("darkgrid")
    sns.set_palette("dark")
    fig = plt.figure(figsize=(16, 7), dpi=100)
    ax1 = fig.add_subplot()

    if timeline_opt(distance, timerange, ax1):
        plt.title("distance in m per day", fontsize=20)
        plt.xlabel("Date", fontsize=13)
        plt.ylabel("distance in m", fontsize=13)
        return fig


# save the distance graph
def save_distance_graph(path):
    distance_graph(null)
    plt.savefig(path)


def elevation_graph():
    sns.set_context("notebook")
    sns.set_style("darkgrid")
    sns.set_palette("dark")
    fig = plt.figure(figsize=(16, 7))
    ax1 = fig.add_subplot()
    ax1.plot(elevation.date[::-1], elevation.value[::-1])
    ax1.set_xticks(date_xtick(elevation.date[::-1]))
    ax1.set_xticklabels(optimize_date(date_xtick(elevation.date[::-1])), rotation=15, fontsize=10)
    plt.title("elevation in m per day", fontsize=20)
    plt.xlabel("Date", fontsize=13)
    plt.ylabel("elevation", fontsize=13)
    return fig


def save_elevation_graph(path):
    elevation_graph()
    plt.savefig(path)


def steps_graph():
    sns.set_context("notebook")
    sns.set_style("darkgrid")
    sns.set_palette("dark")
    fig = plt.figure(figsize=(16, 7))
    ax1 = fig.add_subplot()
    ax1.bar(steps.date[::-1], steps.value[::-1])
    ax1.set_xticks(date_xtick(steps.date[::-1]))
    ax1.set_xticklabels(optimize_date(date_xtick(steps.date[::-1])), rotation=15, fontsize=10)
    plt.title("steps per day", fontsize=20)
    plt.xlabel("Date", fontsize=13)
    plt.ylabel("Steps", fontsize=13)
    return fig


def save_steps_graph(path):
    steps_graph()
    plt.savefig(path)


def calories_graph():
    sns.set_context("notebook")
    sns.set_style("darkgrid")
    sns.set_palette("dark")
    fig = plt.figure(figsize=(16, 7))
    ax1 = fig.add_subplot()
    ax1.plot(calories.date[::-1], calories.value[::-1])
    ax1.set_xticks(date_xtick(calories.date[::-1]))
    ax1.set_xticklabels(optimize_date(date_xtick(calories.date[::-1])), rotation=15, fontsize=10)
    plt.title("Calories burned per day", fontsize=20)
    plt.xlabel("Date", fontsize=13)
    plt.ylabel("Calories", fontsize=13)
    return fig


def save_calories_graph(path):
    calories_graph()
    plt.savefig(path)


def activities_pie():
    lst, time = Datei_Import.get_time_activities(activities)
    activity_labels = ["Walking", "Multisport", "PingPong", "Rowing", "Gym", "Swimming", "Running"]
    activity_count = []
    activity_count.append(lst.count("Walking"))
    activity_count.append(lst.count("Multi Sport"))
    activity_count.append(lst.count("Ping Pong"))
    activity_count.append(lst.count("Rowing"))
    activity_count.append(lst.count("Gym class"))
    activity_count.append(lst.count("Swimming"))
    activity_count.append(lst.count("Running"))
    sns.set_context("notebook")
    sns.set_style("darkgrid")
    sns.set_palette("dark")
    fig = plt.figure(figsize=(10, 7))
    ax1 = fig.add_subplot()
    ax1.pie(activity_count, autopct="%1.1f%%", pctdistance=1.1)
    ax1.legend(activity_labels, loc="best")
    plt.axis("equal")
    plt.title("Percentage of Activities", fontsize=20)
    return fig


def save_activities_graph(path):
    activities_pie()
    plt.savefig(path)
