seq_tam = 4
patrones = [[-2,-9,90,0],[1,2,3,4],[100,200,300,400],[32,64,21,80]]
etiquetas =[]
pesos = []
memoria = [[0]*seq_tam]*seq_tam
tipo = "M"
def entrenar():
	memorias = []
	for p in patrones:
		m = [[0]*seq_tam]*seq_tam
		for i in range(seq_tam):
			ac = p[i]
			for j in range(seq_tam):
				temp =m[i][:]
				temp[j] = ac - p[j]  
				m[i] = temp 
		memorias.append(m)
	print("Las memorias generadas son:")
	cont = 1
	for mem in memorias:
		print("Memoria",cont)
		for fila in mem:
			print(fila)
		cont +=1
	for i in range(seq_tam):
			for j in range(seq_tam):
				sels = []
				for pt in range(len(patrones)):
					sels.append(memorias[pt][i][j])
				aux = memoria[i][:]
				aux[j] = max(sels) if tipo == "M" else min(sels)
				memoria[i] = aux 
	print("La memoria tipo",tipo,"es")
	for f in memoria:
		print(f)
def recuperar(patron):
	x = []
	for fila in memoria:
		aso = []
		for u in range(len(fila)):
			val = fila[u]+patron[u] if tipo == "M" else fila[u]-patron[u]
			aso.append(val)
		res = min(aso) if tipo == "M" else max(aso)
		x.append(res)
	return(x)
import random
tipo = "M"
entrenar()
print("********************** Patrones fundamentales **********************")
for p in patrones:
	print("A recuperar",p,"recuperado",recuperar(p))

print("********************** Patrones con ruido aditivo **********************")
for i in range(3):
	ruido = random.randrange(10) +1 
	indice = random.randrange(seq_tam)
	print("Patrones con",ruido,"en el indice",indice+1)
	for a in patrones:
		p = a[:]  
		p[indice] += ruido
		print("A recuperar",p,"recuperado",recuperar(p))	