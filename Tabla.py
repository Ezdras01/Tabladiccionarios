import Diccionario
from tabulate import tabulate
#print(tabulate(headers=["Numeros","Español","Alemán","Frances","Ingles"]))
print("Tabla de Traducciones\n")
for i in range(1,4):
    if i == 1:
        print(tabulate([[i,Diccionario.dics['esp'][str(i)],Diccionario.dics['deutsch'][str(i)],Diccionario.dics['francais'][str(i)],Diccionario.dics['english'][str(i)]]],headers=["Numeros","Español","Alemán","Frances","Ingles"]))
    else:
        print(tabulate([[i,Diccionario.dics['esp'][str(i)],Diccionario.dics['deutsch'][str(i)],Diccionario.dics['francais'][str(i)],Diccionario.dics['english'][str(i)]]],headers=["       ","       ","      ","       ","      "]))