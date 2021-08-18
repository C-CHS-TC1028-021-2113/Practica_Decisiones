import math

def main():
    # Escribe el código que falta
    a=int(input("Da el valor de a: "))
    
    if (a==0) and (b==0):
      #("No tiene solucion")
    elif (a==0):
        raiz=-c/b
        #(raiz)
    else:
        discrim=b**2-4*a*c
        if (discrim)>0:
            x1=(-b+math.sqrt(discrim))/(2*a)
            x2=(-b-math.sqrt(discrim))/(2*a)
            print(x1)
            print(x2)
        elif (discrim < 0):
          #("Raices complejas")
        else:
            x=-b/(2*a)
            print(x)

if __name__ == '__main__':
    main()
