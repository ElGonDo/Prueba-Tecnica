cadena = "Hola Mundo!"  # cadena que se mostrara de forma inversa
for i in range(len(cadena) - 1, -1, -1):  # el bucle que inicia desde "!" hasta el "H"
    print(cadena[i], end="")  # de manera decremental, y aqui lo imprime
print()  # print para separa las 2 formas de hacerlo
print(cadena[::-1])  # el metodo slicing que lo hace de manera decremental -1
