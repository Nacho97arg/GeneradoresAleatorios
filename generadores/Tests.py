import numpy.matlib as np
from scipy.stats import ksone

class tests:

    def chiSqTest(self, muestra):
        maxval = 2**64 #Probar con distintos valores (num max en muestra y num max posible por el generador)
        for i in range(len(muestra)):
            muestra[i]=muestra[i]/(maxval)
        frecAbs=[]
        for i in range(10):
            frecAbs.append(self.contar(i/10,(i+1)/10,muestra)) #10 intervalos de 0.1
        result=0
        for i in frecAbs:
            result=result+((i-10)**2/10)
        if result < 16.918: #Para 95% de nivel de confianza y 9 grados de libertad
            return "Aprobado"
        else:
            return "Fallo"

    def contar(self, valMin,valMax, val):
        cont=0
        for i in val:
            if i > valMin and i <= valMax:
                cont+=1
        return cont

    def testKS(self, muestra, n):
        valor_critico = self.ks_critical_value(n, 0.05)
        print(valor_critico)
        muestra.sort()
        d_max = 0
        d_min = 0
        for i in range(0, n):
            a = i/n - muestra[i]
            if (a > d_max):
                d_max = a
            b = muestra[i] - (i-1)/n
            if (b < d_min):
                d_min = b

        if (d_min > d_max):
            D = d_min
        else:
            D = d_max

        if(D < valor_critico):
            return True
        else:
            return False

    def ks_critical_value(self, n_trials, alpha):
        return ksone.ppf(1-alpha/2, n_trials)