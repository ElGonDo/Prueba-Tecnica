lista = [3, 6, 9, 12, 4, 1]
suma = 10

for i in range(len(lista)):  # Bucle para interar por los elemento de la lista
    for j in range(len(lista)):  # bucle para comparar el 1 numero con el segundo
        if lista[i] + lista[j] == suma:  # condicion para comprobar si la suma de los 2
            array = []  # variable para guardar los numero utilizados
            array.append(lista[i])  # los agrega a la lista vacia
            array.append(lista[j])
            print(f"{array} ({lista[i]} + {lista[j]} = {suma})")
            # muestro en pantalla la lista, y los 2 numeros utilizados para dicha suma
