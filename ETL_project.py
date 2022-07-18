#! /user/bin/python

#Dependencies
import pandas as pd
import psycopg2 as psy
import sqlalchemy as sa
#import numpy as np
from Passwords import pgadmin_password

# from /../password_folder/passwordfile import <thispassword>



#install pandas and numpy in bash
#To check to see what is installed type: which <module name>
#pip install pandas
#To check if numpy is installed: pip show numpy
#pip install numpy

#ensure csv files are not pushed to git via .gitignore



#extract data from csv
#Pandas extracts data from csv
#works in dataframes
#dataframes organize information

#Extracting Data

#Convert csv into a dataframe
parks = pd.read_csv('~/Documents/ETL Project/parks.csv')

#Testing that python loads the CSV
# print(parks)

#Splitting the df into multiple df to create multiple db table
#in order to simulate data sets that require multiple table due to size

#iloc = index locate to split into specific columns or rows 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
#<df_name>.iloc[rows, columns]

#table 1: parkinfo contants parkcode, park name, and acres

#Transform Data

parkinfo = parks.iloc[:,[0,1,3]]

#Testing parkinfo is working
#print(parkinfo)

#table 2: parklocation contants parkcode, state, Latitude, Longitude
parklocation = parks.iloc[:, [0, 2, 4, 5]]

#print(parklocation)





#load data into postgres

#Loading data to PostgreSQL

#create database in postgres to receive data and save parameters


#SQLalchemy and Psycopg2

#SQLalchemy generates SQL statements and psycopg2 sends SQL statements to the database
#SQLalchemy depends on psycopg2 or other databse drivers to communicate with the database
#SQLalchemy has two components: object-relational mapper (ORM) and core
#The core is itself a fully featured SQL abstraction toolkit
#  provides a smooth layer of abstraction over a wide variety of DBAPI implementations and behaviors
#  provides SQL Expression Language which allows expression of the SQL language through Python expressions.

#create function to create tables

#define a function that will take in a dataframe and a table name
#function connect tp postgres through psycopg2, creates a sqlachemy engine
#and uses the parameters to create a table in the park database
#using the to_sql function

def create_table(df, table_name):
    try:
#connect to postgres through psycopg2
        conn = psy.connect(host="localhost",
                        dbname="park_db",
                        user="postgres",
                        password=pgadmin_password)

#create an engine to communicate with postgres

        engine = sa.create_engine('postgresql+psycopg2://postgres:'+pgadmin_password+'@localhost:5432/park_db')
#testing engine connection, prints engine object
        print(engine)
   
#use the to_sql function to create a table
        df.to_sql(table_name, con=engine, index=False, if_exists='replace')

#verify that table was create
        return engine.table_names()

#raise errors in connection or function
    except Exception as error:
        print(error)


#Close connection and engine if success
    finally:
        conn.close()
        engine.dispose


#run queries from python to postgres


ETL = create_table(parkinfo, "parkinfo")
ETL2 = create_table(parklocation, "parklocation")



print(ETL, ETL2)
