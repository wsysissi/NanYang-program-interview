#matrix_f = open("input_question_4","r")
matrix_f = open("test.txt","r")
lines = matrix_f.readlines()
matrix = []
for line in lines:
    line = line.strip("\n")
    nums = line.split("\t")
	for i in nums :
	
    matrix.append(nums)

