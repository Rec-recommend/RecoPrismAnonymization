import pandas as pd

from anonymize import anonymize
from saveToCSV import saveDataToCSV

df = pd.read_csv("./titanic_train.csv")

data = anonymize( df , 'Users' )

saveDataToCSV( data , 'Users' )