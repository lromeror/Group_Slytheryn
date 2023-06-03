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
df_img_codes = pd.read_csv('/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/DASHBOARD/assets/datas/paises_excel_27_5.csv',sep=';')
#df_img_codes = pd.read_excel('/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/DASHBOARD/assets/datas/Los_ultimos.xlsx',sheet_name='Hoja1')
for pais in  []:
    df_f = df_img_codes[df_img_codes['PAIS'] == pais].reset_index(drop=True)
    for actual,nuevo in zip(df_f['ACTUAL'],df_f.NUEVO):
        try :
            file_oldname = os.path.join(f"/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/DASHBOARD/assets/datas/Los_ultimos.xlsx",actual )
            file_newname_newfile = os.path.join(f"/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/DASHBOARD/assets/Images/{pais}",nuevo)
            os.rename(file_oldname, file_newname_newfile)
        except (FileNotFoundError):
            continue


        