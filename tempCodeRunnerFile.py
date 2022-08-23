while True:
    try:
        Numero1=int(input("Ingrese primer valor:"))
        Numero2=int(input("Ingrese segundo valor:"))
        division=Numero1/Numero2
        print("La división es",division)
    except ValueError:
        print("debe ingresar números.")
    respuesta=input("Desea ingresar otro par de valores?[s/n]")
    if respuesta=="n":
        break
