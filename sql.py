from sqlalchemy import create_engine
import pandas as pd

with create_engine as con:
    rs = con.execute("select lastName, title from employee")
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.colums=rs.key()

    print(len(df))
    print(df.head())