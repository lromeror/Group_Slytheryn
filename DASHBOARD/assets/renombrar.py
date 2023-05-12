import os
import pandas as pd
# ECUADOR Y ARGENTINA YA ESTA
paises=['Ecuador','Argentina','Australia', 'Wales', 'Morocco', 'Qatar', 'Senegal', 'Ghana',
    'Saudi Arabia', 'IR Iran', 'France', 'Uruguay', 'Tunisia',
    'Spain', 'Serbia', 'Brazil', 'Denmark',
    'Mexico', 'Canada', 'Belgium', 'Cameroon', 'Croatia',
    'Netherlands', 'Portugal', 'Costa Rica', 'United States',
    'Germany', 'Japan', 'Switzerland', 'Poland', 'England',
    'Korea Republic']
#['Ecuador','Argentina','Wales','Uruguay'] paises ya hechos
#['Spain','Portugal'] 
#['Mexico','Korea Republic','Qatar','Brazil','Japan']
df_img_codes = pd.read_csv('/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/Data_worldCup/Images_country.csv',sep=';')
for pais in  paises:
    df_f = df_img_codes[df_img_codes['PAIS']==pais]
    for actual,nuevo in zip(df_f.ACTUAL,df_f.NUEVO):
        try :
            file_oldname = os.path.join(f"/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/DASHBOARD/assets/Images/{pais}",actual )
            file_newname_newfile = os.path.join(f"/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/DASHBOARD/assets/Images/{pais}",nuevo)
            os.rename(file_oldname, file_newname_newfile)
        except (FileNotFoundError):
            continue


        