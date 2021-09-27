from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Northwind.sqlite")

with engine.connect() as con
    rs = con.execute("select * from Orders")
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()