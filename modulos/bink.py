from modulos.bin import check_bin
from random import randint
def nib():
	a=randint(0,50)
	b=randint(0,50)
	c=randint(0,50)
	d=randint(0,50)
	e=randint(0,50)
	f=randint(0,50)
	val = check_bin(f"{a}{b}{c}{d}{e}{f}")
	if val !="❌ BIN INVALIDO ❌":
		msg = val
	while val == "❌ BIN INVALIDO ❌":
		a=randint(0,50)
		b=randint(0,50)
		c=randint(0,50)
		d=randint(0,50)
		e=randint(0,50)
		f=randint(0,50)
		val = check_bin(f"{a}{b}{c}{d}{e}{f}")
		if val !="❌ BIN INVALIDO ❌":
			msg = val
			break
		else:
			pass
	return msg