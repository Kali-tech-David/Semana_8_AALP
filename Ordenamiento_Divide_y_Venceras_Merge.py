def DivVenMerge(array):
    p = 0
    r = len(array) - 1
    if (p >= r):
        return array
    
    q = (p + r) // 2
    
    arrayP = array[p:q+1]
    arrayR = array[q+1:r+1]
    
    return Comb_Merge(DivVenMerge(arrayP), DivVenMerge(arrayR))
def Comb_Merge(arrayP, arrayR):
    resultado = []
    while len(arrayP) > 0 and len(arrayR) > 0:
        if arrayP[0] < arrayR[0]:
            resultado.append(arrayP.pop(0))
        else:
            resultado.append(arrayR.pop(0))
    if len(arrayP) > 0:
        resultado.extend(arrayP)
    if len(arrayR) > 0:
        resultado.extend(arrayR)
    return resultado

def main():
    array = [int(x) for x in input("Ingrese los elementos del arreglo separados por espacios: ").split()]
    resultado = DivVenMerge(array)
    print(f"El arreglo ordenado es: {resultado}")    
main()