import pandas as pd

from anonymize import anonymize
from saveToCSV import saveDataToCSV
def startAnonymize():
    df = pd.read_csv("./preAnonymize.csv")
    data = anonymize( df , 'Users' )
    saveDataToCSV( data , 'Users' )