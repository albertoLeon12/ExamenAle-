import random

def menu():
    salida="{:>32}". format("FINANCIERA LINCE")+"\n"
    salida+="{:>34}". format("TARJETA DE CRÉDITO: MENÚ")+"\n"
    salida+="{:<27}". format("1 CONSULTAR SALDO")+"\n"
    salida+="{:>41}". format("2 CONSULTA PAGO PARA NO GENERAR INTERESES")+"\n"
    salida+="{:>28}". format("3 RETIRO CON CARGO A TARJETA")+"\n"
    salida+="{:>16}". format("4 PAGO A TARJETA")+"\n"
    salida+= "{:>7}". format("5 Salir")
    return salida

cliente = input("Hay un cliente S/N: ")

while(cliente=="S"or cliente=="s"):
    nombre=input("NOMBRE DEL CLIENTE: ")
    saldo = random.randint(15000,60000)
    res= int(input(menu()))

    while(not res==5):
        if(res==1):
            salida="Tu saldo actual es $ "+"{:<1.2f}".format(saldo)
            print(salida)

        elif(res==2):
            salida="CANTIDAD QUE ADEUDA AL BANCO ES $"+"{:<1.2f}".format(saldo)
            salida+="\nPago para no generar intereses en $´"+"{:<1.2f}".format(saldo*.70)
            print(salida)

        elif(res==3):
            print("Saldo antes del retiro: $"+"{:<1.2f}".format(saldo))
            retiro=int(input("Cantidad a retirar debe ser menor o igual a "+str(saldo)+":"))
            print("Saldo después del retiro: $"+"{:<1.2f}".format(saldo-retiro))

        elif(res==4):    
            print("Saldo actual: $"+str(saldo))
            pagar=int(input("Cantidad a pagar: "))
            print("Saldo después del pago:"+"{:<1.2f}".format(saldo-pagar))

        elif(res==5):
            salida="NOMBRE:"+nombre
            salida+= "{:<13}".format(" ")+"SALDO ACTUAL $ "+str(saldo)

        res= int(input(menu()))    

    cliente=input("Hay otro cliente S/N: ")        

print("Fin del programa de atención al cliente")
