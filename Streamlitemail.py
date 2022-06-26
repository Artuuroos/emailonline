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


def show_name():
    
    st.info("1.")
    st.info("2.")
    
    
schedule.every(8).seconds.do(show_name)

while 1:
    schedule.run_pending()
    time.sleep(1) 
           
                      
        



    
   
        

        



