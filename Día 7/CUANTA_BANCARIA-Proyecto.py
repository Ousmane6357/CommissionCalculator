class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\n numero de cuenta {self.numero_cuenta}: tiene disponible ${self.balance}"

    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")


    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")

        else:
            print("Fondos insuficientes")


def crear_cliente():
    nombre_clt = input("Ingrese su nombre: ")
    nombre_apl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese tu numero de cuenta: ")
    cliente = Cliente(nombre_clt,nombre_apl,numero_cuenta)
    return cliente


def inicio():
    mi_cliente=crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 'S':
        print("Elige: Depositar  (D), Retirar (R), Salir (S)")
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)

        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)

        print(mi_cliente)

    print("Gracias por operar en banco Python")


inicio()








