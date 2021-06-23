#prompt = "Input number of iterations:"
#repeat = input(prompt)

#xlo = 0.0
#xhi = 1.0
#xbins = 40
xlo = -180.0
xhi = 180.0
xbins = 60
xstep = (xhi-xlo)/xbins
numbers = [round(xlo + (x + 1/2)* xstep,5) for x in range(0, xbins)]
# MR-1D
# Carbon (89303)
# Iron (94260)
# Lead (45515)
# MR-3D for C, Fe, Pb
# nu_1_q2_1_AC_CC_RC (89202	94302	46194)
# nu_1_q2_2_AC_CC_RC (89769	94348	45763)
# nu_1_q2_3_AC_CC_RC (84341	91306	43633)
# nu_2_q2_1_AC_CC_RC (90640	95789	47004)
# nu_2_q2_2_AC_CC_RC (89478	94110	45548)
# nu_2_q2_3_AC_CC_RC (86825	90240	42721)
# nu_3_q2_1_AC_CC_RC (91678	97372	47065)
# nu_3_q2_2_AC_CC_RC (91289	96913	46265)
# nu_3_q2_3_AC_CC_RC (89193	93260	43428)
#repeat = 89303
#repeat = 94260
repeat = 45515
#repeat = 100000
for i in range(repeat):
	print(*numbers, sep = "\n")
