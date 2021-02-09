#Разделение на слова
#	return [начальная позиция, КонечнаяПозиция]
#	КонечнаяПозиция: -1 - конец файла/последовательности
def NextPosition(string, symb, startposition):
	#print(string[startposition:(len(string)-1)])
	#OpenedFile.find(";", position+1)
	if (startposition>0):
			startposition+=1
	if (startposition < len(string)):
		k = string.find(symb, startposition)
	else:
		k = -1
		startposition = -1
	return [startposition, k]

#Разделение на слова строки string, исключая список символов lsymb, 
#с начальной позиции startposition
def NextPositionList(string, lsymb, startposition):
	#print(string[startposition:(len(string)-1)])
	#OpenedFile.find(";", position+1)
	pos=[]
	if (startposition>0):
			startposition+=1
	if (startposition < len(string)):
		if len(lsymb)>1:
			for isymb in range(0, len(lsymb)):
				pos+= [string.find(lsymb[isymb], startposition)]
			pos =[min(pos)]
		else:
			pos+= string.find(lsymb[1], startposition)
		#k = string.find(symb, startposition)
	else:
		pos=[-1]
	return [startposition, pos]

def getsymblist(string1, symb):
	pos = [0]
	for i in range(0, len(string1)):
		if (string1[i]==symb):
			pos+=[i]
		#pos+=[i]
	#print("Positions:\t", pos)
	return pos

#Формирование листа
def PrintPositions(string, symb):
	position = 0
	newposition=0
	StringLength = len(string)
	text = []
	lpos=[]
#	print(StringLength)
	while (position!=-1):
			#newposition = NextPosition(string, symb, position)[1]
			newposition = NextPosition(string, symb, position)[1]
			if newposition>0:
				text+= string[position:newposition].split()
				#text+= string[position:newposition]
				lpos+= [newposition]
				#print(text)
			position = newposition
	#print("len(string) is\t", len(string), "\nlpos:\t",len(lpos),lpos,"\ntext:\n",len(text), text)
			#print(text)
	#print(text, len(text))
	#print(text)
	position = len(text)-1
	while (position > (-1)):
##		print(text[position])
		if (symb==text[position]):
			text.pop(position)
		position-=1
	#print("Text`s length:\t", len(text))
	#for i in range(0, len(text)):
		#if (symb==text[i]):
			#print("symb`s position is\t", i)
	#print("M1\nlen(string) is\t", len(string), "\nlpos:\t",len(lpos),lpos,"\ntext:\n",len(text), text)
	#print("PrintPositions:\t",text)
	return text

#Формирование листа. v.2
def PrintPositions2(string, symb):
	#print(len(symb))
	getsymblist(string, symb)
	position = 0
	newposition=0
	StringLength = len(string)
	text = []
	lpos=[]
#	print(StringLength)
	while (position!=-1):
			#newposition = NextPosition(string, symb, position)[1]
			newposition = NextPosition(string, symb, position)[1]
			if newposition>0:
				text+= string[position:newposition].split()
				#text+= string[position:newposition]
				lpos+= [newposition]
				#print(text)
			position = newposition
	#print("len(string) is\t", len(string), "\nlpos:\t",len(lpos),lpos,"\ntext:\n",len(text), text)
			#print(text)
	#print(text, len(text))
	#print(text)
	position = len(text)-1
	while (position > (-1)):
##		print(text[position])
		if (symb==text[position]):
			text.pop(position)
		position-=1
	#print("Text`s length:\t", len(text))
	#for i in range(0, len(text)):
		#if (symb==text[i]):
			#print("symb`s position is\t", i)
	#print("M1\nlen(string) is\t", len(string), "\nlpos:\t",len(lpos),lpos,"\ntext:\n",len(text), text)
	#print("PrintPositions:\t",text)
	return text
#Формирование листа. v.3
def PrintPositions3(string,symb):
	#print("PrintPositions3:\n")
	nlist = []
	startpos = 0
	pos = getsymblist(string, symb)
	#print("Pos is\t", pos)
	step1 = 0
	for i in range(0, len(pos)):
		if (i<(len(pos)-2)):
			nlist += [string[startpos:(pos[i+1])]]
			startpos = pos[i+1]+1
	#print("1. nlist is:\t")
	#for i in range(0, len(nlist)):
	#	print(nlist[i])
	#print("Nlist length is:\t",len(nlist))
	return nlist
#Формирование листа. v.4
def PrintPositions4(string,lsymb):
	chastr = PrintPositions3(string, "\n")
	startpos = 100
	prevstartpos = 100
	#print(chastr[0])
	#print(len(chastr[0]))
	men=[]
	women=[]
	for i in range(0, len(chastr)):
		a = len(chastr[i])-1
		if (i == 0):
			if (chastr[i][a] == "2"):
				startpos = 2
				prevstartpos = 2
			else:
				startpos = 1
				prevstartpos = 1
		if (len(chastr[i])>4):
			if (chastr[i][a] == "1"):
				startpos = 1
			else:
				startpos = 2
			if (startpos != prevstartpos):
				#print(i, ":\t", prevstartpos, startpos)
				prevstartpos = startpos
			if (startpos == 1):
				women+=[chastr[i]]
			elif (startpos == 2):
				men+=[chastr[i]]
		#for i in range(0, len(men)):
			#print(men[i])
			#print(kkk[i])
	ret = []
	ret +=[men]
	ret+=[women]
	print(women)
	return ret

#Формирование листа с удалением повторяющихся элементов
def FindingList(Flist):
	flag = 0
	k=[]
	#k+=Flist[0].split()
	#print(k)
	#print("Flist len:\t",len(Flist))
	if (len(Flist)>1):
		k+=Flist[0].split()
		for x in range(0,len(Flist)):
			flag = 0
			#print("len(Flist):\t", len(Flist))
			#print("len(k):\t", len(k))
			#print(k)
			if (len(k)>1):
				for xx in range(0, len(k)):
					if (k[xx]==Flist[x]):
						flag = 1
						break
				if (flag == 0):
					k+=Flist[x].split()
			#elif (len(k) == 1):
				#if (k[0]!=Flist[x]):
					#k+=Flist[x].split()
			else:
				k+=Flist[x].split()
			#print("\t:",x, k)
	elif (len(Flist) ==1 ):
		k+=Flist[0].split()
		#print("\t\t\tK is alone")
	#else:
		#print("\t\t\tEmpty K")
#	while (pos1 < len(Flist)):
#		if (len(k)==1):
#		pass
	#print(k)
	#if (len(k)>1):
		#for x in range(0, len(k)):
			#print(k[x])
	#else:
		#print(k)
	#else:
		#pass
	return k
#the first copy of FindingList function
def FindingList2(Flist):
	#print("FindingList2\nFlist is\t", Flist)
	k=[]
	if (len(Flist)>0):
		k+=Flist[0].split()
		if (len(Flist)>1):
			for i in range(0, len(Flist)):
				flag = 0
				if (len(k)>1):
					for ii in range(0, len(k)):
						if (k[ii] == Flist[i]):
							flag=1
							break
					if (flag==0):
						k+=Flist[i].split()
				elif (len(k)==1):
					if (Flist[i]!=k[0]):
						k+=Flist[i].split()
	#print("\nk is\t",len(k), k)
		#if (len(Flist)>1):
			#for i in range(0, len(Flist)):
				
		#else:
			#k+=Flist[0].split()
	#else	:
	return k
#the first copy of FindingList function for strings in list v.3
def FindingList3(Flist):
	#print("FindingList3:")
	k=[]
	#print("len(Flist) is\t:", len(Flist))
	#for i in range(0, len(Flist)):
	#	print(i,":\t", Flist[i])
	for i in range(0, len(Flist)):
		if (len(k)==0)and (len(Flist)>0):
			#print("Add 1")
			k+=[Flist[i]]
		elif (len(Flist)>1) and (len(k)==1):
			if (Flist[i] != k[0]):
				#print("Add 2")
				k+=[Flist[i]]
				#print("NE:\t", k[0], Flist[i])
		elif (len(Flist)>1) and (len(k)>1):
			NEvar = 100
			NEVvar = 0
			for ii in range(0, len(k)):
				if (Flist[i] != k[ii]):
					NEVvar= NEVvar+1
			if (NEVvar==len(k)):
				#print("Add 3")
				k+=[Flist[i]]
		#for kl in range(0, len(k)):
		#	print(k[kl])
	#for i in range(0, len(k)):
		#print("NE:\t",i,":\t", k[i])
	#	print(i,":\t", k[i])
	return k
#compare 2 elements
#return 1 - equal
# -1 - not equ
def compare(string, found):
	comparev=[]
	comparevv=0
	if len(string)>len(found):
		for i in range(0, len(found)):
			if (string[i] == found[i]):
				comparev+=[1]
			else:
				comparev+=[0]
		for i in range(0,len(comparev)):
			comparevv+=comparev[i]
		if (comparevv == len(found)):
			comparevv = 1
		else:
			comparevv = -1
	return comparevv
#compare 2 elements from end
#return 1 - equal
# -1 - not equ
def CompareEnd(endstring, found):
	comparev=[]
	comparevv=0
	if len(endstring)>len(found):
		k=len(endstring)-1
		m = len(found)-1
		for i in range(0, len(found)):
			if (endstring[k-i] == found[m-i]):
				comparev+=[1]
			else:
				comparev+=[0]
		for i in range(0,len(comparev)):
			comparevv+=comparev[i]
		if (comparevv == len(found)):
			comparevv = 1
		else:
			comparevv = -1
	return comparevv

def precount(l1, l2):
	#length(l1>l2)!!!
	output=[]
	k=0
	for i in range(0, len(l1)):
			k = 0
			for ii in range(0, len(l2)):
				if (l1[i]==l2[ii]):
					k+=1
			output+=[l2[ii], k]
	if (len(output)>1):
		for i in range(0, len(output)):
			print(output[i])
			if (i%2==1):
				print("\n")
	return output
#Подсчётов появления каждого элемента
#["Название", "Количество раз"]
# list1 > list2
def Count(list1, list2):
	#print("L1:\t", list1)
	#print("L2:\t", list2)
	print("Name\tNumber")
#	print("List1\t", list1)
#	print("List2\t", list2)
	output = []
	if (len(list1)>len(list2)):
		output = precount(list1,list2)
	else:
		output = precount(list2,list1)
			#print(output[i])
			#print(list2[i],"\t", k)
	#print("L 1:\t",list1)
	#print("L 2:\t",list2)
	print("Output:\t",output)
	#print(len(output), output)
	#for i in range(0, len(output)):
		#print(output[i])
	pass

#list1>list2
def Count2(list1, list2):
	#print("\n\t--- Count2 function ---")
	#print("List1:\n", list1)
	#print("List2:\n", list2)
	output = []
	if (len(list1)>1) and (len(list2)>1):
		for I in range(0, len(list2)):
			count=0
			for II in range(0, len(list1)):
				if (list2[I] == list1[II]):
					count+=1
			output+=[[list2[I], count]]
	#print("Output:\n", output)
	if (len(output)>1):
		print("Name\tCount")
		for i in range(0, len(output)):
			print(output[i][0],"\t", output[i][1])
	pass
#list1>list2
#list2 is list with found elements
def Count3(list1, list2):
	#print("\n\t--- Count2 function ---")
	#print("List1:\n", list1)
	#print("List2:\n", list2)
	output = []
	if (len(list1)>1) and (len(list2)>1):
		for I in range(0, len(list2)):
			count=0
			for II in range(0, len(list1)):
				if (list2[I] == list1[II]):
					count+=1
			output+=[count]
	#print("Output:\n", output)
	return output
#list1,2 - file-list
#fl - found elements
def Count4(list1, list2, fl):
	l1 = Count3(list1, fl)
	#print(l1)
	l2 = Count3(list2, fl)
	#print(l2)
	for i in range(0, len(fl)):
		print(fl[i], l1[i], l2[i],sep="\t")
	pass
