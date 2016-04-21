from math import pi
print "--------Shape Area Calculator---------\nCIRCLE - RECTANGLE - TRIANGLE - SQUARE"

def multiplier(count,side,oside):
	return float(side) if float(count)==1 else multiplier(float(count)-1,float(side)+float(oside),float(oside))

def rectangle():
	print "Enter Dimensions for Rectangle" 
	width,length  =(raw_input("Enter Width: ")), (raw_input("Enter Length: "))
	if width.isdigit() and length.isdigit():
		r= multiplier(width,length,length)
		print r
		return r
	else:
		print "Please enter a number"
		rectangle()
def square():		
	print "Enter Dimensions for square" 
	side = (raw_input("Enter side: "))
	if side.isdigit():
		s= multiplier(side,side,side)
		print s
		return s
	else:
		print "Please enter a number"
		square()
def triangle():
	print "Enter Dimensions for Triangle" 
	base, height= raw_input("Enter Base: "),raw_input("Enter Height: ")
	if base.isdigit() and height.isdigit():
		t= multiplier(multiplier(base,height,height),0.5,0.5)
		print t
		return t
	else:
		print "Please enter a number"
		triangle()
def circle():
	print "Enter Dimensions for Circle" 
	rad = (raw_input("Enter radius: "))
	if rad.isdigit():	
		c= multiplier(multiplier(rad,rad,rad),pi,pi)
		print	c
		return c
	else:
		print "Please enter a number"
		circle()


s= square()
c= circle()
r= rectangle()
t= triangle()

maxx = max(float(r),float(s),float(c),float(t))
guess = raw_input("Enter guess SHAPE: ")
	
		
def guessy(corAns,guess):
	if corAns == guess.lower():
		print "Correct!!!"			
	else:
		print "Try Again!"
		guess = raw_input("Enter guess SHAPE: ")
		print ("Correct!!!" if corAns == guess.lower() else "game over")
def dictionary(maxx,t,c,r,s,guess):
	if  maxx == t:
		corAns = "triangle"
		guessy(corAns,guess)
	elif maxx == r: 
		corAns = "rectangle"
		guessy(corAns,guess)
	elif maxx == c:
		corAns = "circle"
		guessy(corAns,guess)
	elif maxx == s:
		corAns = "square"
		guessy(corAns,guess)













