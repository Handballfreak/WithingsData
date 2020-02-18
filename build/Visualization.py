from matplotlib import pyplot as plt
import Datei_Import

activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, raw_vertical_radius = Datei_Import.get_dataframe()

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
    complete_date_list=[]
    for date in date_list:
        split_date = date.split("-")
        month = number_months.get(split_date[1])
        complete_date = split_date[2]+" " + month + " " + split_date[0]
        complete_date_list.append(complete_date)
    return complete_date_list


def show():
    #plt.close("all")
    #plt.figure(figsize=(40,20)
    ax1 = plt.subplot()
    plt.plot(distance.date[::-1],distance.value[::-1])
    ax1.set_xticks(range(len(distance.date)))
    ax1.set_xticklabels(optimize_date(distance.date[::-1]), rotation = 90, fontsize= 7)
    plt.title("distance in m per day")
    plt.xlabel("Date")
    plt.ylabel("distance in m")
    plt.show()
