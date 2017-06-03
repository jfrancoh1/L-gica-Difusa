def inference(Lista):
	numerador=0
	denominador=0
	for i in range(101):
		numerador+=Lista[i]*i
		denominador+=Lista[i]
	result = numerador/denominador
	return result
