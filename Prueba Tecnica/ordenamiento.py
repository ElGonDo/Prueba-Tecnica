# metodo burbuja
def MiOrdenamiento(array):
    for i in range(len(array)):  # En este bucle hago el numero de pasadas por la lista
        for j in range(len(array) - 1):  # Bucle comparo los numeros de la lista menos 1
            if array[j] > array[j + 1]:  # utilizo un condicional para comparar
                cambio = array[j]  # aqui uso una variable de axulio para intercambiar
                array[j] = array[j + 1]  # para colocar el numero en la nueva posicion
                array[j + 1] = cambio  # siempre en cuando el primero sea mayor que el 2
    return array  # aqui devuelvo la lista ordenada


lista = [4, 2, 9, 1, 7]
print("Sin Ordenamiento: ", lista)
print("Con Ordenamiento: ", MiOrdenamiento(lista))
# llamo la funcion y la muestro en pantalla
