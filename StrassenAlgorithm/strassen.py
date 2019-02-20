# coded by duncanista / Jordan Gonzalez Bustamante

def getMatrix(path):
    file = open(path, 'r').read().splitlines()
    matrix = []
    for line in file:
        matrix.append(list(map(int,line.split(','))))
    return matrix

def getMatrixOrder(matrix):
    return len(matrix)

def generateMatrix(size):
    return [[0 for i in range(size)] for j in range(size)]

def sumMatrices(a,b):
    order = getMatrixOrder(a)
    c = generateMatrix(order)
    for i in range(order):
        for j in range(order):
            c[i][j] = a[i][j] + b[i][j]
    return c

def substractMatrices(a,b):
    order = getMatrixOrder(a)
    c = generateMatrix(order)
    for i in range(order):
        for j in range(order):
            c[i][j] = a[i][j] - b[i][j]
    return c

def toString(matrix):
    s = ''
    for line in matrix:
        s += "\t".join(list(map(str, line))) + "\n"
    return s

def strassenMethod(a,b):
    order = getMatrixOrder(a)
    if(order <= 2):
        c = generateMatrix(order)
        for i in range(order):
            for k in range(order):
                for j in range(order):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    else:
        # dividing matrixC
        size = int(order/2)
        # this for A matrix
        a11 = generateMatrix(size)
        a12 = generateMatrix(size)
        a21 = generateMatrix(size)
        a22 = generateMatrix(size)
        # this for B matrix
        b11 = generateMatrix(size)
        b12 = generateMatrix(size)
        b21 = generateMatrix(size)
        b22 = generateMatrix(size)
        # traverse both matrices and diving them into 4
        for i in range(size):
            for j in range(size):
                a11[i][j] = a[i][j]
                a12[i][j] = a[i][j + size]
                a21[i][j] = a[i + size][j]
                a22[i][j] = a[i + size][j + size]

                b11[i][j] = b[i][j]
                b12[i][j] = b[i][j + size]
                b21[i][j] = b[i + size][j]
                b22[i][j] = b[i + size][j + size]

        m1 = strassenMethod(sumMatrices(a11, a22), sumMatrices(b11, b22))
        m2 = strassenMethod(sumMatrices(a21, a22), b11)
        m3 = strassenMethod(a11, substractMatrices(b12,b22))
        m4 = strassenMethod(a22, substractMatrices(b21, b11))
        m5 = strassenMethod(sumMatrices(a11, a12), b22)
        m6 = strassenMethod(substractMatrices(a21, a11), sumMatrices(b11, b12))
        m7 = strassenMethod(substractMatrices(a12, a22), sumMatrices(b21, b22))

        c11 = substractMatrices(sumMatrices(sumMatrices(m1, m4), m7), m5)
        c12 = sumMatrices(m3, m5)
        c21 = sumMatrices(m2, m4)
        c22 = substractMatrices(sumMatrices(m1,sumMatrices(m3,m6)), m2)

        c = generateMatrix(order)

        for i in range(size):
            for j in range(size):
                c[i][j] = c11[i][j]
                c[i][j + size] = c12[i][j]
                c[i + size][j] = c21[i][j]
                c[i + size][j + size] = c22[i][j]
        return c

m1 = getMatrix('16.txt')
m2 = getMatrix('16-2.txt')
if(getMatrixOrder(m1) == getMatrixOrder(m2)):
    print(toString(strassenMethod(m1,m2)))
else:
    pass




