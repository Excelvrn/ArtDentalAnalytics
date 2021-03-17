#!/usr/bin/python3
####Del repeats, count repeats
# -*- coding: latin-1 -*-
import io, os, sys, string, text
def main(opfile):
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	#print("\t----------------")
	OpenedFile = open(opfile, 'r').read()
	OpenedFileStat = os.stat(opfile)

	with open(opfile, 'r') as myfile:
		data=myfile.readlines()
		
	example1 = text.PrintPositions3(OpenedFile, "\n")
	#print("PrintPositions (example)\t", len(example), ":\n",example, "\n")
	#FL = text.FindingList(example)
			######	Var 2
	#FL = text.FindingList2(example)
	#print("Example1:\t",example1)
	kkk=text.FindingList3(example1)

	##print("TFL output:\t", len(FL),":\n",FL, "\n")
	#text.Count(example, FL)
	#copy of text.Count function
	###
	###	text.Count2(example, FL)
	text.Count2(example1, kkk)
	###
	#print("PC:\n", text.precount(example, FL))

	#kk3 = ["asdf", "asdf1", "asdf2"]
	#kk33 = ["as", "asdf1", "asdf2"]
	#for i in range(0, len(kk3)):
	#	for ii in range(0, len(kk33)):
	#		if (kk3[i]==kk33[ii]):
	#			print("=\t", kk3[i], kk33[ii])
	#		else:
	#			print("!=:\t", kk3[i], kk33[ii])
	#OpenedFile.close()
	#text.getsymblist(example[0] , ";")
	pass
#обработка, удаление повторов
def main2(opfile):
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	
	OpenedFile = open(opfile, 'r').read()
	OpenedFileStat = os.stat(opfile)
	
	with open(opfile, 'r') as myfile:
		data=myfile.readlines()
	
	example1 = text.PrintPositions3(OpenedFile, "\n")
	
	kkk=text.FindingList3(example1)

	for i in range(0,len(kkk)):
		print(kkk[i])
	pass
#обработка, удаление повторов с возвратом
def mainret(opfile):	
	OpenedFile = open(opfile, 'r').read()
	OpenedFileStat = os.stat(opfile)
	with open(opfile, 'r') as myfile:
		data=myfile.readlines()
	example1 = text.PrintPositions3(OpenedFile, "\n")
	kkk=text.FindingList3(example1)
	#for i in range(0,len(kkk)):
	#	print(kkk[i])
	return kkk
#обработка
def mainret1(opfile):
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	OpenedFile = open(opfile, 'r').read()
	OpenedFileStat = os.stat(opfile)
	#with open(opfile, 'r') as myfile:
	#	data=myfile.readlines()
	example1 = text.PrintPositions4(OpenedFile, ["\n", "\t"])
	for i in range(len(example1)-1,0,-1):
		if (text.compare(example1[i], "Сче") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Общ") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Хир") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Орт") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Тер") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Пар") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Неопл") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Лабора") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Тест") == 1) :
			del example1[i]
		elif (text.compare(example1[i], "Импла") == 1) :
			del example1[i]
	for i in range(0, len(example1)):
		print(example1[i])
	return example1
#объединение двух файлов, удаление повторов
def unit(file1,file2):
	l1 = mainret1(file1)
	l2=mainret1(file2)
	nl=mainret(file1)
	nl+=mainret(file2)
	#print(len(nl))
	kkk = text.FindingList3(nl)
	#for i in range(0, len(kkk)):
		#print(i, kkk[i])
	#	print(kkk[i])
	text.Count4(l1, l2, kkk)
	pass
#обработка выдёргивание 1/2 с конца каждой строки с последующим формированием списка
def mainret2(opfile):
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	OpenedFile = open(opfile, 'r').read()
	OpenedFileStat = os.stat(opfile)
	#with open(opfile, 'r') as myfile:
	#	data=myfile.readlines()
	example1 = text.PrintPositions4(OpenedFile, "\n" )
	print("example1[0]:\n", example1[0])
	print("example1[1]:\n", example1[1])
	#print(example1)
	menuni = text.FindingList3(example1[0])
	womenuni = text.FindingList3(example1[1])
	mf = text.FindingList3(example1[1])
	#print(text.Count4(example1[0], example1[1], mf))
	#for i in range(0, len(menuni)):
	#	print(menuni[i])
	return [menuni, womenuni]#обработка выдёргивание 1/2 с конца каждой строки с последующим формированием списка
def mainret3(opfile):
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	OpenedFile = open(opfile, 'r').read()
	OpenedFileStat = os.stat(opfile)
	#with open(opfile, 'r') as myfile:
	#	data=myfile.readlines()
	example1 = text.PrintPositions4(OpenedFile, "\n" )
	ex0 = example1[0]
	ex1 = example1[1]
	for i in range(0, len(ex0)):
		print(ex0[i])
	for i in range(0, len(ex1)):
		print(ex1[i])
	pass
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	OpenedFile = open(opfile, 'r').read()
	OpenedFileStat = os.stat(opfile)
	#with open(opfile, 'r') as myfile:
	#	data=myfile.readlines()
	example1 = text.PrintPositions4(OpenedFile, "\n" )
	print("example1[0]:\n", example1[0])
	print("example1[1]:\n", example1[1])
	#print(example1)
	menuni = text.FindingList3(example1[0])
	womenuni = text.FindingList3(example1[1])
	mf = text.FindingList3(example1[1])
	#print(text.Count4(example1[0], example1[1], mf))
	#for i in range(0, len(menuni)):
	#	print(menuni[i])
	return [menuni, womenuni]#обработка выдёргивание 1/2 с конца каждой строки с последующим формированием списка
def moreless(opfile):
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	OpenedFile = open(opfile, 'r').read()
	OpenedFileStat = os.stat(opfile)
	#with open(opfile, 'r') as myfile:
	#	data=myfile.readlines()
	#example1 = text.PrintPositions4(OpenedFile, "><" )
	#ex0 = example1[0]
	#ex1 = example1[1]
	#for i in range(0, len(ex0)):
	#	print(ex0[i])
	#for i in range(0, len(ex1)):
	#	print(ex1[i])
	text.TextSymbs(OpenedFile, "><")
def cuthtml(opfile, newname):
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	OpenedFile = open(opfile, 'r').read()
	NewFile = open(newname, 'w')
	#print(type(OpenedFile.split(sep=["<",">"])))
	dirname = opfile.find(".")
	print(os.getcwd())
	if (dirname>0):
		 dirname=opfile[0:dirname]
	else:
		dirname = opfile
		dirname+=".dir"
	#dirname = os.getcwd() +"/" + dirname
	
	#os.mkdir("dir000")
	print(dirname)
	#print( os.getcwd())
	#for i in range(0, 30):
	#	print(i, OpenedFile[i])
	#text.findtag(OpenedFile, "html")
	#text.findtag(OpenedFile, "head")
	#text.findtag(OpenedFile, "body")
	#text.getbasictags(OpenedFile)
	#k = text.getfindtag(OpenedFile, "head")
	#k = text.getfindtag(OpenedFile, "body")
	#print(k[0][0], k[1][0])
	#print(OpenedFile[k[0]: k[1]])
	
	#text.getstings1(OpenedFile)
	#k = text.getbetags(OpenedFile, "body")
	#print(OpenedFile[106979:(len(OpenedFile)-1)])
	print(text.getbetags(OpenedFile, NewFile))

	pass
def namehtml(opfile):
	print(opfile)
	print(os.path.dirname(opfile))
	print(os.path.split(opfile))
	name = os.path.split(opfile)[0]+"/0."+os.path.split(opfile)[1] 
	print(name)
	#like cuthtml(opfile, newname)
	cuthtml(opfile, name)
	pass
def start():
	#print(sys.argv)
	#print(sys.argv[1])
	#0 - название настоящего файла "EFv3.py"
	#print(sys.agrv[1])
	#	EFv3.py compare file1 file2
	#	   0       1      2     3
	if (sys.argv[1] == "count") and (len(sys.argv)==3):
		main(sys.argv[2])
	elif (sys.argv[1] == "file") and (len(sys.argv)==3):
		main2(sys.argv[2])
	elif (sys.argv[1] == "compare") and (len(sys.argv)==4):
		unit(sys.argv[2], sys.argv[3])
	elif (sys.argv[1] == "mainret") and (len(sys.argv)==3):
		mainret1(sys.argv[2])
	elif (sys.argv[1] == "back") and (len(sys.argv)==3):
		mainret2(sys.argv[2])
	elif (sys.argv[1] == "back1") and (len(sys.argv)==3):
		mainret3(sys.argv[2])
	#elif (sys.argv[1] == "moreless") and (len(sys.argv)==3):
	elif (sys.argv[1] == "moreless"):
		moreless(sys.argv[2])
	#
	elif (sys.argv[1] == "cuthtml"):
		cuthtml(sys.argv[2], sys.argv[3])
	elif (sys.argv[1] == "namehtml"):
		namehtml(sys.argv[2])
	else:
		print("Insert params!")
	pass

start()

