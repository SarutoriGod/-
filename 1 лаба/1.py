a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
f = int(input('f: '))
if a == 0:
	print('На ноль делить нельзя, переменная a не может равняться нулю')
else:
	print(abs(a - b * c * d**3 + (c**5 - a**2) / a + f**3 * (a -213))) 