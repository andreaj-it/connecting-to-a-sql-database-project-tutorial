import os

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

cursor.execute("""
                INSERT INTO publishers(publisher_id,name) values (1,'O Reilly Media');
                INSERT INTO publishers(publisher_id,name) values (2,'A Book Apart');
                INSERT INTO publishers(publisher_id,name) values (3,'A K PETERS');
                INSERT INTO publishers(publisher_id,name) values (4,'Academic Press');
                INSERT INTO publishers(publisher_id,name) values (5,'Addison Wesley');
                INSERT INTO publishers(publisher_id,name) values (6,'Albert&Sweigart');
                INSERT INTO publishers(publisher_id,name) values (7,'Alfred A. Knopf');
                """)

conn.commit()
conn.close()