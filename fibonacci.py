
def fibo(n):
	
  	a = 0
 	 b = 1
  
  	for K in range(n):
    		c = a+b
    		a = b
    		b = c
    
   return b
   
   for x in range(10):
      
	pass

def fibo_rec(n):
	if n < 2:
		return n
	return fibo_rec(n-1)+ fibo_rec(n-2) 
	for x in range(10):
		
	pass
	

print(fibo(10))
print(fibo_rec(10))
	
