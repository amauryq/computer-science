# how yield works

# generate next square number
def nextSquare(): 
    i = 1; 
  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes
                # from this point      
  
for num in nextSquare(): 
    if num > 100: 
         break    
    print(num)