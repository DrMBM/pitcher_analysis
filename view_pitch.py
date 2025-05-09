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


target_pitch_type = st.selectbox("球種を選択してください", pitch_type_list)

coord_dict = {}
coord_list = []
for pitch_type ,x,z in zip(df_yamamoto['pitch_type'],df_yamamoto['plate_x'],df_yamamoto['plate_z']):
    if pitch_type not in coord_dict:
        coord_dict[pitch_type] = []
    if pitch_type == target_pitch_type:
        coord_list.append(1)
    else:
        coord_list.append(0.3)
    coord_dict[pitch_type].append((x,z))

zone_left, zone_right = -0.83, 0.83
zone_bottom, zone_top = 1.5, 3.5
fig = plt.figure(figsize=(6, 6))  
#coord_arr = np.array(coord_list)
#plt.scatter(coord_arr[:,0],coord_arr[:,1])
i = 0
for pitch_type, coords in coord_dict.items():
    coords = list(zip(*coords))  # x, z に分割
    plt.scatter(coords[0], coords[1], c=plt.cm.tab20(i),alpha=coord_list[i])
    i += 1
    
plt.vlines([zone_left, zone_right], zone_bottom, zone_top, color='r')
plt.hlines([zone_bottom, zone_top], zone_left, zone_right, color='r')

# 軸の範囲を固定
plt.xlim(-2, 2)
plt.ylim(0, 5)
plt.axis('off')

st.pyplot(fig)