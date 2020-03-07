from matplotlib import pyplot as plt
import Datei_Import
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import time
from datetime import date
activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude,\
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


def distance_graph(timerange):
    sns.set_context("notebook")
    sns.set_style("darkgrid")
    sns.set_palette("dark")
    fig = plt.figure(figsize=(16, 7), dpi=100)

    now = time.localtime()

    #Series to list
    datelist = distance.date.tolist()

    ax1 = fig.add_subplot()
    #no specification
    if timerange == null:
        ax1.bar(datelist[::-1], distance.value[::-1])
        ax1.set_xticks(date_xtick(datelist[::-1]))
        ax1.set_xticklabels(optimize_date(date_xtick(datelist[::-1])), rotation=15, fontsize=10)

    #in the following it is assumed that the values were recorded every day without gaps

    #last year
    elif timerange == "last_year":
        last_year = now.tm_year - 1
        start_date = str(last_year)+"-01-01"
        end_date = str(now.tm_year) + "01-01"
        #the data must contain values since the last year indicated
        try:
            start_index = datelist.index(start_date)
            end_index = datelist.index(end_date)
        except:
            start_index = 0
            try:
                end_index = 365
            except:
                #in this case the list includes less than 365 values
                end_index = len(datelist)
        ax1.bar(datelist[start_index:end_index:-1], distance.value[start_index:end_index:-1])
        ax1.set_xticks(date_xtick(datelist[start_index:end_index:-1]))
        ax1.set_xticklabels(optimize_date(date_xtick(datelist[start_index:end_index:-1])), rotation=15, fontsize=10)
    #last month
    elif timerange == "last_month":
        last_month = now.tm_month - 1
        #in case of january
        if(last_month == 0):
            last_month = 12
        start_date = str(now.tm_year) +"-"+ str(last_month) + "-01"
        end_date = str(now.tm_year) +"-"+ str(now.tm_month) + "-01"
        # the data must contain values since the last month indicated
        end_index = datelist.index(end_date)
        try:
            start_index = datelist.index(start_date)
        except:
            start_index = 0
        ax1.bar(datelist[start_index:end_index:-1], distance.value[start_index:end_index:-1])
        ax1.set_xticks(date_xtick(datelist[start_index:end_index:-1]))
        ax1.set_xticklabels(optimize_date(date_xtick(datelist[start_index:end_index:-1])), rotation=15,
                            fontsize=10)
    #last week
    elif timerange == "last_week":
        # date.today().weekday() == 0 is true if today is a monday
        monday_of_last_week = now.tm_day - date.today().weekday() - 7
        monday_of_current_week = monday_of_last_week + 7
        start_date = str(now.tm_year) + "-" + str(now.tm_month) +"-"+ monday_of_last_week
        end_date = str(now.tm_year) + "-" + str(now.tm_month) +"-"+ monday_of_current_week
        # the data must contain values since the last week indicated
        if (len(datelist) < 7):
            print("collect more data")
            ax1.bar(datelist[::-1], distance.value[::-1])
            ax1.set_xticks(date_xtick(datelist[::-1]))
            ax1.set_xticklabels(optimize_date(date_xtick(datelist[::-1])), rotation=15, fontsize=10)
        else:
            start_index = datelist.index(start_date)
            end_index = datelist.index(end_date)
            ax1.bar(datelist[start_index:end_index:-1], distance.value[start_index:end_index:-1])
            ax1.set_xticks(date_xtick(datelist[start_index:end_index:-1]))
            ax1.set_xticklabels(optimize_date(date_xtick(datelist[start_index:end_index:-1])), rotation=15,
                                fontsize=10)

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
    activity_labels = ["Walking","Multisport","PingPong","Rowing","Gym","Swimming","Running"]
    activity_count = []
    activity_count.append(lst.count("Walking"))
    activity_count.append(lst.count("Multi Sport"))
    activity_count.append(lst.count("Ping Pong"))
    activity_count.append(lst.count("Rowing"))
    activity_count.append(lst.count("Gym class"))
    activity_count.append(lst.count("Swimming"))
    activity_count.append(lst.count("Running"))
    plt.pie(activity_count, labels=activity_labels, autopct="%1.1f%%")
    plt.show()