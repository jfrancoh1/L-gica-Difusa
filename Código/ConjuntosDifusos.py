def lluviaDebil(x):  					# Conjunto x1: LluviaDebil
	if(x < 5):							# 1 para 0<=x<=5
		valx = 1
	if (5 <= x <= 20):
		valx = (((-1/15)*x)+(4/3))		# (-1/15)x+(4/3) para 5<=x <=20
	if (x > 20):
		valx = 0						# 0 para x>20
	return valx
	
def lluviaFuerte(x): 					# Conjunto x2: LluviaFuerte
	if (x < 10):						# Conjunto x1: LluviaDebil
		valx = 0
	if (10 <= x <= 30):
		valx = (((1/20)*x)-(1/2))
	if (30 <= x <= 50):
		valx = (((-1/20)*x)+(5/2))
	if (x > 50):
		valx = 0
	return valx
	
def lluviaTorrencial(x): 				# Conjunto x3: LluviaTorrencial
	if (x < 50):
		valx = 0
	if (50 <= x <= 60):
		valx = (((1/20)*x)-(2))
	if (x > 60):
		valx = 1
	return valx
	
def aguaMuybaja(x):
	if(x < 5):
		valx = 1
	if (5 <= x <= 12):
		valx = (((-1/7)*x)+(12/7))
	if (x > 12):
		valx = 0
	return valx
	
def aguaModerada(x):
	if (x < 7):
		valx = 0
	if (7 < x <= 13):
		valx = (((1/6)*x)-(7/6))
	if (x == 7):
		valx = 0
	if (13 <= x <= 19):
		valx = (((-1/6)*x)+(19/6))
	if (x > 19):
		valx = 0
	return valx
	
def aguaMuyalta(x):
	if (x < 14):
		valx = 0
	if (14 <= x <= 20):
		valx = (((1/6)*x)-(14/6))
	if (x > 20):
		valx = 1
	return valx
	
def totalmenteTapada(x):
	if(x < 10):
		valx = 1
	if (10 <= x <= 30):
		valx = (((-1/20)*x)+(3/2))
	if (x > 30):
		valx = 0
	return valx
	
def tapaModerada(x):
	if (x < 20):
		valx = 0
	if (20 <= x <= 40):
		valx = (((1/20)*x)-(1))
	if (40 <= x <= 70):
		valx = (((-1/30)*x)+(7/3))
	if (x > 70):
		valx = 0
	return valx
	
def totalmenteDestapada(x):
	if (x < 60):
		valx = 0
	if (60 <= x <= 90):
		valx = (((1/30)*x)-(2))
	if (x > 90):
		valx = 1
	return valx
