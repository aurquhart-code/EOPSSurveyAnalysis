import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="EOPS Survey Dashboard", layout="wide")

DATA_DIR = Path("data")

TERM_FILES = {
    "FA-21": "FA-21.csv",
    "SP-21": "SP-21.csv",
    "FA-22": "FA-22.csv",
    "SP-22": "SP-22.csv",
    "FA-23": "FA-23.csv",
    "SP-23": "SP-23.csv",
    "FA-24": "FA-24.csv",
    "SP-24": "SP-24.csv",
    "SP-25": "SP-25.csv",
}

@st.cache_data
def load_all_terms():
    frames = []
    for term, filename in TERM_FILES.items():
        path = DATA_DIR / filename
        df = pd.read_csv(path, dtype=str)
        df["term"] = term
        frames.append(df)
    all_df = pd.concat(frames, ignore_index=True)
    all_df.columns = [c.strip() for c in all_df.columns]
    return all_df

st.title("EOPS Survey Dashboard (smoke test)")

try:
    df_all = load_all_terms()
    st.success("Data loaded successfully.")
    st.write("Number of rows:", len(df_all))
    st.write("First 5 rows:")
    st.dataframe(df_all.head())
except Exception as e:
    st.error(f"Error loading data: {e}")

