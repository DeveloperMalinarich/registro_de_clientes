#defino la funcion que creara la base y se conectara a ella
def base_datos():
    #importo libreria SQLite
    import sqlite3

    #creo una db y una conexion a ella
    conn = sqlite3.connect('registro_de_clientes.db')
    
    #creo el cursor almacenado en la variable
    c = conn.cursor()

    #llamo a la funcion que crea la tabla
    tabla_clientes(c, conn)

    #cierro la conexion
    conn.commit()
    conn.close()
    
#creo las tablas
def tabla_clientes(c, conn):
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS clientes(
                    ID_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    DNI INTEGER UNIQUE NOT NULL, 
                    telefono INTEGER NOT NULL,
                    email TEXT NOT NULL
            )
        """)
    #este es el mensaje de error si algo ocurre cuando creo la tabla
    except Exception as e:
        print("Algo no salió bien creando esta tabla, revisá el codigo")
    
    #se imprime este mensaje de confirmacion si todo esta bien
    print("La tabla se creo correctamente !!!")

#llamo a la funcion principal
base_datos()