import pygame
import sys
import math

ANCHO=800
ALTO=700
ROJO=(255,0,0)
AZUL=(0,0,255)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
VERDE=(0,255,0)
AMARILLO=(255,255,0)
VIOLETA=(255,0,255)
AZULS=(0,255,255)
NARANJA=(255, 130,0)

ANCHO=1400
ALTO=500
ox = int(ANCHO/2)
oy = int(ALTO/2)
origen = (ox, oy)
pantalla = pygame.display.set_mode([ANCHO,ALTO])
ox1 = 0
oy1 = ALTO
origen1 = (ox1, oy1)

def Planosen():
    xini=(0,ALTO)
    xfin=(ANCHO,ALTO)
    yini=(0,ALTO)
    yfin=(0,0)
    pygame.draw.line(pantalla, AZUL, xini, xfin, 5)
    pygame.draw.line(pantalla, AZUL, yini, yfin, 5)
  
def Tras_punto1(x, y):
    nx = ox1 + x
    ny = oy1 - y
    return (nx, ny) 
     
def Plano():
    xini=(0,int(ALTO/2))
    xfin=(ANCHO,int(ALTO/2))
    yini=(int(ANCHO/2),0)
    yfin=(int(ANCHO/2),ALTO)
    pygame.draw.line(pantalla, AZUL, xini, xfin, 2)
    pygame.draw.line(pantalla, AZUL, yini, yfin, 2)
    
def Vector(xi,yi,xf,yf):
    tx = xi+xf
    ty = yi-yf
    return(tx,ty)
    
def Tras_punto(x, y):
    nx = ox + x
    ny = oy - y
    return (nx, ny)
    
def Dibujar(origen, v, c):
    pygame.draw.aaline(pantalla, c, origen, v, 2)
    
def DibujarCon(origen, v, c):
    pygame.draw.line(pantalla, c, origen, v, 5)
    
def Suma_vec(x1, y1, x2, y2):
    svx = x1 + x2
    svy = y1 + y2
    nvec = Vector(ox, oy, svx, svy)
    return nvec

def Suma_vector(ox, oy, x1v, y1v, x2v, y2v):   
    vec1 = Vector(ox,oy,x1v,x2v)
    vec2 = Vector(ox,oy,x2v,y2v)
    vecs = Suma_vec(x1v,y1v,x2v,y2v, ox, oy)
    Dibujar(origen, vec1, ROJO)
    Dibujar(origen, vec2, ROJO)
    Dibujar(origen, vecs, AZUL)

def Resta_vec(x1, y1, x2, y2):
    svx = x1 - x2
    svy = y1 - y2
    nvec = Vector(ox, oy, svx, svy)
    return nvec

def Resta_vector(x1v, y1v, x2v, y2v):   
    vec1 = Vector(ox,oy,x1v,x2v)
    vec2 = Vector(ox,oy,x2v,y2v)
    vecr = Resta_vec(x1v,y1v,x2v,y2v, ox, oy)
    Dibujar(origen, vec1, ROJO)
    Dibujar(origen, vec2, ROJO)
    Dibujar(origen, vecr, AZUL)

def Conv_a_rec(grados, vx, vy, R):
    x2v = int(R*(math.cos(math.radians(grados)))) + vx
    y2v = int(R*(math.sin(math.radians(grados)))) + vy
    return (x2v, y2v)
    
def Dibujar_angle(grados, x1v, y1v, R, C):
    newori = Tras_punto(x1v, y1v)
    v = Conv_a_rec(grados, 0, 0, R)
    nvec = Vector(newori[0], newori[1], v[0], v[1])
    Dibujar(newori, nvec, C)

def Dibujar_tria(l1, grados, v):
	Dibujar_angle(180-grados, v, v, l1, ROJO)
	Dibujar_angle(grados, v, v, l1, ROJO)
	rl1 = Conv_a_rec(grados, v, v, l1)
	rl2 = Conv_a_rec(180-grados, v, v, l1)
	rl1t = Tras_punto(rl1[0], rl1[1])
	rl2t = Tras_punto(rl2[0], rl2[1])
	Dibujar(rl1t, rl2t, ROJO)
	return (rl1, rl2)
	
def Dibujar_triangle(x1, y1, x2, y2, x3, y3):
    p1 = Tras_punto(x1, y1)
    p2 = Tras_punto(x2, y2)
    p3 = Tras_punto(x3, y3)

    Dibujar(p1, p2, NEGRO)
    Dibujar(p2, p3, NEGRO)
    Dibujar(p3, p1, NEGRO)

def Dibujar_tri(l1, l2, grados, R):
    compl1 = Conv_a_rec(grados, 0, 0, l1)
    compl2 = Conv_a_rec(0, 0, 0, l2)
    l1f = Tras_punto(compl1[0], compl1[1])
    l2f = Tras_punto(compl2[0], compl2[1])
    Dibujar(origen, l1f, NEGRO)
    Dibujar(origen, l2f, NEGRO)
    Dibujar(l1f, l2f, NEGRO)

def Ecuacion(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    b = (y1-(m*x1))
    return(m,b)
    
def Punto_ini(m,b):
    Xini = (-ANCHO/2)
    Yini = (m*(-ANCHO/2))+b
    
    return (Xini, Yini)
    
def Punto_fin(m,b):
    Xfin = (ANCHO/2)
    Yfin = ((m*ANCHO/2) + b)
    return (Xfin, Yfin)

def circu(pantalla, R):
    NR = Tras_punto(R, 0)
    pygame.draw.circle(pantalla, BLANCO, origen, int(R), 2)
    Dibujar(origen, NR, NEGRO)

def rotacion_pun(x, y, grados):
    nx = int(x*(math.cos(math.radians(grados))) - y*(math.sin(math.radians(grados))))
    ny = int(x*(math.sin(math.radians(grados))) + y*(math.cos(math.radians(grados))))
    return (nx, ny)
    
def rotacion(x, y, dx, dy, grados):
    nx = int(dx+((math.cos(math.radians(grados)))*(x-dx)) - ((math.sin(math.radians(grados)))*(y-dy)))
    ny = int(dy+((x-dx)*(math.sin(math.radians(grados)))) + ((y-dy)*(math.cos(math.radians(grados)))))
    return (nx, ny)
    
def poligono(puntos):
    lp = []
    for pto in puntos:
        x = pto[0]
        y = pto[1]
        lp.append(Tras_punto(x, y))
    pygame.draw.polygon(pantalla, ROJO, lp, 1)
       
def escalonar(puntos, Sx, Sy):
    lp = []
    dx = puntos[0][0]
    dy = puntos[0][1]
    for pto in puntos:
        E = ((Sx*(pto[0]-dx)+dx), (Sy*(pto[1]-dy)+dy))
        lp.append(Tras_punto(E[0],E[1]))
    pygame.draw.polygon(pantalla, ROJO, lp, 1)

def rotar(puntos, grados):
    lp = []
    dx = puntos[0][0]
    dy = puntos[0][1]
    for pto in puntos:
        Rot = rotacion(pto[0], pto[1], dx, dy, grados)
        lp.append(Tras_punto(Rot[0], Rot[1]))
    pygame.draw.polygon(pantalla, ROJO, lp, 1)
	
def fun1(x):
	return x*x+2

def fun2(x,a):
	return a*(1+math.cos(math.radians(x)))

def fun3(x,a):
	return a*math.sin(math.radians(2*x))

def fun4(x,a):
	return a*2*math.sin(math.radians(3*x))

def fun5(x,a):
	return a*1/2+math.cos(math.radians(x))
	
def curva(color):
	for i in range(-15, 15):
		ini = Tras_punto(i, fun1(i))
		fin = Tras_punto(i+1, fun1(i+1))
		pygame.draw.aaline(pantalla, color, ini, fin, 3)

def curva2(color, a):
	for i in range(0, 360):
		ini = Conv_a_rec(i+180, ox, oy, fun2(i,a))
		fin = Conv_a_rec(i+180, ox, oy, fun2(i+1,a))
		pygame.draw.aaline(pantalla, color, ini, fin, 3)

def curva3(color, a):
	for i in range(0,360):
		ini = Conv_a_rec(i+180, ox, oy, fun3(i,a))
		fin = Conv_a_rec(i+180, ox, oy, fun3(i+1,a))
		pygame.draw.aaline(pantalla, color, ini, fin, 3)

def curva4(color, a):
	for i in range(0, 360):
		ini = Conv_a_rec(i+180, ox, oy, fun4(i,a))
		fin = Conv_a_rec(i+180, ox, oy, fun4(i+1,a))
		pygame.draw.aaline(pantalla, color, ini, fin, 3)

def curva5(color, a):
	for i in range(0,360):
		ini = Conv_a_rec(i+180, ox, oy, fun5(i,a))
		fin = Conv_a_rec(i+180, ox, oy, fun5(i+1,a))
		pygame.draw.aaline(pantalla, color, ini, fin, 3)

