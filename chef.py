T = 1
#T = int(input())

def crear_arbol():
    N = int(input())
    l = list()
    for j in range(N):
        (x, y, z) = map(int, input().split())
        l.append([x, y, z])
        
    return l



for i in range(T):
    arbol = crear_arbol()
    


