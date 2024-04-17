import os

#DEFINICIONES
productos =[('Leche', 50), ('Galletas', 35), ('Gaseosa', 87), ('Huevos', 66), ('Aceite',110), ('Pan', 20)] #(producto, precio)
carrito=[]

menu= '''
1. Agregar producto
2. Eliminar producto
3. Ver lista de compras
4. Finalizar compra
5. Salir
'''


#MOSTRAR MENU
def mostrar_menu():
    
    print('\nMENU PRINCIPAL')
    print(menu)
    seleccion=int(input('Seleccione una opción: '))
    
    if seleccion==1:
        agregar_producto()
    elif seleccion==2:
        eliminar_producto()
    elif seleccion==3:
        ver_lista()
    else:
        finalizar_compra()
   
#AGREGAR PRODUCTO     
def agregar_producto():
    os.system('cls')
    print('AGREGAR PRODUCTOS\n')
    print('Lista de productos disponibles:')
    for i, producto in enumerate(productos):
        print (f'{i+1} - {producto[0]} ${producto[1]}')   
        
    seleccion=int(input('\nIndique el número del producto que desea agregar: '))
    while seleccion<1 or seleccion>6:
        seleccion=int(input('Ingrese un número de producto válido: '))
        
    carrito.append(productos[seleccion-1]) #Le resto uno ya que lo imprimo desde 1 pero en realidad empiezan desde 0
    os.system('cls')
    print('\n-------------------------------------')
    print('           PRODUCTO AGREGADO!')
    print('-------------------------------------\n')
    mostrar_menu()

#ELIMINAR PRODUCTO
def eliminar_producto():
    if carrito==[]:
        print('TU CARRITO ESTÁ VACÍO, NO HAY PRODUCTOS DISPONIBLES PARA ELIMINAR')
        mostrar_menu()
    else: 
        os.system('cls')
        print('ELIMINAR PRODUCTOS\n')
        print('Lista de productos en su carrito de compras:')
        for i, producto in enumerate(carrito):
            print (f'{i+1} - {producto[0]} ${producto[1]}')  
        
        seleccion=int(input('\nIndique el número del producto que desea eliminar de su carrito: '))
        while seleccion<1 or seleccion>len(carrito):
            seleccion=int(input('Ingrese un número de producto válido: '))
            
        carrito.pop(seleccion-1)
        os.system('cls')
        print('\n-------------------------------------')
        print('          PRODUCTO ELIMINADO!')
        print('\n-------------------------------------\n')
        mostrar_menu()
        
#VER LISTA DE COMPRAS
def ver_lista():
    total=0
    if carrito==[]:
        print('\nTU CARRITO ESTÁ VACÍO, NO HAY PRODUCTOS PARA MOSTRAR')
        mostrar_menu()
    else:
        os.system('cls')
        print('\n-------------------------------------')
        print('\nCARRITO DE COMPRAS:')
        for i, producto in enumerate(carrito):
            print (f'  {i+1} - {producto[0]} ${producto[1]}')
            total+=producto[1]
        print('\n-------------------------------------')
        mostrar_menu()
        
#FINALIZAR COMPRA
def finalizar_compra():
    total=0
    if carrito==[]:
        print('\nTU CARRITO ESTÁ VACÍO, PARA COMPRAR PRIMERO AGREGA UN PRODUCTO')
        mostrar_menu()
    else:
        os.system('cls')
        print('¡GRACIAS POR ELEGIRNOS!')
        print('A continuacion, te dejamos tu ticket de compra:')
        print('\nTICKET:')
        print('\n-------------------------------------')
        print('\nCARRITO DE COMPRAS:')
        for i, producto in enumerate(carrito):
            print (f'  {i+1} - {producto[0]} ${producto[1]}')
            total+=producto[1]
        print(f'TOTAL: {total}')
        print('\n-------------------------------------')
        
#MAIN
os.system('cls')
mostrar_menu()