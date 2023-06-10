matriz = [7, 2, 9, 5, 1, 6]  # Matriz para halla el maximo y minimo
minimo = matriz[0]  # inicio una variable para guardar el valor minimo con el
maximo = matriz[0]  # primer valor de la lista para comparar con el segundo
for i in matriz:  # itero por la matriz
    if i > maximo:  # comparo los numeros para halla el maximo
        maximo = i  # si es minimo se guarda en la variable
    elif i < minimo:  # comparo los numeros para halla el maximo
        minimo = i  # si es minimo se guarda en la variable
diferencia = maximo - minimo  # para halla la diferencia, es restando
print(f"(la maxima diferencia entre {minimo} y {maximo} Es {diferencia} )")
# muestro el resultado final en pantalla
