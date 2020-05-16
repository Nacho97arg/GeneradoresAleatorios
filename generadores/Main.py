import generadores as gn
import Tests as ts
import numpy.matlib as np

gen = gn.ranGen()
testers = ts.tests()
nrosRandom = gen.randGCL(15,100)#gen.randLFG(6,8,100)#
#testers.testCorridas(nrosRandom)
print(testers.testCorridas(nrosRandom))

#for i in nrosRandom:
#   print(i)





