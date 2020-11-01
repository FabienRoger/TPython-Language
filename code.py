def recherchedico(l,i=0,j=-1):
	l = []
	
	if j == -1:j = len(l)-1
	if abs(i-j) == 0:
		return i
	if l[i] > x or l[j] < x:
		return -1
	k = (i+j)//2
	l.append(recherchedico(i,k))
	l.append(recherchedico(k,j))
	f,s = l
	return max(f,s) #un des deux vaut -1
