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



optionen2 = option_menu(menu_title=None,
                       options=["Home","Diagramm","Price","Notifi"],
                       icons=["house","graph-up","clock","alarm"],
                       menu_icon="cast",
                       default_index=0,
                       orientation="horizontal",
                       )


if optionen2=="Home":
    st.write("Homepage")
    
else:
    if optionen2=="Diagramm":
        with st.sidebar:
            optionenside= option_menu(menu_title=None,
            options=["Liniendiagramm","Säulendiagramm"],
            icons=["graph-up","bar-chart-line"],
            menu_icon="",
            default_index=0,
            orientation="vertical",
        )
        if optionenside=="Liniendiagramm":
            st.write("Hier kommt ein Liniendiagramm hin")
            with st.form(key='form1'):
                submit_button = st.form_submit_button(label='Graph ansehen')
            if submit_button:
                fig = px.line(        
                df, #Data Frame
                x = "Scan", #Columns from the data frame
                y = "Preis",
                title = "Preisgraph"
            )
                fig.update_traces(line_color = "skyblue")
                st.plotly_chart(fig)
           
        else:
            st.write("Hier kommt ein Säulendiagramm hin")
            with st.form(key='form1'):
                submit_button1 = st.form_submit_button(label='Graph ansehen')
            if submit_button1:
                fig = px.bar(        
                df, #Data Frame
                x = "Scan", #Columns from the data frame
                y = "Preis",
                title = "Preisgraph"
            )
                fig.update_traces(line_color = "skyblue")
                st.plotly_chart(fig) 
       
        
    if optionen2=="Price":
        st.write("Preisantizipation")
        
    if optionen2=="Notifi":
        
        st.subheader("Benachrichtigung anfordern")
        emailteil1=st.text_input("Emailnamen eingeben")
        emaildomains=["@gmail.com","@gmx.de","@web.de"]

        option = st.selectbox('Email Domain auswählen', emaildomains)
        ganzeemail=emailteil1+option

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        yag = yagmail.SMTP("dbtickeralert@gmail.com","ujbdfkbgqwbjemrh")
        contents = [
        "Ein neuer Preis ihrer Verbindung ist verfuegbar."
        "\n"
        "Kaufen Sie sich ein Ticket."
        "\n"

        "Freundlicher Gruss"
        "\n"
        "DBTickeralert"
        ]
        liste=[1,2,3,4,5,6,7,8,9,10]

                
        preisangabe = st.slider("Ihr gewünschter Höchstpreis:")
        with st.form(key='form1'):
                submit_buttonpreis = st.form_submit_button(label='Benachrichtige mich')    
                if submit_buttonpreis:
                    st.write("Sie erhalten eine Email Benachrichitung wenn sich der Preis unter",preisangabe ,"€ befindet") 
                    for i in range(len(liste)):
                      if liste[i]<=preisangabe:
                        yag.send(to=ganzeemail,
                        subject='Neuer Preis',
                        contents=contents)
                      else:
                        if preisangabe>liste[i]:
                          st.write("Ihre Kaufbereitschaft ist sehr hoch") 
           
                      
        



    
   
        

        



