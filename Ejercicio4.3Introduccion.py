try:
    a=int(input("escribe un numero entero "))
    b=int(input("escribe un numero entero "))
    milista=[]
    if a<b:
        while a==b:
            milista.append(a)
            a+=1

    elif b<a:
        while a == b:
            milista.append(b)
            b+=1
    else:
        milista.append(a)
    print(milista)

    # if a%2==0:
    #     print("el número "+ str (a)+ " es divisible por 2")
    # else:
    #     print("el número "+ str (a)+ " no es divisible por 2")
except:
    print("el dato introducido no es un numero entero")