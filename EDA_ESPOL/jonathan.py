nombre='doberman'
puntos= 3
nombre2 = 'pitbull'
puntos2=3
f = open('result.txt','a')
f.write(f'{nombre} tiene {puntos} \n')
f.write(f'{nombre2} tiene {puntos2} \n')
f.close()

f=open('result.txt','r')
for x in f:
    l_x =x.strip().split('tiene')
    valor=3
    print(f'{l_x[0]} tiene {l_x[1]}')