import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import gspread
import seaborn as sns

# ------------------------------
# Google Sheets Setup
# ------------------------------

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
SHEET_NAME = "NanJason_MochiHealth_moodLogger"

@st.cache_resource
def get_gsheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds/credentials.json", SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1
    return sheet

def append_mood(timestamp, mood, note):
    sheet = get_gsheet()
    sheet.append_row([timestamp, mood, note])

def get_all_data():
    # get all the data logged - for plotting purposes
    sheet = get_gsheet()
    df = pd.DataFrame(sheet.get_all_records())
    if df.empty:
        return pd.DataFrame(columns=["Timestamp", "Mood", "Note"])
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Date"] = df["Timestamp"].dt.date
    return df

def get_today_data(df):
    # filter to only today's data
    return df[df["Date"] == pd.Timestamp.today().date()]

# Specify color for the bar plots
mood_colors = {
    "😊": "green",
    "😕": "gold",
    "😠": "red"
}
mood_order = ["😊",  "😕", "😠"]


# ------------------------------
# Streamlit App
# ------------------------------

st.set_page_config(page_title="Mood Logger", layout="centered")
st.title("Ticket Mood Logger")

# Mood input
mood = st.radio("Select Mood", ["😊", "😕", "😠"], horizontal=True)
note = st.text_input("Optional Note")
submit = st.button("Log Mood")

if submit:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    append_mood(timestamp, mood, note)
    st.success("Mood logged!")

st.markdown("---")


# Load full data
df = get_all_data()

# Visualization options
view_option = st.radio(
    "Select View",
    ["Show All Tickets", "Today Only"]
)

# Plotting

toplot = st.button("Show Plot")
if toplot:
    if view_option == "Show All Tickets":
        if df.empty:
            st.info("No mood entries found.")
        else:
            mood_counts = df["Mood"].value_counts().reindex(mood_order).fillna(0)
            colors = [mood_colors[m] for m in mood_counts.index]
            fig, ax = plt.subplots(figsize=(10, 5))
            
            sns.barplot(x=mood_counts.index, y=mood_counts.values, palette=colors, ax=ax)
            ax.set_title("All Ticket Moods")
            ax.set_ylabel("Count")
            ax.set_xlabel("Date")
            st.pyplot(fig)

    elif  view_option =="Today Only":
        df_today = df[df["Date"] == pd.Timestamp.today().date()]
        if df_today.empty:
            st.info("No mood entries logged today.")
        else:
            mood_counts = df_today["Mood"].value_counts().reindex(mood_order).fillna(0)
            colors = [mood_colors[m] for m in mood_counts.index]

            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(x=mood_counts.index, y=mood_counts.values, palette=colors, ax=ax)
            ax.set_title("Mood Distribution "+str(datetime.now().strftime("%m-%d-%Y")))
            ax.set_ylabel("Count")
            ax.set_xlabel("Mood")
            st.pyplot(fig)