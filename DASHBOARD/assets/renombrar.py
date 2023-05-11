import os
import pandas as pd
# ECUADOR Y ARGENTINA YA ESTA
paises=['Australia', 'Wales', 'Morocco', 'Qatar', 'Senegal', 'Ghana',
    'Saudi Arabia', 'IR Iran', 'France', 'Uruguay', 'Tunisia',
    'Spain', 'Serbia', 'Brazil', 'Denmark',
    'Mexico', 'Canada', 'Belgium', 'Cameroon', 'Croatia',
    'Netherlands', 'Portugal', 'Costa Rica', 'United States',
    'Germany', 'Japan', 'Switzerland', 'Poland', 'England',
    'Korea Republic']
df_img_codes = pd.read_csv('')
for pais in paises:
    df_f = df_img_codes[df_img_codes.PAIS==pais]
    for actual,nuevo in zip(df_f.ACTUAL,df_f.ACTUAL):
        file_oldname = os.path.join(f"/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/DASHBOARD/assets/Images/{pais}",actual )
        file_newname_newfile = os.path.join(f"/Users/angelozurita/Repositorios_GitHub/Group_Slytheryn/DASHBOARD/assets/Images/{pais}",nuevo)
        os.rename(file_oldname, file_newname_newfile)

        