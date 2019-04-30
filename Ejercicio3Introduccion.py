a=float(input("Numero de segundos "))
if a<(60*60):
    print("tenemos "+str(int(a/60))+" minutos y "+str(int(a%60))+" segundos")
else:
    print("tenemos "+str(int(a/(60*60)))+" horas "+str(int((a%(60*60))/60))+" minutos y "+str(int(a%60))+" segundos")
