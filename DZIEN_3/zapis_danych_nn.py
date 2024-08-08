import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import mysql

#przykładowe dane z predykcji sieci neurnowej (zalecane użycie tablicy numpy.ndarray)

predictions = np.array([112.3,34.3543,2.4,0.45,13,134,-564.3435,99,])

df = pd.DataFrame(predictions,columns=['Predictions'])

#zapis do csv
df.to_csv("pred.csv",index=False)

#zapis do txt
np.savetxt("pred.txt",predictions)

user = 'root'
password = 'abc123'
host = '127.0.0.1'
port = '3306'
database = 'bazatestowa'

#utworzenie połączenia URI
connction_string = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"

#utwórz silnik połączenia
engine = create_engine(connction_string)
#zapis DF do tabeli sql
table_name = 'pred'
df.to_sql(table_name,engine,if_exists='replace',index=False)

