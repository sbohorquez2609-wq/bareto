hemoglobina  = float(input("ingrese el valor de la hemoglobina (g/dl):"))
genero = int(input("Ingrese el genero (1: mujer , 2: hombre):"))

if hemoglobina == 1: 
    if hemoglobina < 12.6:
        print("Baja")
        
    elif hemoglobina <= 15:
        print("Normal")
        
    else:
        print("Alta")
        

if hemoglobina == 2: 
    if hemoglobina < 12.2:
        print("Baja")
        
    elif hemoglobina <= 16.6:
        print("Normal")
        
    else:
        print("Alta")
        
else:
    print("No es posible generar la alerta")
        
