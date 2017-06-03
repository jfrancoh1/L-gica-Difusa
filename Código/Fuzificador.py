from ConjuntosDifusos import *

def lluvia(x):
	x1=("{0:.2f}".format(lluviaDebil(x)))
	x2=("{0:.2f}".format(lluviaFuerte(x)))
	x3=("{0:.2f}".format(lluviaTorrencial(x)))
	return x1,x2,x3
	
def agua(y):
	y1=("{0:.2f}".format(aguaMuybaja(y)))
	y2=("{0:.2f}".format(aguaModerada(y)))
	y3=("{0:.2f}".format(aguaMuyalta(y)))
	return y1,y2,y3
	
def tapa(z):
	z1=("{0:.2f}".format(totalmenteTapada(z)))
	z2=("{0:.2f}".format(tapaModerada(z)))
	z3=("{0:.2f}".format(totalmenteDestapada(z)))
	return z1,z2,z3
	
def degreePertenence(x,y,z):
	x1,x2,x3=lluvia(x)[0],lluvia(x)[1],lluvia(x)[2]
	y1,y2,y3=agua(y)[0],agua(y)[1],agua(y)[2]
	z1,z2,z3=tapa(z)[0],tapa(z)[1],tapa(z)[2]
	return (x1,x2,x3,y1,y2,y3,z1,z2,z3)


