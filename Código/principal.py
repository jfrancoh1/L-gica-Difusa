from Fuzificador import *
from Reglas import *
from Inference import *
from Graphic import *

def principal():
	x = float(input("Ingrese la cantidad de lluvia en mm/h: "))
	y = float(input("Ingrese la cantidad de agua en el tanque en litros: "))
	z = float(input("Ingrese la apertura de la tapa en porcentaje: "))
	x1,x2,x3,y1,y2,y3,z1,z2,z3=degreePertenence(x,y,z)
	listaTapa = reglasTapa(x1,x2,x3,y1,y2,y3,z1,z2,z3)
	listaLlave = reglasLlave(x1,x2,x3,y1,y2,y3,z1,z2,z3)
	resultadoTapa=inference(listaTapa)
	resultadoLlave=inference(listaLlave)
	"""if(y>=25):
		resultadoLlave=0
		print("Alerta, cerrar la llave completamente, tanque lleno.")"""
	print ("Mover La tapa ", resultadoTapa, "%")
	print ("Abrir la llave ", resultadoLlave, "%")
	DibujarLTapa(listaTapa, "z1", "z2", "z3")
	#DibujarLTapa(listaLlave, "w1", "w2", "w3")

principal()
	
