from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("postgresql+psycopg2://postgres:111@127.0.0.1/Nokian")
#engine = create_engine("postgresql+psycopg2://gen_user:vnyk4p2jf1@5.23.55.46/5432/default_db")
date = datetime.now()

with pd.ExcelFile('free_stock.xlsx') as xls:

    #'records.xlsx', sheet_name='Numbers', header=None

    df = pd.read_excel(xls)
    df['cur_year'] = f'{date.year}'
    df['cur_month'] = f'{date.month}'
    df['cur_day'] = f'{date.day}'

    df.to_sql(name='vist_daily', con=engine, if_exists='append', index=False)
