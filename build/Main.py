# import pandas as pd
import Datei_Import
import Visualization
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Visualization.distance_graph()
# Visualization.step_graph()
# Visualization.elevation_graph()
# activities, calories_earned, calories_passive, distance, elevation, steps, sleep, raw_altitude, raw_calories_earned, raw_distance, raw_elevation, raw_gps_speed, raw_horizontal_radius, raw_hr, raw_lap_pool, raw_latitude, raw_longtitude, raw_sleep_state, raw_steps, raw_vertical_radius = Datei_Import.get_dataframe()

# activities = Datei_Import.clean_activities(activities)
# print(activities)
def distance_click():
    graph1 = Toplevel()
    graph1.title("Distance Graph")
    label = Label(frame, text="a generic Toplevel window")
    label.pack()
    # canvas = FigureCanvasTkAgg(Visualization.distance_graph(), graph1)
    # canvas._tkcanvas.grid(row=0, column=0)


frame = Tk()
frame.title("Withings Data Analyse Tool")
frame.geometry("400x400")
button_distance = Button(frame,text="distance graph",command=distance_click(),height=5,width=20)
button_distance.grid(row=0,column=0)

# button_step = Button(frame,text="steps graph",command=steps_click(),height=5,width=20)
# button_step.grid(row=1,column=0)

# button_elevation = Button(frame,text="elevation graph",command=elevation_click(),height=5,width=20)
# button_elevation.grid(row=2,column=0)

frame.mainloop()

