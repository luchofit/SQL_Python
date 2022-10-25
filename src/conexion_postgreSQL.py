import psycopg2
import psycopg2.extras
#connection = None
#cursor = None

try:
    connection = psycopg2.connect(
        host= 'localhost',
        dbname = "proyectoX",
        user= "postgres" ,
        password = 'PRUEBA123',
        port = 5433
    )
    print("conexion exitosa")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) #retorna el cursor no como tupla sino como diccionario
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as ex:
    print("Ocurrió un error al conectar a PostgreSQL: ", ex)
# finally:
#   if cursor is not None:
#       cursor.close()
#   if connection is not None:  
#       connection.close()
#   print("conexión finalizada")
