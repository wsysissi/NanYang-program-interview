#matrix_f = open("input_question_4","r")
class Matrix_Site:
	def __init__ (self,val,label=None):
		self.val = val
		self.label = label
matrix_f = open("test.txt","r")
lines = matrix_f.readlines()
matrix = []
for line in lines:
	line = line.strip("\n")
	nums = line.split("\t")
	sites = []
	for i in nums :
		matrix_site = Matrix_Site(int(i))
		sites.append(matrix_site)
	matrix.append(sites)
print(matrix)
