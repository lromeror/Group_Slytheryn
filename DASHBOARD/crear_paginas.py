import pandas as pd
teams=pd.read_csv('DASHBOARD/selecciones.csv',sep=';')
for team in teams['seleccion']:
    f=open(f'DASHBOARD/pages/{team}.py','w')
    f.write(f"pais='{team}'")
    f.close()