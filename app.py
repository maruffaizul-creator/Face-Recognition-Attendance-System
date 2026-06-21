import streamlit as st
import pandas as pd
import time
from datetime import datetime

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")

import os

file_path = 'attendence/attendence_' + date + '.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.write("No attendance record found for today.")