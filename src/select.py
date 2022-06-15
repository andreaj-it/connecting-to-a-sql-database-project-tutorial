
import os

#pip install pandas
import pandas as pd

#pip install python-dotenv
from dotenv import load_dotenv 

import psycopg2

load_dotenv()

conn = psycopg2.connect(
                       database = os.getenv('DB_NAME'),
                       user = os.getenv('DB_USER'),
                       password = os.getenv('DB_PASSWORD'),
                       host =os.getenv('DB_HOST'),
                       port = os.getenv('DB_PORT')
                       )


cursor = conn.cursor()

#cursor.execute("""
#                SELECT * FROM publishers;
#            """)

df = pd.read_sql("SELECT * FROM publishers;",conn)

print(df)

conn.commit()
conn.close()