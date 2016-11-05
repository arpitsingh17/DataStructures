# Binary Search
# Input list must be sorted in this search method. 

def bin(alist,item):
    aalist = alist
    midterm = alist[(len(alist)//2)]
    found = False
    
    while True:
    	try:
		    if item < midterm:
		        #print (alist[:((alist.index(midterm)))])

		        return(bin(alist[:((alist.index(midterm)))],item))
		        


		    elif item > midterm:
				#print(alist.index(midterm))
		        return(bin(alist[(alist.index(midterm)+1):],item))
		        #print alist[(alist.index(midterm)+1):]
		    elif item==midterm:
		    	return("Found")
		    	break
        except:
	    	return "Not Found"
	    
	        
	        
	 
          
      

print (bin([1,2,3,4,5],42))
