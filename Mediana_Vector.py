def mediana(array):
    if(len(array)%2 != 0):
        imed = len(array) // 2
        return calcMediana(array, imed, 0, len(array) - 1)
    else:
        imed1 = len(array) // 2
        imed2 = len(array) // 2 - 1
        
        med1 = calcMediana(list(array), imed1, 0, len(array) - 1)
        med2 = calcMediana(list(array), imed2, 0, len(array) - 1)
        return (float)(med1 + med2) / 2.0

def calcMediana(array, imed, lI, lS):
    if(lI == lS):
        return array[lI]
    
    idx_pivote = lI + (lS - lI) // 2
    a = array[idx_pivote]
    array[idx_pivote], array[lS] = array[lS], array[idx_pivote]
    iR = lI
    for i in range(lI, lS):
        if(array[i] < a):
            array[iR], array[i] = array[i], array[iR]
            iR += 1
    array[iR], array[lS] = array[lS], array[iR]
    
    if(iR == imed):
        return array[iR]
    elif(iR > imed):
        return calcMediana(array, imed, lI, iR - 1)
    else:
        return calcMediana(array, imed, iR + 1, lS)

def main():
    array = [int(x) for x in input("Ingrese los elementos del arreglo separados por espacio: ").split()]
    resultado = mediana(array)
    print(f"La mediana del arreglo es: {resultado}")

main()
