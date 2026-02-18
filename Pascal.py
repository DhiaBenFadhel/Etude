from numpy import array

# saisie
def saisie():
    n = int(input("donner la taille de la matrice: "))
    while not 3 < n < 10:
        n = int(input("donner la taille de la matrice: "))
    return n


# remplir
def remplir(m, n):
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i :
                m[i][j] = 1
            else:
                m[i][j] = m[i - 1][j] + m[i - 1][j - 1]


# afficher
def afficher(m, n):
    for i in range(n):
        for j in range(i+1):
            print(m[i][j], end=" ")
        print()


# pp
n = saisie()
m = array([[0]*n for i in range(n)])
remplir(m, n)
afficher(m, n)
