def heuristica(l):
     h = len(l)
     soma = 0
     for i in range(h):
        for j in range(h):
            if i != j and (l[i] - i == l[j] - j or l[i] + i == l[j] + j):
                soma = soma + 1 
                print "primeira", l[i],i
                print "segunda", l[j],j
     return soma

l = [2,1,7,4,0,6,3,5]

print heuristica(l)
