# coding: UTF-8
import pyodbc
import pandas as pd

# データベースに接続してSQL文を実行する関数
def ReadQueryBySQLServer(sql, env):
    config = r"DRIVER={SQL Server};"
    # .envファイルに記載した情報を基に接続情報を設定
    config = config + "SERVER={0};DATABASE={1};UID={2};PWD={3};".format(
        env[0], env[1], env[2], env[3]
    )
    # 接続
    con = pyodbc.connect(config)
    # SQLを実行
    df = pd.io.sql.read_sql(sql, con)
    # 切断
    con.close()
    # pandasのデータフレームを返す
    return df
