#%%
import pandas as pd

#%%
nvo_bel = float(input('Въведете точките от НВО по БЕЛ: '))
nvo_mat = float(input('Въведете точките от НВО по МАТ: '))
klas_bel = float(input('Въведете оценката по БЕЛ от 7 клас: '))
klas_mat = float(input('Въведете оценката по МАТ от 7 клас:'))

#%%
df = pd.read_csv('raw_data/plan-priem-2024-2025.csv', sep=',')

#%%
plovdiv_filter = df['Нас. място'] == 'ГР.ПЛОВДИВ'
plovdiv_df = df[plovdiv_filter]


#%%
score_6 = 50
score_5 = 39
score_4 = 26
score_3 = 15