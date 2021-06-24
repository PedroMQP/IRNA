#patrones = [
#				[[0,1,0],[1,0,1],[1,0,1],[1,1,1],[1,0,1]],
#				[[1,1,1],[1,0,0],[1,1,0],[1,0,0],[1,1,1]],
#				[[1,1,1],[0,1,0],[0,1,0],[0,1,0],[1,1,1]],
#				[[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]],
#				[[1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]
#			]

patrones = [
				[[0,0,1],
				 [0,1,1],
				 [0,0,1],
				 [0,0,1],
				 [0,0,1]],

				[[1,1,1],
				 [0,0,1],
				 [1,1,1],
				 [1,0,0],
				 [1,1,1]],

				[[1,1,1],
				 [0,0,1],
				 [0,1,1],
				 [0,0,1],
				 [1,1,1]],

				[[1,0,1],
				 [1,0,1],
				 [1,1,1],
				 [1,0,1],
				 [1,1,1]],
				
				[[1,1,1],
				 [1,0,0],
				 [1,1,1],
				 [0,0,1],
				 [1,1,1]]
			]
tam_fila = 3
n_filas = 5 
votacion_mem = []
W = [[[0]*tam_fila]*tam_fila]*n_filas
def bin_to_dec(bin_seq):
	ex = len(bin_seq) - 1
	res = 0
	for b in bin_seq:
		res += (2**ex)*b
		ex -= 1
	return res
def buscar_apariciones(val,lista):
	indices = []
	for i in range(len(lista)):
		if val == lista[i]:
			indices.append(i)
	return indices
def obtener_columna(i,matriz):
	new_col = []
	for fila in matriz:
		new_col.append(fila[i])
	return new_col
def entrenar():
	for i in range(n_filas):
		swi = []
		for j in range(len(patrones)):
			m = [[0]*tam_fila]*tam_fila
			for k in range(tam_fila):
				act = patrones[j][i][k]
				for l in range(tam_fila):
					aux = m[k][:]
					aux[l] =  act - patrones[j][i][l] 
					m[k] = aux  
					#print("fila",patrones[j][i],"patron",j,"x",act,"y", patrones[i][j][l] )
			#print("**************	")
			swi.append(m)
		for f in range(tam_fila):
			for c in range(tam_fila):
				temp = []
				for p in range(len(swi)):
					temp.append(swi[p][f][c])
				aux = W[i][f][:]
				aux[c] =  min(temp)
				aux2 = W[i][:]
				aux2[f] = aux 
				W[i] = aux2
	for i in range(len(patrones)):#Generamos la matr[iz de votación
		nfila = []#Fila para matriz de votación
		for f in patrones[i]:#Filas del patron
			nfila.append(bin_to_dec(f))
		votacion_mem.append(nfila)

def recuperar(patron):
	votacion = [0]*n_filas
	for i in range(n_filas):
		x = []
		w = W[i]
		c = patron[i]
		for j in range(tam_fila):
			temp = []
			for k in range(tam_fila):
				temp.append(w[j][k]+c[k])
			x.append(max(temp))
		idxs = buscar_apariciones(bin_to_dec(x),obtener_columna(i,votacion_mem))
		#print(idxs)
		for ind in idxs:
			votacion[ind] += 1
	mv = max(votacion)
	for v in range(len(votacion)):
		if votacion[v] == mv:
			return v + 1


entrenar()
print("La memoria generada es")
for fila in votacion_mem:
	print(fila)
print("Las memorias por fila son")
for w in W:
	print(w)
import random
print("Patrones fundamentales")
for p in patrones:
	print("A recuperar",p,"recuperado",recuperar(p))

print("********************** Patrones con ruido aditivo **********************")
for a in patrones:
	fila = random.randrange(len(a))
	indice = random.randrange(len(a[0]))
	p = a[:]
	if p[fila][indice] == 0:
		p[fila][indice] =  1
	else:	
		p[fila][indice] =  0
	print("ruido",p[fila][indice],"en el indice",indice+1,"en la fila",fila+1,"clase",recuperar(p))