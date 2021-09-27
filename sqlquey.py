from sqlalchemy import create_engine
import pandas as pd

engine= create_engine("sqlite:///Northwind.sqlite")
con = engine.connect()
rs = con.execute("SELECT * FROM Orders")
df = pd.Dataframe(rs.fetchall())
con.close()
print(df.head())