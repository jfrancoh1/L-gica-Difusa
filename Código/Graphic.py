import pygame
import sys
import math
from libreplano import *
from pyg import *

ROJO=(255,0,0)
AZUL=(0,0,255)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
VERDE=(0,255,0)
AMARILLO=(255,255,0)
VIOLETA=(255,0,255)
AZULS=(0,255,255)
NARANJA=(255, 130,0)

ANCHO=1000
ALTO=500

def DibujarLTapa(Lista, c1, c2, c3):
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO,ALTO])
	pantalla.fill(BLANCO)
	Planosen()
	p1 = Tras_punto1(0, 100)
	p2 = Tras_punto1(100, 100)
	p3 = Tras_punto1(300, 0)
	Dibujar(p1, p2, ROJO)
	Dibujar(p2, p3, ROJO)
	p1 = Tras_punto1(200, 0)
	p2 = Tras_punto1(400, 100)
	Dibujar(p1, p2, AZUL)
	p1 = Tras_punto1(400, 100)
	p2 = Tras_punto1(700, 0)
	Dibujar(p1, p2, AZUL)
	p1 = Tras_punto1(600, 0)
	p2 = Tras_punto1(900, 100)
	p3 = Tras_punto1(1000, 100)
	Dibujar(p1, p2, VERDE)
	Dibujar(p2, p3, VERDE)
	for i in range (100):
		p1 = Tras_punto1(i*10, Lista[i]*100)
		p2 = Tras_punto1((i+1)*10, Lista[i+1]*100)
		DibujarCon(p1, p2, NARANJA)
	text = Text()
	text.render(pantalla, c1, AZUL, (80, 450))
	text.render(pantalla, c2, AZUL, (400, 450))
	text.render(pantalla, c3, AZUL, (850, 450))
	
	pygame.display.flip()
			
	while True:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
