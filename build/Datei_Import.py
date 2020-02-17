import pandas as pd
import os

def get_pfad():
    pfad = os.getcwd()
    #print(pfad)

def get_vorlage_pfad():
    pfad = get_pfad()
    pfad=str(pfad)
    pfad_split = pfad.split("W")
    print(pfad_split)