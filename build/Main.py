# import pandas as pd
import Datei_Import
import Visualization
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, raw_vertical_radius = Datei_Import.get_dataframe()

# Open Frame with the Distance Graph
def distance_click():
    graph1 = Toplevel()
    graph1.title("Distance Graph")
    canvas = FigureCanvasTkAgg(Visualization.distance_graph(), graph1)
    canvas._tkcanvas.grid(row=0, column=0)

# Open Frame with the Steps Graph
def steps_click():
    graph1 = Toplevel()
    graph1.title("Steps Graph")
    canvas = FigureCanvasTkAgg(Visualization.steps_graph(), graph1)
    canvas._tkcanvas.grid(row=0, column=0)

# Open Frame with the elevation Graph
def elevation_click():
    graph1 = Toplevel()
    graph1.title("Elevation Graph")
    canvas = FigureCanvasTkAgg(Visualization.elevation_graph(), graph1)
    canvas._tkcanvas.grid(row=0, column=0)

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

