from numpy import array

def saisie():
    n = int(input("donner la taille de la matrice: "))
    return n

def remplir(m, n):
    for i in range(n):
        for j in range(n):
            m[i][j] = int(input("m[" + str(i) + "][" + str(j) + "]= "))


def afichage(m, n):
    p = 1
    sp = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] % 2 == 0:
                sp = sp + m[i][j]
            else:
                p = p * m[i][j]
    print("la somme des éléments pairs est: ", sp)
    print("le produit des éléments impairs est: ", p)

# pp--
n = saisie()
m = array([[int] * n] * n)
remplir(m, n)
afichage(m, n)
