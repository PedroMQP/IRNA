seq_tam = 4
patrones = [[10,15,13,17],[1,2,3,4],[10,20,30,40],[32,64,21,80]]
#seq_tam = 3
#patrones = [[1,0,1],[4,2,3],[6,5,5]]
etiquetas =[]
pesos = []
memoria = [[0]*seq_tam]*seq_tam
L = 128

def entrenar():
	matrices = []
	for i in range(len(patrones)):
		m = [[0]*seq_tam]*seq_tam
		for j in range(seq_tam):
			ac = patrones[i][j]
			for k in range(seq_tam):
				aux = m[j][:]
				aux[k] = ac - patrones[i][k] + L - 1
				m[j] = aux
		matrices.append(m)
	cont = 0
	for mat in matrices:
		cont += 1
		print("Matriz",cont)
		print(mat)
	for i in range(seq_tam):
		for j in range(seq_tam):
			sels = []
			for m in matrices:
				sels.append(m[i][j])

			aux = memoria[i][:]

			aux[j] = max(sels)
			memoria[i] = aux

def recuperar(p):
	x = []
	for f in range(len(memoria)):
		e = []
		for i in range(len(p)):
			val = memoria[f][i]
			res = 0
			if  val+p[i] >= L and val+p[i] < 2 * (L - 1): 
				res = val+p[i] - (L-1)
			elif val+p[i] >= 2 * (L - 1):
				res = L - 1
			elif val+p[i] <= L - 1:
				res = 0
			e.append(res)
		x.append(min(e))

	return x	
entrenar()
for m in memoria:
	print(m)
import random
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

