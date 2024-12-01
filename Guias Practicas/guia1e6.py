import numpy as np
import matplotlib.pyplot as plt
class Cuerpo:
    def __init__(self, velocidad, posicion_inicial=0):
        self.velocidad = velocidad
        self.posicion_inicial = posicion_inicial
    def calcular_posicion(self, tiempo):
        return self.posicion_inicial + self.velocidad * tiempo
class SimuladorMovimiento:
    def __init__(self, cuerpo):
        self.cuerpo = cuerpo
    def simular(self, tiempo_maximo, intervalo=0.1):
        tiempos = np.arange(0, tiempo_maximo, intervalo)
        posiciones = [self.cuerpo.calcular_posicion(t) for t in tiempos]
        plt.figure(figsize=(10, 6))
        plt.plot(tiempos, posiciones, label=f'Velocidad = {self.cuerpo.velocidad} m/s')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Posición (m)')
        plt.title('Movimiento Rectilíneo Uniforme')
        plt.legend()
        plt.grid(True)
        plt.show()
if __name__ == "__main__":
    cuerpo = Cuerpo(velocidad=5, posicion_inicial=0)
    simulador = SimuladorMovimiento(cuerpo)
    simulador.simular(tiempo_maximo=10, intervalo=0.1)