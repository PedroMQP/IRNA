nclases = 6
seq_tam = 3
patrones = [
			 [[4,4,4],[4,4,5],[4,5,5],[5,4,4],[5,4,5]],
			 [[10,9,10],[9,9,10],[10,10,10],[10,11,11],[10,9,11]],
			 [[100,100,100],[100,200,100],[200,100,100],[100,100,200],[200,200,200]],
			 [[1000,900,1000],[900,900,1000],[1000,1000,1000],[1000,1100,1100],[1000,900,1100]]

		   ]
memoria = []
def entrenar():
	for clase in patrones:
		t = []
		for  i in range(seq_tam): 
			suma = 0
			tam = len(clase)
			for j in range(tam):
				suma += clase[j][i]
			t.append(suma/tam)
		memoria.append(t)

def recuperar(p):
	x = []
	for f in range(len(memoria)):
		e = []
		for i in range(len(p)):
			val = memoria[f][i]
			e.append(abs(val-p[i]))
		x.append(max(e))

	minimo = min(x)
	cont = 0
	for j in range(len(x)):
		if x[j] == minimo:
			return j + 1
entrenar()
print("La memoria generada es")
for fila in memoria:
	print(fila)

import random
print("Patrones fundamentales")
for p in patrones:
	for sp in p: 
		print("A recuperar",sp,"recuperado",recuperar(sp))

print("********************** Patrones con ruido aditivo **********************")
for a in patrones:
	for sp in a:
		ruido = random.randrange(10) +1 
		indice = random.randrange(seq_tam)
		p = sp[:]  
		p[indice] += ruido
		print("ruido",ruido,"en el indice",indice+1,"clase",recuperar(p))
		#print("A recuperar",p,"recuperado",recuperar(p))	
