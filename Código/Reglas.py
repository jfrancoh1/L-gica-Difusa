from Fuzificador import *
from Desfuzificador import *

def desfucaso1(valores, corte, cruce2, r1, r2, r1val, r2val, funcion1, funcion2):
	for i in range (r1val, corte+1):
		valores[i] = funcion1(i)
	for i in range (corte+1, r2val+1):
		valores[i] = funcion2(i)
	for i in range (r2val+1, cruce2+1):
		valores[i] = r2

def desfucaso2(valores, corte, cruce2, r1, r2, r1val, r2val, funcion):
	for i in range (r1val, corte+1):
		valores[i] = funcion(i)
	for i in range (corte+1, cruce2+1):
		valores[i] = r2
		
def desfucaso3(valores, corte, cruce, cruce2, r1, r2, r1val, r2val, funcion):
	for i in range (corte, cruce):
		valores[i] = funcion(i)
	for i in range (cruce, r2val+1):
		valores[i] = funcion(i)
	for i in range (r2val+1, cruce2):
		valores[i] = r2
		
def Desfuzificacion(r1Tapaval,r2Tapavalizq,r2Tapavalder,r3Tapaval, r1Tapa, r2Tapa, r3Tapa):
	valores=[]
	r1Tapaval=int(r1Tapaval)
	r2Tapavalizq=int(r2Tapavalizq)
	r2Tapavalder=int(r2Tapavalder)
	r3Tapaval=int(r3Tapaval)
	for i in range (101):  				
		valores.append(0)
	for i in range (r1Tapaval+1):					
		valores[i]=r1Tapa 
	for i in range (r1Tapaval+1,31):								
		valores[i]=totalmenteTapada(i)
	if(r1Tapaval <= 25 and r2Tapavalizq >= 25):
		desfucaso1(valores, 25, 40, r1Tapa, r2Tapa, r1Tapaval, r2Tapavalizq, totalmenteTapada, tapaModerada)
	if(r2Tapavalizq < 25):
		cort = int(totalmenteTapadax(r2Tapa))
		desfucaso2(valores, cort, 40, r1Tapa, r2Tapa, r1Tapaval, r2Tapavalizq, totalmenteTapada)
	if(r1Tapaval > 25 and (r1Tapa<r2Tapa)):
		cort = int(tapaModeradaizqx(r1Tapa))
		desfucaso3(valores, cort, 25, 41, r1Tapa, r2Tapa, r1Tapaval,r2Tapavalizq, tapaModerada)
	for i in range(41, r2Tapavalder+1):		
		valores[i]=r2Tapa
	for i in range(r2Tapavalder+1, 71):
		valores[i]=tapaModerada(i)
	if(r2Tapavalder <= 65 and r3Tapaval >= 65):
		desfucaso1(valores, 65, 100, r2Tapa, r3Tapa, r2Tapavalder, r3Tapaval, tapaModerada, totalmenteDestapada)
	if(r3Tapaval < 65):
		cort = int(tapaModeradaderx(r3Tapa))
		desfucaso2(valores, cort, 100, r2Tapa, r3Tapa, r2Tapavalder ,r3Tapaval, tapaModerada)
	if(r2Tapavalder > 65 and (r2Tapa<r3Tapa)):
		cort = int(tapaModeradaderx(r2Tapa))
		desfucaso3(valores, cort, 65, 100, r2Tapa, r3Tapa, r2Tapavalder,r3Tapaval, totalmenteDestapada)
	return valores							
	
"""Esta función determina el valor según las reglas definidas y además define los valors xtremos según los cortes de cada valor con el eje x para
armar el conjunto a desfuzificar"""

def reglasTapa(x1,x2,x3,y1,y2,y3,z1,z2,z3):
	r1Tapa=float(x3)			#if  lluvia is torrencial then tapa totalmente cerrada
	r4Tapa=float(y3)			#if agua is muy alta then tapa totalmente cerrado
	r2Tapa=float(min(x2,y2))	#if lluvia is moderada and agua is mediana then tapa medio abierta
	r3Tapa=float(max(x2,y1))	#if lluvia is moderada or agua muy baja then tapa totalmente abierta
	r1Tapa=max(r1Tapa, r4Tapa)  #Se elige la max entre los valores posibles para la regla de totalmente cerrada
	r1Tapaval=round(totalmenteTapadax(r1Tapa))   # Hallar el punto x en que se corta el valor fuzificado con el conjunto z1
	r2Tapavalizq=round(tapaModeradaizqx(r2Tapa)) # Hallar el punto x en que se corta el valor fuzificado con el conjunto z2 a la izquierda
	r2Tapavalder=round(tapaModeradaderx(r2Tapa)) # Hallar el punto x en que se corta el valor fuzificado con el conjunto z2 a la derecha
	r3Tapaval=round(totalmenteDestapadax(r3Tapa))# Hallar el punto x en que se corta el valor fuzificado con el conjunto z3
	"""print("Valor regla 1 = ", r1Tapa)
	print("Valor regla 2 = ", r2Tapa)
	print("Valor regla 3 = ", r2Tapa)
	print("Valor x regla 1 = ", r1Tapaval)
	print("Valor x regla 2 derecha = ", r2Tapavalizq)
	print("Valor x regla 2 izquierda = ", r2Tapavalder)
	print("Valor x regla 3 = ", r3Tapaval)"""
	Listat = Desfuzificacion(r1Tapaval,r2Tapavalizq,r2Tapavalder,r3Tapaval,r1Tapa,r2Tapa,r3Tapa)
	return Listat
	
def reglasLlave(x1,x2,x3,y1,y2,y3,z1,z2,z3):
	r1Llave=float(x3)
	r1Llaveaux=float(y3)
	r2aux=float(max(x2,y1))
	r2Llaveaux2=float(min(r2aux, float(z2)))
	r2Llaveaux3=float(min(y2, z3))
	r2aux4=float(max(x2,y1))
	r2Llaveaux5=float(min(r2aux4, float(z1)))
	r2Llaveaux2=max(r2Llaveaux2, r2Llaveaux3, r2Llaveaux5)
	r1Llave=max(r1Llave, r1Llaveaux)
	r2Llave = r2Llaveaux2  
	r3Llave=float(y1)
	r1Llaveval=round(totalmenteTapadax(r1Llave))   # Hallar el punto x en que se corta el valor fuzificado con el conjunto w1
	r2Llavevalizq=round(tapaModeradaizqx(r2Llave)) # Hallar el punto x en que se corta el valor fuzificado con el conjunto w2 a la izquierda
	r2Llavevalder=round(tapaModeradaderx(r2Llave)) # Hallar el punto x en que se corta el valor fuzificado con el conjunto w2 a la derecha
	r3Llaveval=round(totalmenteDestapadax(r3Llave))# Hallar el punto x en que se corta el valor fuzificado con el conjunto w3
	"""print("Valor regla 1 = ", r1Tapa)
	print("Valor regla 2 = ", r2Tapa)
	print("Valor regla 3 = ", r2Tapa)
	print("Valor x regla 1 = ", r1Tapaval)
	print("Valor x regla 2 derecha = ", r2Tapavalizq)
	print("Valor x regla 2 izquierda = ", r2Tapavalder)
	print("Valor x regla 3 = ", r3Tapaval)"""
	Listal = Desfuzificacion(r1Llaveval,r2Llavevalizq,r2Llavevalder,r3Llaveval,r1Llave,r2Llave,r3Llave)
	return Listal
