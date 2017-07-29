def even_function(a):
	if a % 2 == 0:
		return True
	else:
		return False
print filter (even_function, [1,2,3,4,5,6,7,8,9])
