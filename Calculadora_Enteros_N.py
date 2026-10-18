def tamano(numero):
    return len(str(numero))

def mult(u,v):
    
    n = max(tamano(u), tamano(v))    
    if(n <= 1):
        return u*v
    else:
        s = n // 2
        w = u // 10**s
        x = u % 10**s
        y = v // 10**s
        z = v % 10**s
        return mult(w,y)*(10**(2*s)) + (mult(w,z)+mult(x,y))*(10**s) + mult(x,z)

def main():
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    
    signo = -1 if (num1 < 0) != (num2 < 0) else 1
    resultado = signo * mult(abs(num1), abs(num2))
    
    print(f"Multiplicándolos: {num1} x {num2} = {resultado}")
main()        
    