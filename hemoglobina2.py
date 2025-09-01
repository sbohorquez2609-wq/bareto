N = int(input())

hombres_baja = 0
hombres_normal = 0
hombres_alta = 0
mujeres_baja = 0
mujeres_normal = 0
mujeres_alta = 0

for _ in range(N):
    hemoglobina = float(input())
    genero = int(input())
    
  
    while genero != 1 and genero != 2:
        genero = int(input())
    
    if genero == 1:  
        if hemoglobina < 12.2:
            hombres_baja += 1
        elif hemoglobina <= 16.6:
            hombres_normal += 1
        else:
            hombres_alta += 1
    elif genero == 2:  
        if hemoglobina < 12.6:
            mujeres_baja += 1
        elif hemoglobina <= 15:
            mujeres_normal += 1
        else:
            mujeres_alta += 1

print(hombres_baja, hombres_alta, hombres_normal, mujeres_baja, mujeres_alta, mujeres_normal)
