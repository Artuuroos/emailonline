import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import smtplib, ssl
import requests
import streamlit as st
import time
import yagmail
import schedule
import time
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                        database="dbticket", 
                        user="dbticket_user", 
                        password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
global cursor 
cur = conn.cursor()
a=1
def show_name():
  if a <1000:
    with st.form("log"+a):
      loginn=st.text_input("Email-Adresse: ")
      loginp=st.text_input("Passwort: ",type="password")
      submit=st.form_submit_button("Ja")
    if submit:
      result=pandas.DataFrame(columns=["username","tabelle"])
      result.loc[len(result)]=[loginn,loginp]
      result.to_sql(name="offline", con=engine, if_exists="append")
      result=result[0:0]
      st.info("1.")
      st.info("2.")
    
    
schedule.every(8).seconds.do(show_name)

while 1:
    schedule.run_pending()
    time.sleep(1) 
           
                      
        



    
   
        

        



