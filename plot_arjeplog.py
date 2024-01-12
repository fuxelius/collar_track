#
#     plot_arjeplog_gps.py
#
#          Project:  PM1
#          Author:   Hans-Henrik Fuxelius   
#          Date:     2023-07-02       
#          Descr:    Projection of GPS positions in reindeer
#          Ref:      SLU
#

# USAGE
# conda activate torch
# streamlit run plot_arjeplog_gps.py

import numpy as np
import pandas as pd
import sqlite3
import streamlit as st

# ------------------ ------------------ ------------------
# access DB tables
# con = sqlite3.connect("negev21_0003_20221121_1905.sqlite3")

# df_pos  =  pd.read_sql_query("""SELECT lat, lon, alt, dop, speed
#                                 FROM gps
#                                 WHERE track_id < 3""", con)

# con.close()

# df_pos.to_csv('negev21_0003_20221121_1905.csv', index=False)

# ------------------ ------------------ ------------------
# access CSV file
df_pos = pd.read_csv('negev21_0003_20221121_1905.csv')

df_pos['dop'] = 1 / df_pos['dop'] * 30
  
df_pos['color'] = '#A45C40'                                                      # BROWN       Faster then   36 km/h, this is transort by truck!
df_pos['color'][(df_pos['speed'] > 5)   & (df_pos['speed'] <= 10)]   = '#FF5F15' # RED         Between 18  - 36 km/h
df_pos['color'][(df_pos['speed'] > 3)   & (df_pos['speed'] <= 5)]    = '#FFAEBC' # PINK        Between 11  - 18 km/h
df_pos['color'][(df_pos['speed'] > 1)   & (df_pos['speed'] <= 3)]    = '#59981A' # GREEN       Between 4   - 11 km/h
df_pos['color'][(df_pos['speed'] > 0.15) & (df_pos['speed'] <= 1)]   = '#7EC8E3' # LIGHT BLUE  Between 0.5 - 4 km/h
df_pos['color'][(df_pos['speed'] > 0)   & (df_pos['speed'] <= 0.15)] = '#0000FF' # DARK BLUE   Slower then   0.5 km/h

# RENDER

st.title("Streamlit Dashboard of Reindeer position by GPS")

st.markdown("""|Color|Speed|
|------|--------------------------------------|
|BROWN|Faster then   36 km/h, this is transport by truck!|
|RED|Between 18  - 36 km/h|
|PINK|Between 11  - 18 km/h|
|GREEN|Between 4   - 11 km/h|
|LIGHT BLUE|Between 0.5 - 4 km/h|
|DARK BLUE|Slower then   0.5 km/h|""")

st.map(df_pos,
    latitude='lat',
    longitude='lon',
    size='dop',
    color='color',
    zoom=5)










