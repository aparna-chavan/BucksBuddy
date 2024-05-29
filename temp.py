from imports import *
import keys

conn = keys.get_snowflake_conn()
cur = conn.cursor()
sql = 'select "ticker", "d" from "company_info"'
cur.execute(sql)
df2 = cur.fetch_pandas_all()

print(df2)