#prompt = "Input number of iterations:"
#repeat = input(prompt)

xlo = 0.0
xhi = 1.25
xbins = 50
xstep = (xhi-xlo)/xbins
numbers = [round(xlo + (x + 1/2)* xstep,5) for x in range(0, xbins)]
# Carbon (89303)
# Iron (94260)
# Lead (45515)
repeat = 45515
#repeat = 100000
for i in range(repeat):
	print(*numbers, sep = "\n")
