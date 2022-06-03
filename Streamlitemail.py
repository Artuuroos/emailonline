import smtplib, ssl
import pandas as pd
import streamlit as st


st.subheader("Benachrichtigung anfordern")
emailteil1=st.text_input("Emailnamen eingeben")
emaildomains=["@gmail.com","@gmx.de","@web.de"]

option = st.selectbox('Email Domain auswählen', emaildomains)
ganzeemail=emailteil1+option

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "dbtickeralert@gmail.com"
receiver_email = ganzeemail
password = "ujbdfkbgqwbjemrh"
message = """\
Subject: Neuer Preis DB 

Ein neuer Preis ihrer Verbindung ist verfuegbar.
Kaufen Sie sich ein Ticket.

Freundlicher Gruss
DBTickeralert"""

zahl=st.number_input("Preis: ",min_value=1,max_value=11,step=1) 
st.write("Ihr angegebener Preis: ", zahl,"€")
liste=[1,2,3,4,5,6,7,8,9,10]

with st.form(key='form1'):
    submit_button = st.form_submit_button(label='Submit1')
    
    if submit_button:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            for i in range(len(liste)):
                if liste[i]<=zahl:
                    server.sendmail(sender_email, receiver_email, message)
                else:
                    if zahl>liste[i]:
                        st.write("Es gibt kein Ticket für diesen Preis")

