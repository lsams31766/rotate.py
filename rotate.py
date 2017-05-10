# coding: utf-8
SIZE = 4

L = []

def fill_list():
	for i in range(SIZE * SIZE):
		L.append(i)
		
def get_value(c,r):
	return L[r*SIZE + c]

def set_value(c,r,value):
	L[r*SIZE + c] = value

def rotate_pt(c,r):
	return SIZE-1-r,c

def print_point(c,r):
	print "(" + str(c) + "," + str(r) + ")",
	
def print_grid():
	for r in range(SIZE):
		for c in range(SIZE):
			print get_value(c,r),
		print ""
			
	
def print_change(c1,r1,c2,r2):
		print_point(c1,r1),
		print "->",
		print_point(c2,r2)
		print ""	

def rotate(offset_c, offset_r):
	save = get_value(offset_c, offset_r)
	c1 = offset_c
	r1 = offset_r
	c2 = c1
	r2 = r1
	for i in range(4):
		c1=c2
		r1=r2
		c2,r2 = rotate_pt(c1,r1)
		print_change(c1,r1,c2,r2)
		set_value(c1,r1,get_value(c2,r2))
		#rotate again
	set_value(c1, r1, save)

fill_list()
print_grid()

last = SIZE - 1
for row in range(SIZE/2):
	for col in range(last):
		rotate(col+row,row)
		print "-----"
	last -= 2
print_grid()




