import numpy.matlib as np
from scipy.stats import ksone
from scipy.stats import chi2

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

    def testCorridas(self, muestra):

        maxval = 2**64 #Probar con distintos valores (num max en muestra y num max posible por el generador)
        for i in range(len(muestra)):
            muestra[i]=muestra[i]/(maxval)

        muestrabin=[]
        for i in muestra:
            if i >= 0.5:
                muestrabin.append(1)
            else:
                if i < 0.5:
                    muestrabin.append(0)

        corrida = []
        frecAbsCorrida = []
        index = 0
        frecNroAct = 1
        while index < len(muestrabin):
            nroAct = muestrabin[index]
            if index != len(muestrabin)-1:
#                frecNroAct = 1
                if nroAct == muestrabin[index+1]:
                    frecNroAct = frecNroAct + 1
                if nroAct != muestrabin[index+1]:
                    if corrida.count(frecNroAct) != 0:
                        i = corrida.index(frecNroAct)
                        frecAbsCorrida[i] = frecAbsCorrida[i] + 1
                        frecNroAct = 1
                    if corrida.count(frecNroAct) == 0:
                        corrida.append(frecNroAct)
                        frecAbsCorrida.append(1)
                        frecNroAct = 1

            else:
                if nroAct == muestrabin[index-1]:
                    frecNroAct = frecNroAct + 1
                    if corrida.count(frecNroAct) != 0:
                        i = corrida.index(frecNroAct)
                        frecAbsCorrida[i] = frecAbsCorrida[i] + 1
                        frecNroAct = 1
                    if corrida.count(frecNroAct) == 0:
                        corrida.append(frecNroAct)
                        frecAbsCorrida.append(1)
                        frecNroAct = 1
                if nroAct != muestrabin[index-1]:
                    if corrida.count(frecNroAct) != 0:
                        i = corrida.index(frecNroAct)
                        frecAbsCorrida[i] = frecAbsCorrida[i] + 1
                        frecNroAct = 1
                    if corrida.count(frecNroAct) == 0:
                        corrida.append(frecNroAct)
                        frecAbsCorrida.append(1)
                        frecNroAct = 1
            index = index + 1

        frecEsperada = []
        for i in range(len(corrida)):
            frecEsperada.append((len(muestra) - corrida[i] + 3)/ 2**(1+corrida[i]))

        resultado = 0
        for i in range(len(corrida)):
            resultado = resultado + (((frecEsperada[i]-frecAbsCorrida[i])**2) / frecEsperada[i])

        if resultado < chi2.isf(0.01, max(corrida)):
            return "Aprobado"
        else: 
            return "Fallo"

    def series(self, muestra):
    	N = len(muestra)
    	n = 5
    	lista_parejas = []
    	for i in range(0, N-1):
    		pareja = [muestra[i], muestra[i+1]]
    		lista_parejas.append(pareja)

    	tabla = []
    	for i in range(0, n):
    		lista = []
    		for j in range(0, n):
    			lista.append(0)
    		tabla.append(lista)

    	for i in lista_parejas:
    		for j in range(n, 0, -1):
    			for k in range (n, 0, -1):
    				if(j-1 == 0 and k-1 != 0):
    					if (1/j > i[0] and 1/k > i[1] and 1/(k-1) < i[1]):
    						tabla[5-j][5-k] += 1
    						break
    				elif (k-1 == 0 and j-1 != 0):
    					if (1/j > i[0] and 1/k > i[1] and 1/(j-1) < i[0]):
    						tabla[5-j][5-k] += 1
    						break
    				elif (k-1 == 0 and j-1 == 0):
    					if (1/j > i[0] and 1/k > i[1]):
    						tabla[5-j][5-k] += 1
    						break
    				else:
    					if (1/j > i[0] and 1/k > i[1] and 1/(j-1) < i[0] and 1/(k-1) < i[1]):
    						tabla[5-j][5-k] += 1
    						break

    	x_0 = 0
    	for i in range(0, n):
    		for j in range(0, n):
    			x_0 = (tabla[i][j] - (N-1)/n**2)**2

    	x_0 = n**2/(N-1) * x_0

    	x_0_calculada = 36.4

    	if x_0 < x_0_calculada:
    		return "Aprobado"
    	else:
    		return "Fallo"