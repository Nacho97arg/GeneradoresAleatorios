import generadores as gn
import Tests as ts
import numpy.matlib as np
import random

gen = gn.ranGen()
testers = ts.tests()
nrosRandomLFG = gen.randLFG(6,7,100)
nrosRandomGLC = gen.randGCL(15,100)
nrosRandomPy = []
for i in range(100):
    nrosRandomPy.append(random.random())
#testers.testCorridas(nrosRandom)
print('------------------------------------------------------------------------------')
print('| Generadores \ Test | Chi Cuadrado | Kolmogorov-Smirnov | Corridas | Series |')
print('|--------------------|--------------|--------------------|----------|--------|')
print('|         GLC        |   '+testers.chiSqTest(nrosRandomGLC)+'   |      '+testers.testKS(nrosRandomGLC)+'      | '+testers.testCorridas(nrosRandomGLC)+' |   '+testers.series(nrosRandomGLC)+'|')
print('|--------------------|--------------|--------------------|----------|--------|')
print('|         LFG        |    '+testers.chiSqTest(nrosRandomLFG)+'     |       '+testers.testKS(nrosRandomLFG)+'        |   '+testers.testCorridas(nrosRandomLFG)+'  |   '+testers.series(nrosRandomLFG)+'|')
print('|--------------------|--------------|--------------------|----------|--------|')
print('|      randrange     |   '+testers.chiSqTest(nrosRandomPy)+'   |      '+testers.testKS(nrosRandomPy)+'      | '+testers.testCorridas(nrosRandomPy)+' |   '+testers.series(nrosRandomPy)+'|')
print('------------------------------------------------------------------------------')

#for i in nrosRandom:
#   print(i)





