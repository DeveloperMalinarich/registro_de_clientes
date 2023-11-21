import sqlite3
conn = sqlite3.connect('registro_de_clientes.db')
c = conn.cursor()

#defino la funcion principal

def menu_principal():
    import sqlite3
    conn = sqlite3.connect('registro_de_clientes.db')
    c = conn.cursor()
    print("** BIENVENIDO AL REGISTRO DE CLIENTES **")
    print("  NOTA: En nuestra app podés consultar tus datos o" 
          " darte de alta.\n")
    
    #solicito datos al usuario
     
    nombre = input("Por favor ingresa tu nombre: ")
    apellido = input("Y ahora tu apellido: ")
    

    #realizo consulta en la base
    def comparo_base(nombre, apellido):
        c.execute("SELECT * FROM clientes WHERE nombre =? AND apellido = ?", (nombre, apellido))
        
        #almaceno los resultados en la variable resultados
        resultados = c.fetchall()
        
        #llamar a los menus corresopndientes
        if resultados:
            cliente_existe(nombre, apellido)
        
        if not resultados:
            cliente_noexiste()
    comparo_base(nombre, apellido)        

#creo la funcion a llamar cuando el cliente existe
def cliente_existe(nombre, apellido):
    conn = sqlite3.connect('registro_de_clientes.db')
    c = conn.cursor()

    while True:

        opcion = int(input("El cliente ya existe, seleccioná una opcion por favor:"
                       "\n1. Ver mis datos."
                       "\n2. salir del programa."
                       "\n>>>>"))

        if opcion == 1:
            #ejecutar consulta que muestre los datos del cliente
            c.execute("SELECT * FROM clientes WHERE nombre = ? AND apellido = ?", (nombre, apellido))
            resultado = c.fetchall()
            print(resultado)
            print()
            input("** MUCHAS GRACIAS POR CONSULTAR NUESTRA BASE! **"
                  "\n Te esperamos nuevamente pronto"
                  "\n Por favor, presioná Enter para finalizar. "
                  "\n >>>>   ENTER    <<<<< ")
            break
        
        elif opcion == 2:
            #imprimir mensaje de despedida y romper bucle
            print("** MUCHAS GRACIAS POR CONSULTAR NUESTRA BASE!"
                  "\nTe esperamos nuevamente pronto")
            break

        else:
            # imprime mensaje de seleccion erronea
            print("La opcion seleccionada no existe, por favor intentá otra vez.")

            # solicitar elección nuevamente
            opcion = int(input("Seleccioná una opcion por favor:"
                            "\n1. Ver mis datos."
                            "\n2. salir del programa"
                            "\n>>>"))
            continue

#defino funcion cliente no existe
def cliente_noexiste():
    import sqlite3
    conn = sqlite3.connect('registro_de_clientes.db')
    c = conn.cursor()

    #solicito eleccion al usuario
    opcion = int(input("El cliente no existe, por favor ingresá la opcion deseada:"
                       "\n.1 Agregar mis datos"
                       "\n.2 Salir del programa"
                       "\n>>>"))
    #defino bucle while

    while True:
        #opcion 1 agregar mis datos
        if opcion == 1:

            #solicito datos al usuario
            nombre = input("Ingresá tu nombre por favor y presioná Enter."
                            "\n>>>")
            apellido = input("Ahora, ingresá tu apellido por favor."
                                "\n>>>")
            DNI = int(input("Ingresá tu numero de DNI sin los puntos y presioná Enter."
                            "\n>>>"))
            telefono = int(input("Ingresá tu numero de telefono sin espacios ni guiones y presioná Enter."
                            "\n>>>"))
            mail = (input("Ingresá tu dirección de correo electrónico presioná Enter."
                            "\n>>>"))

            #defino variable que almacena los datos 
            datos_cliente = (None, nombre, apellido, DNI, telefono, mail)

            #realizo la consulta para insertar los datos en la base
            try:
                c.execute("INSERT INTO clientes VALUES (?,?,?,?,?,?)", datos_cliente)
                conn.commit()

                #imprimo mensaje de confirmacion
                input("Se agregaron los datos correctamente a la base, bienvenido!"
                    "\nPresiona Enter para finalizar.")
                break
            
            #si hay alguna excepcion imprimo el mensaje de error
            except Exception as e:
                print("Algo no salió bien, revisa el codigo!")

        #si elije la opcion 2
        elif opcion == 2:

        #imprimir mensaje de despedida y romper bucle
            print("** MUCHAS GRACIAS POR CONSULTAR NUESTRA BASE!"
                    "\nTe esperamos nuevamente pronto")
            break

        else:
            # imprime mensaje de seleccion erronea
            print("La opcion seleccionada no existe, por favor intentá otra vez.")

            # solicitar elección nuevamente
            opcion = int(input("Seleccioná una opcion por favor:"
                            "\n1. Ver mis datos."
                            "\n2. salir del programa"
                            "\n>>>"))
            continue


menu_principal()