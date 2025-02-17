def piramide_asteriscos(n):
    if n < 2:
        print("El número debe ser al menos 2.")
        return
    
    for i in range(1, n + 1):
        espacios = n - i  
        asteriscos = 2 * i - 1  #
        print(" " * espacios + "*" * asteriscos)  


n = int(input("Ingrese un número entero (mínimo 2): "))
piramide_asteriscos(n)
