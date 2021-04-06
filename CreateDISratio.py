#prompt = "Input number of iterations:"
#repeat = input(prompt)

xlo = 0.0
xhi = 1.0
xbins = 40
xstep = (xhi-xlo)/xbins
numbers = [round(xlo + (x + 1/2)* xstep,5) for x in range(0, xbins)]
#repeat = 45000
repeat = 92500
#repeat = 100000
for i in range(repeat):
	print(*numbers, sep = "\n")
