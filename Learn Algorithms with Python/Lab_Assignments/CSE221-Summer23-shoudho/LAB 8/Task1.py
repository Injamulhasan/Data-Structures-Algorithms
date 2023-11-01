class disjointset:

    def __init__(self,a):
        self.par = list(range(a+1)) 
        self.size = [1]*(a+1)

    def find(self,i):

        if self.par[i] !=i:
            self.par[i] = self.find(self.par[i])

        return self.par[i]

    def uni(self,a,b):
        ma = self.find(a)
        nb = self.find(b)

        if ma != nb:

            if self.size[ma] < self.size[nb]:
                ma, nb = nb, ma
            self.par[nb] = ma
            self.size[ma] += self.size[nb]

def kruskal(num_nd,ed):

    ed.sort(key=lambda weight: weight[2])  
    ds = disjointset(num_nd)
    tl_c = 0

    for edg in ed:
        nd1, nd2, ct = edg

        if ds.find(nd1) != ds.find(nd2):  
            ds.uni(nd1,nd2)
            tl_c += ct
    return tl_c

def r_inp(f1):
    f = open(f1,'r')
    a,b = map(int, f.readline().split())
    ed = []

    for _ in range(b):
        
        i,j,k = map(int, f.readline().split())
        ed.append((i,j,k))
    f.close()
    return a,ed

def w_out(output, f1):
    f = open(f1, 'w')
    f.write(str(output))
    f.close()

f1 = "input1.txt"
a, ed = r_inp(f1)
res = kruskal(a, ed)
f2 = "output1.txt"
w_out(res,f2)
