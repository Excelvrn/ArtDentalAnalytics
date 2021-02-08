import io, os, sys, string, text
def main():
	#	how to use
	#	python3 EF.py file_name.txt > output_file_name.txt
	#print("\t----------------")
	#words = ["word"]
	#print(words)
	#words += "asdfasdf".split()
	#print(words)
	#words += "asdfasdf"
	#print(words)
	#
	#OpenedFile = open(sys.argv[1], os.O_RDWR)
	OpenedFile = open(sys.argv[1], 'r').read()
	OpenedFileStat = os.stat(sys.argv[1])
	#step = 0
	#position = 0
	###
	###
	###
	#OpenedFile = os.open("./copy.txt", os.O_RDWR)
	#print(len(sys.argv))
	#print(str(OpenedFile).find('\\n'))

	#print("print-1", *OpenedFile)

	##
	##

	with open(sys.argv[1], 'r') as myfile:
		data=myfile.readlines()
	#print("print-2\n", data)
	#print("print-3\n", len(data))
	#for x in range(0, len(data)):
		#print("print-4\n", data[x], "\n")
	#print("String\t", "print-5\n", data[10:15], "\n")
	#position = 
	#print("step-", step, data[1].find(";"))

	##
	##

	#print(OpenedFileStat.st_size)
	#print("OpenedFile \t", OpenedFile)
	#FindResult = str(OpenedFile).find('.', 0)
	#print(FindResult)
	#step+=1
	#print("step\t", step," \n", OpenedFile)
	#position = OpenedFile.find(";")
	#print("Position\t", position)
	#position = OpenedFile.find(";", position+1)
	#print("Position\t", position)
	#position = text.NextPosition(OpenedFile, ";", position)[1]
	#print("Position\t", text.NextPosition(OpenedFile, ";", position))
	example = text.PrintPositions(OpenedFile, "; ")
	#print("PrintPositions (example)\t", len(example), ":\n",example, "\n")
	#FL = text.FindingList(example)
			######	Var 2
	FL = text.FindingList2(example)


	##print("TFL output:\t", len(FL),":\n",FL, "\n")
	#text.Count(example, FL)
	#copy of text.Count function
	text.Count2(example, FL)
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
main()
