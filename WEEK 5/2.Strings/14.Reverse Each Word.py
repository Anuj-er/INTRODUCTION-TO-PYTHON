def reverseEachWord(string) :
	w = string.split(" ")        
                           
	nw= [i[::-1] for i in w]
                          
	ns = " ".join(nw)
	return ns