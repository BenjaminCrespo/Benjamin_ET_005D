productos = {'C-123': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'C-111': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'C-234': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'C-456': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'C-1222': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'C-477': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'C-334': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'C-2906': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'C-123': [387990,10], 
'C-111': [327990,4], 
'C-234': [424990,1],
'C-456': [664990,21], 
'C-477': [290890,32], 
'C-334': [444990,7],
'C-1222': [749990,2], 
'C-2906': [349990,1]}

def stock_marca(marca):
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            precio, cantidad = stock.get(modelo, [0, 0])
            print(f"modelo: {modelo}, stock: {cantidad}")
            
def buscar_precio(p_min, p_max):
    try:
        resultados = []
        for modelo, datos in stock.items():
            precio = datos[0]
            if p_min <= precio <= p_max:
                marca = productos[modelo][0]
                resultados.append(f"{marca} - {modelo}")
                if resultados:
                    print("Modelos encontrados: ", resultados)
            else:
                print("No hay computadores en ese rango de precio")
    except:
                print("Error, valor incorrecto")
                
def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False

def menu():
    while (True):
        print("\n** Menu Principal **")
        print("1. Stock de marcas")
        print("2. Busqueda de precios")
        print("3. Actualizar precios")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            marca = input("Ingrese una marca: ")
            stock_marca(marca)
            
        elif opcion == "2":
            try:
                p_min = int(input("Ingrese el precio minimo: "))
                p_max = int(input("Ingrese el precio maximo: "))
                buscar_precio(p_min, p_max)
            except ValueError:
                print("Debe ingresar una opcion valida")
                
        elif opcion == "3":
            modelo = input("Ingrese modelo del computador para actualizar: ")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio :"))
                if actualizar_precio(modelo, nuevo_precio):
                    print("¡Precio actualizado!")
                else:
                    print("El modelo no existe")
            except ValueError:
                print("Debe ingresar un numero valido")
        elif opcion == "4":
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar una opcion valida")
            
menu()
