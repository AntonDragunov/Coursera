import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("postgresql+psycopg2://postgres:111@127.0.0.1/Nokian")
#engine = create_engine("postgresql+psycopg2://gen_user:vnyk4p2jf1@5.23.55.46/5432/default_db")

with pd.ExcelFile('K5.xlsx') as xls:

    #'records.xlsx', sheet_name='Numbers', header=None

    df = pd.read_excel(xls)

with pd.ExcelFile('DEALER_PRICE_LIST.xlsx') as xls:
    df1 = pd.read_excel(xls)

