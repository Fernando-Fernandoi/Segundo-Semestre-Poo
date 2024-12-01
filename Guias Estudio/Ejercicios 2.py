class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito realizado. Saldo actual: {self.__saldo}."

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro realizado. Saldo actual: {self.__saldo}."
        return "Saldo insuficiente o cantidad inválida."

    def consultar_saldo(self):
        return f"Titular: {self.__titular}, Saldo: {self.__saldo}."

# Ejemplo de uso
cuenta = CuentaBancaria("Juan", 500)
print(cuenta.depositar(100))
print(cuenta.retirar(200))
print(cuenta.consultar_saldo())
