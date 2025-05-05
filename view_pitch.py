from pybaseball import playerid_lookup,statcast_pitcher
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 特定の選手のIDを取得するプログラム
# data = playerid_lookup('Yamamoto','Yoshinobu')
# data.to_excel("yamomoto_id.xlsx",index=False)

df_yamamoto = statcast_pitcher('2024-03-28', '2024-09-30', player_id = 808967)
def create_kinddata(df):
    tmplist = []
    for tmp in df:
        if tmp not in tmplist:
            tmplist.append(tmp)
    return tmplist

#球種を調べる
#game_data_list = create_kinddata(df_yamamoto['pitch_type'])

#日付を調べる
#game_data_list = create_kinddata(df_yamamoto['game_date'])

target_pitch_type = 'FF'
target_game_day = '2024-09-28'
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
plt.show()