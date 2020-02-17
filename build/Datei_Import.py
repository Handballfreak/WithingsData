import pandas as pd
import os

def get_pfad():
    pfad = os.getcwd()
    print(type(pfad))

def get_vorlage_pfad():
    pfad = get_pfad()
    pfad=str(pfad)
    pfad_split = pfad.split("\\")
    print(pfad_split)