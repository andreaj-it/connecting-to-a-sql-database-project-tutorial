
import os
import sqlalchemy as sql
import pymysql
import pandas as pd
#import python-dotenv


# 1) Connect to the database here using the SQLAlchemy's create_engine function
def connect():
    global engine # this allows us to use a global variable called engine
    # A "connection string" is basically a string that contains all the databse credentials together
    connection_string = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    #connection_string ="" #el compañero pasa el string directo porque el anterior no lo estaba tomando del .env preguntar a Camila como lo resolvio ?
    print("Starting the connection...")
    engine = sql.create_engine(connection_string)
    engine.connect()
    return engine

#print(os.getenv('DB_USER')) 
#print(os.environ)

connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
engine.execute(""" 
    CREATE TABLE publishers(
        publisher_id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        PRIMARY KEY(publisher_id)
    );
    CREATE TABLE authors(
        author_id INT NOT NULL,
        first_name VARCHAR(100) NOT NULL,
        middle_name VARCHAR(50) NULL,
        last_name VARCHAR(100) NULL,
        PRIMARY KEY(author_id)
    );
    CREATE TABLE books(
        book_id INT NOT NULL,
        title VARCHAR(255) NOT NULL,
        total_pages INT NULL,
        rating DECIMAL(4, 2) NULL,
        isbn VARCHAR(13) NULL,
        published_date DATE,
        publisher_id INT NULL,
        PRIMARY KEY(book_id),
        CONSTRAINT fk_publisher FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
    );
    CREATE TABLE book_authors (
        book_id INT NOT NULL,
        author_id INT NOT NULL,
        PRIMARY KEY(book_id, author_id),
        CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES books(book_id) ON DELETE CASCADE,
        CONSTRAINT fk_author FOREIGN KEY(author_id) REFERENCES authors(author_id) ON DELETE CASCADE
    );""")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
engine.execute("""
    INSERT INTO publishers(publisher_id,name) values (1,'O Reilly Media');
    INSERT INTO publishers(publisher_id,name) values (2,'A Book Apart');
    INSERT INTO publishers(publisher_id,name) values (3,'A K PETERS');
    INSERT INTO publishers(publisher_id,name) values (4,'Academic Press');
    INSERT INTO publishers(publisher_id,name) values (5,'Addison Wesley');
    INSERT INTO publishers(publisher_id,name) values (6,'Albert&Sweigart');
    INSERT INTO publishers(publisher_id,name) values (7,'Alfred A. Knopf');
""")

engine.execute("""
    INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (1,'Merritt',null,'Eric');
    INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (2,'Linda',null,'Mui');
    INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (3,'Alecos',null,'Papadatos');
    INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (4,'Anthony','Molinaro');
    INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (5,'David',null,'Cronin');
    INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (6,'Richard',null,'Blum');
    INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (7,'Yuval','Noah','Harari');
    INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (8,'Paul',null,'Albitz');

    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (1,'Lean Software Development: An Agile Toolkit',240,4.17,'9780320000000','2003-05-18',5);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (2,'Facing the Intelligence Explosion',91,3.87,null,'2013-02-01',7);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (3,'Scala in Action',419,3.74,'9781940000000','2013-04-10',1);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (4,'Patterns of Software: Tales from the Software Community',256,3.84,'9780200000000','1996-08-15',1);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (5,'Anatomy Of LISP',446,4.43,'9780070000000','1978-01-01',3);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (6,'Computing machinery and intelligence',24,4.17,null,'2009-03-22',4);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (7,'XML: Visual QuickStart Guide',269,3.66,'9780320000000','2009-01-01',5);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (8,'SQL Cookbook',595,3.95,'9780600000000','2005-12-01',7);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (9,'The Apollo Guidance Computer: Architecture And Operation (Springer Praxis Books / Space Exploration)',439,4.29,'9781440000000','2010-07-01',6);
    insert into books (book_id,title,total_pages,rating,isbn,published_date,publisher_id) values (10,'Minds and Computers: An Introduction to the Philosophy of Artificial Intelligence',222,3.54,'9780750000000','2007-02-13',7);

    INSERT INTO book_authors (book_id, author_id) values (8,4);
    INSERT INTO book_authors (book_id, author_id) values (8,4);
    INSERT INTO book_authors (book_id, author_id) values (8,4);
    INSERT INTO book_authors (book_id, author_id) values (8,4);
""")

# 4) Use pandas to print one of the tables as dataframes using read_sql function
authors = pd.read_sql("SELECT * FROM authors;", engine)
print(authors)
