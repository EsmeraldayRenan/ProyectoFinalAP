import urllib2  
import json
from operator import add
from pyspark import SparkContext

response = urllib2.urlopen('http://144.202.34.148:8080/GetDat')
data = json.load(response)
print data

def prom(va,estado):
    pro = 0
    for e in va:
        pro += e
    print "El promedio de los valores de la posicion ", estado," es", pro/len(va)

if __name__ == "__main__":
    sc = SparkContext(appName="Promedio de la distancia para los lados ")
    def pro(l):
        izquierda = []
        centro = []
        derecha = []
        for e in data:
            if (e.get('estado') == "Izquierda"):
                izquierda += [e.get('distancia')]
            elif (e.get('estado') == "Derecha"):
                derecha += [e.get('distancia')]
            else:
                centro += [e.get('distancia')]
                
            
        prom(izquierda,"izquierda")
        prom(centro,"centro")
        prom(derecha,"derecha")

a = sc.parallelize([1], 5).map(pro).reduce(add)
print a