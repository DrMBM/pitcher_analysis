#スピードと回転数から投手の球種を分けるかk-meansで分けてみる
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib
from sklearn.cluster import KMeans


df = pd.read_csv('/Users/masaki/Desktop/野球/pitcher_analysis/data/yamamoto.csv')
df_events = df['events']
df_gamedatas = df['game_date']
df_innings = df['inning']
df_events = df_events.dropna(how='any')
cal_innings_dic = {'field_out' :1, 'strikeout':1,'sac_fly':1,'sac_bunt':1,
                   'grounded_into_double_play':2,'force_out' :1,'fielders_choice':1}
#打者との結果とその回数を辞書でまとめている
dic_event = {}
dic_gamedata = {}
pitching_innings = 0
i = 0
tmp = 5
for event  in df_events:
    if event not in dic_event.keys():
        dic_event[event] = 0
    if event in cal_innings_dic:
        pitching_innings += cal_innings_dic[event]
    dic_event[event] += 1

pitching_innings /= 3
#K/BB
k_BB = dic_event['strikeout']/dic_event['walk']

#BB/9
BB_9 = (dic_event['walk']*9) / pitching_innings

#K/9
K_9 = (dic_event['strikeout']*9) / pitching_innings

def walk_puls_hits(df):
    count = df['walk'] + df['single'] + df['double'] + df['triple'] + df['home_run']
    return count

#WHIP
whip = walk_puls_hits(dic_event)/pitching_innings


print(f"K/BB:{k_BB}")
print(f"BB/9:{BB_9}")
print(f"K/9: {K_9}")
print(f"whip:{whip}")

