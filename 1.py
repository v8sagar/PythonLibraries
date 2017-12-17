class Hello():
	"""docstring for Hello"""
	greet = input("'Enter greet mesage'\n")
	
	def Hi(greet):
		if greet == 'hi':
			print("English")
			pass
		print(greet)
		print(str('hi'*4)*4 )
		
	Hi(greet)		