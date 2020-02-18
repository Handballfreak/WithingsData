import pandas as pd
import Datei_Import
import Visualization

activities = Datei_Import.datei_einlesen("activities.csv")
#print(activities)

Visualization.show()
#print(Datei_Import.get_dataframe())