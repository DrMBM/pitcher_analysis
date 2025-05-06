import streamlit as st
from pybaseball import playerid_lookup,statcast_pitcher
import numpy as np
import matplotlib.pyplot as plt

df_yamamoto = statcast_pitcher('2024-03-28', '2024-09-30', player_id = 808967)
def create_kinddata(df):
    tmplist = []
    for tmp in df:
        if tmp not in tmplist:
            tmplist.append(tmp)
    return tmplist

#球種を調べる
pitch_type_list = create_kinddata(df_yamamoto['pitch_type'])

# #日付を調べる
game_data_list = create_kinddata(df_yamamoto['game_date'])

target_pitch_type = st.selectbox("球種を選択してください", pitch_type_list)
target_game_day = st.selectbox("球種を選択してください", game_data_list)

coord_list = []
for day,pitch_type ,x,z in zip(df_yamamoto['game_date'],df_yamamoto['pitch_type'],df_yamamoto['plate_x'],df_yamamoto['plate_z']):
    if pitch_type == target_pitch_type and day == target_game_day:
        coord_list.append([x,z])

zone_left, zone_right = -0.83, 0.83
zone_bottom, zone_top = 1.5, 3.5

coord_arr = np.array(coord_list)
plt.scatter(coord_arr[:,0],coord_arr[:,1])
plt.vlines([zone_left, zone_right], zone_bottom, zone_top, color='r')
plt.hlines([zone_bottom, zone_top], zone_left, zone_right, color='r')
plt.axis('off')

st.pyplot(plt)