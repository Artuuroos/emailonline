import pandas
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests
import csv
import time
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px
import plotly
from matplotlib import dates as mpl_dates
from cProfile import label
from distutils.cmd import Command
import datetime
from streamlit.cli import main
from streamlit.proto.RootContainer_pb2 import RootContainer
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

try:
            conn = psycopg2.connect(dbname="dbticket", user="postgres", password="123456")
            engine = create_engine('postgresql://postgres:123456@localhost:5432/dbticket')
            cursor = conn.cursor()

except:

            print('Fehler bei der DB Verbindung !')

#scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
        #'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets']
#creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\momo\PycharmProjects\streamlit\creds.json', scope)
#client = gspread.authorize(creds)
#st.set_page_config(page_title="My Website", layout="wide")

st.subheader("Hi unsere Website")
st.title("Datenanalyse")
#spreadsheet = client.open("test")
#gc = gspread.service_account(filename=r"C:\Users\momo\PycharmProjects\streamlit\creds.json")
#sheet = gc.open("test").sheet1
#sheet.insert_row(["anfrage", "alter_1", "bahnkarteneu", "start", "ziel", "datum", "abfahrt_zv1", "ankunft_zv1", "art_zug_zv1",
                  #  "sparpreis2_zv1"])
result=pandas.DataFrame(columns=["anfrage", "alter_1", "bahnkarteneu", "start", "ziel", "datum", "abfahrt_zv1", "ankunft_zv1", "art_zug_zv1",
                    "sparpreis2_zv1"])

st.write("Digital Lab")
optionliste = ["", 'Darmstadt Hbf',
               "Wiesbaden Hbf",
               "Hanau Hbf",
               "Frankenthal Hbf",
               "Kaiserslautern Hbf",
               "Pirmasens Hbf",
               "Speyer Hbf",
               "Zweibrücken Hbf",
               "Kassel Hbf",
               "Boppard Hbf",
               "Koblenz Hbf",
               "Wittlich Hbf",
               "Mainz Hbf",
               "Worms Hbf",
               "Saarbrücken Hbf",
               "Saarlouis Hbf",
               "Trier Hbf",
               "Braunschweig Hbf",
               "Hildesheim Hbf",
               "Wolfsburg Hbf",
               "Bremen Hbf",
               "Bremerhaven Hbf",
               "Emden Hbf",
               "Osnabrück Hbf",
               "Hamburg Hbf",
               "Hannover Hbf",
               "Kiel Hbf",
               "Lübeck Hbf",
               "Cottbus Hbf",
               "Brandenburg Hbf",
               "Eberswalde Hbf",
               "Potsdam Hbf",
               "Neustrelitz Hbf",
               "Rostock Hbf",
               "Stralsund Hbf",
               "Schwerin Hbf",
               "Augsburg Hbf",
               "Lindau Hbf",
               "Bayreuth Hbf",
               "Hof Hbf",
               "München Hbf",
               "Nürnberg Hbf",
               "Deggendorf Hbf",
               "Passau Hbf",
               "Regensburg Hbf",
               "Berchtesgaden Hbf",
               "Ingolstadt Hbf",
               "Aschaffenburg Hbf",
               "Schweinfurt Hbf",
               "Würzburg Hbf",
               "Chemnitz Hbf",
               "Gera Hbf",
               "Dresden Hbf",
               "Arnstadt Hbf",
               "Erfurt Hbf",
               "Merseburg Hbf",
               "Döbeln Hbf",
               "Leipzig Hbf",
               "Bernburg Hbf",
               "Dessau Hbf",
               "Magdeburg Hbf",
               "Stendal Hbf",
               "Thale Hbf",
               "Wernigerode Hbf",
               "Lörrach Hbf",
               "Reutlingen Hbf",
               "Tübingen Hbf",
               "Freudenstadt Hbf",
               "Karlsruhe Hbf",
               "Pforzheim Hbf",
               "Bad Friedrichshall Hbf",
               "Heidelberg Hbf",
               "Heilbronn Hbf",
               "Mannheim Hbf",
               "Öhringen Hbf",
               "Stuttgart Hbf",
               "Aalen Hbf",
               "Ulm Hbf",
               "Bielefeld Hbf",
               "Gütersloh Hbf",
               "Paderborn Hbf",
               "Dortmund Hbf",
               "Lünen Hbf",
               "Bottrop Hbf",
               "Duisburg Hbf",
               "Krefeld Hbf",
               "Oberhausen Hbf",
               "Aachen Hbf",
               "Düsseldorf Hbf",
               "Eschweiler Hbf",
               "Gevelsberg Hbf",
               "Mönchengladbach Hbf",
               "Neuss Hbf",
               "Remscheid Hbf",
               "Rheydt Hbf",
               "Solingen Hbf",
               "Wuppertal Hbf",
               "Bochum Hbf",
               "Castrop-Rauxel Hbf",
               "Essen Hbf",
               "Gelsenkirchen Hbf",
               "Wanne-Eickel Hbf",
               "Witten Hbf",
               "Hagen Hbf",
               "Siegen Hbf",
               "Bonn Hbf",
               "Köln Hbf",
               "Recklinghausen Hbf"
               ]

bahnkarteliste = ["25", "50", "nein"]
optionliste.sort()

option = st.selectbox('Startbahnhof auswählen', optionliste)
st.write('Startbahnhof ist:', option)

losdatum = st.date_input('Datum', value=pd.to_datetime("today"))
st.write("Datum:", losdatum.strftime("%d.%m.%Y"))

uhrzeit_stunde1 = st.number_input("Stunde: ", min_value=1, max_value=24, step=1)
st.write("Stunde: ", uhrzeit_stunde1)

uhrzeit_minuten1 = st.number_input("Minute: ", min_value=1, max_value=59, step=1)
st.write("Minute: ", uhrzeit_minuten1)

alter_1 = st.number_input("Alter: ", min_value=1, max_value=110, step=1)
st.write("Alter: ", alter_1)

bahnkarteneu = st.selectbox("Bahnkarte:", bahnkarteliste)
st.write("Bahnkarte:", bahnkarteneu)

zielbahn = st.selectbox("Zielbahnhof auswählen", optionliste)
st.write("Ihr Zielbahnhof ist:", zielbahn)

with st.form(key='form1'):
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    start = option
    ziel = zielbahn
    datum = losdatum.strftime("%d.%m.%Y")
    uhrzeit_stunde = str(uhrzeit_stunde1)
    uhrzeit_minuten = str(uhrzeit_minuten1)

    uhrzeit_minuten = str(uhrzeit_minuten1)

    st.write("Die Excel-Datei wird erstellt:")

# alter_f=str(list(range(15,5,-1)))
# alter_y=str(list(range(26,13,-1)))
# alter_e=str(list(range(64,26,-1)))
# alter_s=str(list(range(110,64,-1)))


# uhrzeit_stunde= input("Uhrzeit(Stunde): ")
# uhrzeit_minuten= input("Uhrzeit(Minuten): ")
# alter_1=input("Wie alt sind sie? ")

if alter_1 in range(15, 5, -1):
    alter = "f"
else:
    if alter_1 in range(26, 13, -1):
        alter = "y"
    else:
        if alter_1 in range(64, 26, -1):
            alter = "e"
        else:
            alter = "s"

if bahnkarteneu == "50":
    bahnkarte = "4"
else:
    if bahnkarteneu == "25":
        bahnkarte = "2"
    else:
        bahnkarte = "0"

#spreadsheet = client.open("test")
#gc = gspread.service_account(filename=r"C:\Users\momo\PycharmProjects\streamlit\creds.json")
#sheet = gc.open("test").sheet1
#sheet.append_row(["anfrage", "alter_1", "bahnkarteneu", "start", "ziel", "datum", "abfahrt_zv1", "ankunft_zv1", "art_zug_zv1",
                 #   "sparpreis2_zv1"])
while True:

    url = 'https://reiseauskunft.bahn.de/bin/query.exe/dn?revia=yes&existOptimizePrice-deactivated=1&country=DEU&dbkanal_007=L01_S01_D001_qf-bahn-svb-kl2_lz03&start=1&protocol=https%3A&REQ0JourneyStopsS0A=1&S=' + start + '&REQ0JourneyStopsSID=A%3D1%40O%3DM%C3%BCnchen+Hbf%40X%3D11558339%40Y%3D48140229%40U%3D80%40L%3D008000261%40B%3D1%40p%3D1652295202%40&REQ0JourneyStopsZ0A=1&Z=' + ziel + '&REQ0JourneyStopsZID=A%3D1%40O%3DAachen+Hbf%40X%3D6091495%40Y%3D50767803%40U%3D80%40L%3D008000001%40B%3D1%40p%3D1652295202%40&date=Fr%2C+' + datum + '&time=' + uhrzeit_stunde + '%3A' + uhrzeit_minuten + '&timesel=depart&returnDate=&returnTime=&returnTimesel=depart&optimize=0&auskunft_travelers_number=1&tariffTravellerType.1=' + alter + '&tariffTravellerReductionClass.1=' + bahnkarte + '&tariffClass=2&rtMode=DB-HYBRID&externRequest=yes&HWAI=JS%21js%3Dyes%21ajax%3Dyes%21&externRequest=yes&HWAI=JS%21js%3Dyes%21ajax%3Dyes%21#hfsseq1|gl.0263982.1652621988'
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    zugverbindungen = soup.find("div", class_="resultContentHolder")
    zugverbindung1 = zugverbindungen.find("div", class_="connectionData")
    stationen_zugverbindung1 = zugverbindung1.find("div", class_="connectionStations").get_text(strip=True)
    uhrzeit_zv1 = zugverbindung1.find("div", class_="connectionTime")
    abfahrt_zv1 = uhrzeit_zv1.find("div", class_="time timeDep").get_text(strip=True)
    ankunft_zv1 = uhrzeit_zv1.find("div", class_="time timeArr").get_text(strip=True)
    art_zug_zv1 = soup.find("div", class_="products").get_text(strip=True)
    preis_zv1 = soup.find("div", class_="overviewConnection")
    sparpreis_zv1 = preis_zv1.find("div", class_="connectionPrice").get_text(strip=True)
    sparpreis2_zv1 = sparpreis_zv1.replace("ab", "")

    if "THA" in art_zug_zv1:

        print(
            "Diese Zugverbindung wird nicht von uns unterstüzt. Bitte wählen Sie eine Verbindung der Züge von der DB.")
        break

    else:
        if "VRS-Tarif" in sparpreis_zv1:

            print("Hier ist kein Vergleich notwendig, da diese Verbindung zu VRS-Tarifen angeboten wird.")
            break

        else:

            anfrage = time.strftime("%d.%m. %H:%M")
            print(anfrage)
            print("Stationen: ", stationen_zugverbindung1)
            print("Fahrzeit: ", abfahrt_zv1, ankunft_zv1)
            print("Art des Zuges/der Züge: ", art_zug_zv1)
            print("Die Verbindung kostet: ", sparpreis_zv1)

    result.loc[len(result)]=[str(anfrage), alter_1, bahnkarteneu, start, ziel, datum, abfahrt_zv1, ankunft_zv1, art_zug_zv1,
                     sparpreis2_zv1]
    result.to_sql(name="tabelle1", con=engine, if_exists="append" )
    result=result[0:0]
    #sheet.append_row([str(anfrage), alter_1, bahnkarteneu, start, ziel, datum, abfahrt_zv1, ankunft_zv1, art_zug_zv1,
                #    sparpreis2_zv1])
            #with open('test_code23.csv', 'a', newline='') as f:
          #      writer = csv.writer(f, delimiter=';')
           #     writer.writerow(
            #        [anfrage, alter_1, bahnkarteneu, start, ziel, datum, abfahrt_zv1, ankunft_zv1, art_zug_zv1,
             #        sparpreis2_zv1])

    sleep(18)






