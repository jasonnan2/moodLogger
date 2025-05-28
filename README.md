# Mood of the Queue – Mood Logger App

This is a lightweight internal tool built with Python and Streamlit that allows support agents to log the "mood" of their support ticket queue and visualize trends over time. Moods are recorded via emoji input, stored in Google Sheets, and displayed with customizable visual summaries.

---

## ✅ Features

- Emoji-based mood logging (😊 😠 😕)
- Optional notes for each entry (e.g., “lots of Rx delays today”)
- Google Sheet as the backend (live and collaborative)
- Visualize mood distribution:
  - For today only
  - Full historical view
- Colored bar charts using Seaborn (happy = green, mid = yellow, angry = red)
- Clean, minimal UI with Streamlit

---

## 🚀 Demo

👉 [Deployed App on Streamlit Cloud](https://jasonnan2-moodlogger-mochihealth-moodlogger-jt2nm3.streamlit.app/)

📊 [Linked Google Sheet](https://docs.google.com/spreadsheets/d/1eKCxOPorMe_b8YhgplvpVgEYLUyMt7B9uYsQPPbhTNw/edit?usp=sharing)

---

## 🛠 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io)
- **Backend/Storage**: [Google Sheets](https://developers.google.com/sheets/api)
- **Visualization**: `matplotlib`, `seaborn`
- **Authentication**: Service account credentials with `gspread`

---

## 📂 Project Structure

```bash
mood-logger/
├── mochiHealth_moodLogger.py                      # Main Streamlit app
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignore credentials and cache
├── README.md                   # This file
└── .streamlit/
    └── config.toml             # Streamlit Cloud config
