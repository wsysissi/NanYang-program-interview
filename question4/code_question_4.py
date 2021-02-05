
class Matrix_Site:
	def __init__ (self,val,label=0):
		self.val = val
		self.label = label
matrix_f = open("input_question_4","r")
#matrix_f = open("test.txt","r")
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
#print(matrix)
total_label = 0
for hang in range(0,len(matrix)):
    for lie in range(0,len(matrix[hang])):
        if matrix[hang][lie].val == 1 and matrix[hang][lie].label == 0:
            total_label +=1
            matrix[hang][lie].label = total_label
            x = hang
            y = lie
            queue = [[x,y]]
            while len(queue) != 0:
                now_site = queue.pop()
                now_x = now_site[0]
                now_y = now_site[1]
                #print(now_x,now_y)
                if matrix[now_x-1][now_y].val == 1 and now_x-1>-1:#上
                    if matrix[now_x-1][now_y].label == 0:
                        matrix[now_x-1][now_y].label = matrix[now_x][now_y].label
                        queue.append([now_x-1,now_y])
                        #print("shang")
                if now_x+1<len(matrix):#下
                    if matrix[now_x+1][now_y].val == 1 and matrix[now_x+1][now_y].label == 0:
                        matrix[now_x+1][now_y].label = matrix[now_x][now_y].label
                        queue.append([now_x+1,now_y])
                        #print("xia")
                if matrix[now_x][now_y-1].val == 1 and now_y-1>-1:#左
                    if matrix[now_x][now_y-1].label == 0:
                        matrix[now_x][now_y-1].label = matrix[now_x][now_y].label
                        queue.append([now_x,now_y-1])
                        #print("zuo")
                if now_y+1<len(matrix[0]):
                    if matrix[now_x][now_y+1].val == 1 and matrix[now_x][now_y+1].label == 0: #右
                        matrix[now_x][now_y+1].label = matrix[now_x][now_y].label
                        queue.append([now_x,now_y+1])
                        #print("you")
matrix_f.close()

outf = open("output_question_4.txt","a")
#outf = open("output_test.txt","a")
for hang in range(0,len(matrix)):
    for lie in range(0,len(matrix[hang])):
        if lie < len(matrix[0])-1:
            outf.write(str(matrix[hang][lie].label)+" ")
        elif lie == len(matrix[0])-1:
            outf.write(str(matrix[hang][lie].label)+"\n")
outf.close()
print(total_label)
                
                
                
