import  urllib2
import json
from pyspark import SparkContext

response = urllib2.urlopen('http://144.202.34.148:8080/GetDat')
data = json.load(response)
print data

def maxmin(valor, pos):
	if(valor!=[]):
		mayor = valor[0]
		menor = valor[0]
		i = 0
		while i < len(valor):
			if valor[i] <= menor:
				menor = valor[i]
			else:
				mayor = valor[i]
			i += 1
		print ("La mayor distancia de la posicion ",pos," es: ",mayor," y el menor es :",menor)
	else:
		print("Sin datos disponibles para la posicion: ",pos)

if __name__ == "__main__":
    sc = SparkContext.getOrCreate();
    def pros(p):
        izquierda = []
        derecha = []
        for e in data:
            if (e.get('estado') == "Izquierda"):
                izquierda += [e.get('distancia')]
            elif (e.get('estado') == "Derecha"):
                derecha += [e.get('distancia')]                
                
            
        maxmin(izquierda,"izquierda")
        maxmin(derecha,"derecha")

sc.parallelize([1], 4).map(pros).collect()

