#Creamos primera función en el que leemoos documento
def LeerDocument(archivo):
    """Leerá la información de un fichero y la guardará en una variable del tipo lista
    
    Parámetros:

    Entrada:
        archivor: Ruta de acceso al fichero
        
    Salida:
        -Lista con los datos del fichero
    """
    documento = open(archivo, "r")
    leer = documento.read()
    #print(leer)
    lineas = leer.split("\n")
    print(lineas)

LeerDocument("LibroCuentas.txt")
    


def IdentificarPago(lista):
    """Tendremos la identificación de los pagados
    
    Parámetros:
        -lista: lista de str
        
    Salida:
        -No devuelve nada
    """
    import os
    
    if os.path.isfile("LibroCuentas.txt"):
        with open("LibroCuentas.txt", "r") as file:
            leer_documento = file.readlines()
        with open ("PAGADO.txt", "w") as file:
            for i in leer_documento:
                if lista in i:
                    file.write(i)

IdentificarPago("PAGADO")