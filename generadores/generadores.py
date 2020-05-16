import numpy as np

class ranGen:

    def randGCL(self, seed, rep): #Linear congruential generator
        val = []
        a=25214903917
        c=11
        m=2**64
        for i in range(0,rep):
            
            if i==0:
                x = ((seed * a + c) % m) / m
                #x = (seed * a + c) % m
                val.append(x)
            else:
                x = ((val[i-1] * a + c) % m) / m
                #x = (val[i-1] * a + c) % m
                val.append(x)
        return val

    def randLFG(self,seed1,seed2,rep): #Lagged Fibonacci generator
        fibseq=[seed1,seed2]
        j = 65
        k = 71
        m=2**64
        val=[]
        for i in range(0,k-2):
            fibseq.append(fibseq[i] + fibseq[i+1])

        for n in range(rep):
            for i in range(len(fibseq)):
                if i is 0:
                    out = ((fibseq[j-1] + fibseq[k-1]) % m) / m
                    #out = fibseq[j-1] + fibseq[k-1] % m
                elif 0 < i < len(fibseq)-1:
                    fibseq[i] = fibseq[i+1] / m
                    #fibseq[i] = fibseq[i+1]
                else:
                    fibseq[i] = out
                    val.append(out)
        return val


    
