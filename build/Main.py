# import pandas as pd
import Datei_Import
import Visualization
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)

activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, raw_vertical_radius = Datei_Import.get_dataframe()
# print(Datei_Import.get_walking(activities))

def save_click():
    print("Test")
# Open Frame with the Distance Graph
def distance_click():
    graph1 = Toplevel()
    graph1.title("Distance Graph")
    canvas = FigureCanvasTkAgg(Visualization.distance_graph(), graph1)
    canvas._tkcanvas.grid(row=1, column=1)
    menubar = Menu(graph1)
    graph1.config(menu = menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Save",menu=filemenu)
    filemenu.add_command(label="Test",command = save_click)



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
    filemenu.add_command(label="Save", command=save_click)
    # Speichern unter festgelegtem Namen und Pfad
    filemenu.add_command(label="Save as", command=None)

    timeline_menu = Menu(menubar, tearoff= 0)
    menubar.add_cascade(label="Timeline",menu=timeline_menu)
    # last 7 days
    timeline_menu.add_command(label="last week",command = None)
    #last month
    timeline_menu.add_command(label="last month", command=None)
    #last year
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
    menubar.add_cascade(label="Save", menu=filemenu)
    filemenu.add_command(label="Test", command=save_click)
# Main frame
frame = Tk()
frame.title("Withings Data Analyse Tool")
frame.geometry("400x400")

# button to produce distance graph
button_distance = Button(frame,text="distance graph",command=distance_click,height=5,width=20)
button_distance.grid(row=0,column=0)

# button to produce steps graph
button_step = Button(frame,text="steps graph",command=steps_click,height=5,width=20)
button_step.grid(row=1,column=0)

# button to produce elevation graph
button_elevation = Button(frame,text="elevation graph",command=elevation_click,height=5,width=20)
button_elevation.grid(row=2,column=0)

frame.mainloop()

