# import pandas as pd
from datetime import datetime
import Datei_Import
import Visualization
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

read_path = Datei_Import.get_vorlage_pfad()

# import ctypes
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# print(screensize)
from datetime import date


# def get_standard_path_save():
# pfad = Datei_Import.get_pfad()
# pfad_split = pfad.split("\\")
# standard_path_save = pfad_split[0] + "\\" + pfad_split[1] + "\\" + pfad_split[2] + "\\pictures"
# return standard_path_save


def set_standard_save_path():
    global standard_path_save
    standard_path_save = filedialog.askdirectory()
    var_file = open(read_path + "var.txt", "w")
    var_file.write("Standard Save:" + standard_path_save)
    # print(standard_path_save)


standard_path_save = ""
var_file = open(read_path + "var.txt", "r")
line = var_file.readline()
split_first_line = line.split(":")[1:]
standard_path_save += split_first_line[0] + ":"
for i in range(1, len(split_first_line)):
    standard_path_save += split_first_line[i]

activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, raw_calories_earned, \
raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, raw_lap_pool, raw_latitude, raw_longtitude, \
raw_sleep_state, raw_steps, raw_vertical_radius = Datei_Import.get_dataframe()

# print(Datei_Import.get_walking(activities))
# print(Datei_Import.get_rowing(activities))
# print(Datei_Import.get_gym(activities))
# print(Datei_Import.get_swimming(activities))
# print(Datei_Import.get_running(activities))
# print(Datei_Import.get_calories())
lst, time = Datei_Import.get_time_activities(activities)
print(len(lst))
print(time)
Visualization.activities_pie()


def save_steps_click():
    frame.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                  filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    Visualization.save_steps_graph(frame.filename)


def standard_save_steps():
    print(standard_path_save)
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M")
    Visualization.save_steps_graph(standard_path_save + "\\" + "steps" + timestamp + ".png")


def save_distance_click():
    frame.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                  filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    Visualization.save_distance_graph(frame.filename)


def standard_save_distance():
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M")
    Visualization.save_distance_graph(standard_path_save + "\\" + "distance" + timestamp + ".png")


def save_elevation_click():
    frame.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                  filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    Visualization.save_elevation_graph(frame.filename)


def standard_save_elevation():
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M")
    Visualization.save_elevation_graph(standard_path_save + "\\" + "elevation" + timestamp + ".png")


def save_calories_click():
    frame.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                  filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    Visualization.save_calories_graph(frame.filename)


def standard_save_calories():
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M")
    Visualization.save_calories_graph(standard_path_save + "\\" + "calories" + timestamp + ".png")


# Open Frame with the Distance Graph
def distance_click():
    graph1 = Toplevel()
    graph1.title("Distance Graph")
    canvas = FigureCanvasTkAgg(Visualization.distance_graph(null), graph1)
    canvas._tkcanvas.grid(row=1, column=1)
    menubar = Menu(graph1)
    graph1.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    # In einem Standardpfad speichern
    filemenu.add_command(label="Save", command=standard_save_distance)
    # Speichern unter festgelegtem Namen und Pfad
    filemenu.add_command(label="Save as", command=save_distance_click)

    timeline_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Timeline", menu=timeline_menu)
    # last 7 days
    timeline_menu.add_command(label="last week", command=last_week_click)
    # last month
    timeline_menu.add_command(label="last month", command=None)
    # last year
    timeline_menu.add_command(label="last year", command=None)

def last_week_click():
    graph1 = Toplevel()
    graph1.title("Distance Graph")
    timerange = null
    canvas = FigureCanvasTkAgg(Visualization.distance_graph("last week"), graph1)
    canvas._tkcanvas.grid(row=1, column=1)
    menubar = Menu(graph1)
    graph1.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    # In einem Standardpfad speichern
    filemenu.add_command(label="Save", command=standard_save_distance)
    # Speichern unter festgelegtem Namen und Pfad
    filemenu.add_command(label="Save as", command=save_distance_click)

    timeline_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Timeline", menu=timeline_menu)
    # last 7 days
    timeline_menu.add_command(label="last week", command=last_week_click)
    # last month
    timeline_menu.add_command(label="last month", command=None)
    # last year
    timeline_menu.add_command(label="last year", command=None)

# Open Frame with the Steps Graph
def steps_click():
    graph1 = Toplevel()
    graph1.title("Steps Graph")
    canvas = FigureCanvasTkAgg(Visualization.steps_graph(), graph1)
    canvas._tkcanvas.grid(row=1, column=1)
    menubar = Menu(graph1)
    graph1.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    # In einem Standardpfad speichern
    filemenu.add_command(label="Save", command=standard_save_steps)
    # Speichern unter festgelegtem Namen und Pfad
    filemenu.add_command(label="Save as", command=save_steps_click)

    timeline_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Timeline", menu=timeline_menu)
    # last 7 days
    timeline_menu.add_command(label="last week", command=None)
    # last month
    timeline_menu.add_command(label="last month", command=None)
    # last year
    timeline_menu.add_command(label="last year", command=None)


# Open Frame with the elevation Graph
def elevation_click():
    graph1 = Toplevel()
    graph1.title("Elevation Graph")
    canvas = FigureCanvasTkAgg(Visualization.elevation_graph(), graph1)
    canvas._tkcanvas.grid(row=1, column=1)
    menubar = Menu(graph1)
    graph1.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    # In einem Standardpfad speichern
    filemenu.add_command(label="Save", command=standard_save_elevation)
    # Speichern unter festgelegtem Namen und Pfad
    filemenu.add_command(label="Save as", command=save_elevation_click)

    timeline_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Timeline", menu=timeline_menu)
    # last 7 days
    timeline_menu.add_command(label="last week", command=None)
    # last month
    timeline_menu.add_command(label="last month", command=None)
    # last year
    timeline_menu.add_command(label="last year", command=None)


def calories_click():
    graph1 = Toplevel()
    graph1.title("Calories Graph")
    canvas = FigureCanvasTkAgg(Visualization.calories_graph(), graph1)
    canvas._tkcanvas.grid(row=1, column=1)
    menubar = Menu(graph1)
    graph1.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    # In einem Standardpfad speichern
    filemenu.add_command(label="Save", command=standard_save_calories)
    # Speichern unter festgelegtem Namen und Pfad
    filemenu.add_command(label="Save as", command=save_calories_click)

    timeline_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Timeline", menu=timeline_menu)
    # last 7 days
    timeline_menu.add_command(label="last week", command=None)
    # last month
    timeline_menu.add_command(label="last month", command=None)
    # last year
    timeline_menu.add_command(label="last year", command=None)


# Main frame
frame = Tk()
frame.title("Withings Data Analyse Tool")
frame.geometry("400x400")

# button to produce distance graph
button_distance = Button(frame, text="distance graph", command=distance_click, height=5, width=20)
button_distance.grid(row=0, column=0)

# button to produce steps graph
button_step = Button(frame, text="steps graph", command=steps_click, height=5, width=20)
button_step.grid(row=1, column=0)

# button to produce elevation graph
button_elevation = Button(frame, text="elevation graph", command=elevation_click, height=5, width=20)
button_elevation.grid(row=2, column=0)

button_calories = Button(frame, text="calories graph", command=calories_click, height=5, width=20)
button_calories.grid(row=3, column=0)

# button to set standard save directory
button_standard_save = Button(frame, text="Set Standard Save-Directory", command=set_standard_save_path, height=5,
                              width=20)
button_standard_save.grid(row=0, column=1)
frame.mainloop()
