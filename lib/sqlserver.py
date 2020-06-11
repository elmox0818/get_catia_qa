# coding: UTF-8
import pyodbc
import pandas as pd

# データベースに接続してSQL文を実行する関数
def ReadQueryBySQLServer(sql, env):
    config = r"DRIVER={SQL Server};"
    config = config + "SERVER={0};DATABASE={1};UID={2};PWD={3};".format(
        env[0], env[1], env[2], env[3]
    )
    con = pyodbc.connect(config)
    df = pd.io.sql.read_sql(sql, con)
    con.close()
    return df
