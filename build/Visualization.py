from matplotlib import pyplot as plt
import Datei_Import
import seaborn as sns

activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, raw_vertical_radius = Datei_Import.get_dataframe()


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
    date_xtick = []
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


def distance_graph():
    sns.set_context("notebook")
    sns.set_style("darkgrid")
    sns.set_palette("dark")
    fig = plt.figure(figsize=(20,10))
    ax1 = fig.add_subplot()
    plt.bar(distance.date[::-1], distance.value[::-1])
    ax1.set_xticks(date_xtick(distance.date[::-1]))
    ax1.set_xticklabels(optimize_date(date_xtick(distance.date[::-1])), rotation=15, fontsize=10)
    plt.title("distance in m per day", fontsize = 20)
    plt.xlabel("Date", fontsize = 13)
    plt.ylabel("distance in m", fontsize = 13)
    plt.savefig(Datei_Import.get_vorlage_pfad()+"distance.png")
    plt.show()
