#BORRAR DESPUES: odio las matematicas.
import numpy as np
import matplotlib.pyplot as plt
class FuncionTrigonometrica:
    def __init__(self, tipo, amp=1, per=2*np.pi):
        self.tipo = tipo
        self.amp = amp
        self.per = per
    def evaluar(self, x):
        if self.tipo == 'seno':
            return self.amp * np.sin(x * 2 * np.pi / self.per)
        elif self.tipo == 'coseno':
            return self.amp * np.cos(x * 2 * np.pi / self.per)
        elif self.tipo == 'tangente':
            return self.amp * np.tan(x * 2 * np.pi / self.per)
    def graficar(self, intervalo):
        x_vals = np.arange(intervalo[0], intervalo[1], intervalo[2])
        y_vals = [self.evaluar(x) for x in x_vals]
        plt.plot(x_vals, y_vals, label=f'{self.tipo} (A={self.amp}, P={self.per})')
        plt.xlabel('x (radianes)')
        plt.ylabel('f(x)')
        plt.title(f'Gráfica de {self.tipo}')
        plt.legend()
        plt.grid(True)
        plt.show()
    def __repr__(self):
        return f'FuncionTrigonometrica(tipo={self.tipo}, amp={self.amp}, per={self.per})'
    def valor_critico(self):
        if self.tipo in ['seno', 'coseno']:
            return self.amp
        elif self.tipo == 'tangente':
            return np.inf
if __name__ == "__main__":
    seno = FuncionTrigonometrica('seno', amp=2, per=np.pi)
    print(f"Evaluación en x=1: {seno.evaluar(1)}")
    seno.graficar((0, 4, 0.1))
    print(seno)
    print(f"Valor crítico: {seno.valor_critico()}")