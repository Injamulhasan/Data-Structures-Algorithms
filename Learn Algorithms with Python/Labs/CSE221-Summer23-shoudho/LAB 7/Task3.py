class disjointset:
    def __init__(self, p):
        self.par = list(range(p+1))
        self.size = [1]*(p+1)

    def find(self, a):
        if self.par[a] !=a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]

    def union(self,x,y):
        xa = self.find(x)
        xb = self.find(y)
        if xa !=xb:
            if self.size[xa] < self.size[xb]:
                xa,xb =xb,xa
            self.par[xb] =xa
            self.size[xa]+=self.size[xb]

def r_inp(f3):
    f = open(f3, 'r')
    j, k = map(int, f.readline().split())
    ds = disjointset()
    ds.init(j)
    unions = []
    for i in range(k):
        m,n= map(int, f.readline().split())
        ds.union(m,n)
        unions.append(ds.size[ds.find(m)])
    f.close()
    return unions

def w_out(out, f3):
    f= open(f3, 'w')
    for value in out:
        f.write(str(value) + "\n")
    f.close()

f3= "input3.txt"
uni = r_inp(f3)
f3 = "output3.txt"
w_out(uni, f3)

