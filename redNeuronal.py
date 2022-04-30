#Importante esta librería 
import numpy as np

#Creamos una neurona.
class Neurona:
    #Inicializamos el peso y el sesgo de mi neurona 
    def __init__(self,peso,sesgo):
        self.peso =peso
        self.sesgo =sesgo
    
    #Funcion sigmoide
    def sigmoide(self,x):
        return 1/(1+np.exp(-x))
    
    def proceso(self,input):
        total = np.dot(self.peso,input) + self.sesgo
        return self.sigmoide(total)

# ne1 = Neurona(np.array([0,1]),4)

# salida = ne1.proceso(np.array([2,3]))
# print(salida)

#Creamos una red neuronal
#Estará conformada por 3 neuronas , 2 input
class RedNeuronal:
    peso = np.array([0,1])
    sesgo = 0

    #Utilizamos la clase neurona
    ne1 = Neurona(peso,sesgo)
    ne2 = Neurona(peso,sesgo)
    ne3 = Neurona(peso,sesgo)

    def PorcesoNeuronal(self,inputn):
        out1 = self.ne1.proceso(inputn)
        out2 = self.ne1.proceso(inputn)

        out3 = self.ne3.proceso(np.array([out1, out2]))
        return out3

#Con nuestra clase(R.N) creamos una
re1 = RedNeuronal()
#Calculamos
calculo = re1.PorcesoNeuronal(np.array([2,3]))
#Imprimios resultado
print(calculo)


    
    
    