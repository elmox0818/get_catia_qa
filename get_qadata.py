# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv
from lib.sqlserver import ReadQueryBySQLServer

# 環境変数を取得する関数
def get_env():
    path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path=path)

    SERVER = os.environ.get("SERVER")
    DATABASE = os.environ.get("DATABASE")
    UID = os.environ.get("UID")
    PASSWORD = os.environ.get("PASSWORD")

    return (SERVER, DATABASE, UID, PASSWORD)


def get_export():
    # 環境変数を取得
    env = get_env()

    # 4つのテーブルに対して処理を実行
    for i in range(1, 5):
        # 1はないので表記しない
        if i == 1:
            sql = "SELECT * FROM [Catia].[dbo].[EMP_Catia]"
        # その他は採番
        else:
            sql = "SELECT * FROM [Catia].[dbo].[EMP_Catia{}]".format(str(i))
        df = ReadQueryBySQLServer(sql, env)
        _df = df.replace("\r", "", regex=True)
        _df_cleaned = _df.replace("\n", "", regex=True)
        _df_cleaned.to_csv("./results/csv/Catia{}.csv".format(str(i)))


def main():
    get_export()


if __name__ == "__main__":
    main()
