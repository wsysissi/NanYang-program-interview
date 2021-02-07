class Matrix_P :
    def __init__ (self,hang,lie,color=None):
        self.hang = hang
        self.lie = lie
        self.color = color

class Color :
    def __init__(self,color_name,color_num):
        self.color_name = color_name
        self.color_num = color_num
       
def set_matrix(hang,lie):
    matrix = []
    for i in range(0,hang):
        hang_i = []
        for j in range(0,lie):
            point = Matrix_P(i,j)
            hang_i.append(point)
        matrix.append(hang_i)
    return matrix
    
def get_colors (color_list,color_num_list):
    colors = []
    for i in range(0,len(color_list)):
        color = Color(color_list[i],color_num_list[i])
        colors.append(color)
    return colors

def color_it (colors,matrix):
    hang_num = len(matrix)-1
    lie_num = len(matrix[0])-1
    p_hang = 0
    i = 0
    while True:
        p_lie = 0
        while p_lie <= lie_num:
            #print("i:%d"%(i))
            #print("colors[i]num:%d"%(colors[i].color_num))
            #print("p_hang:%d, p_lie:%d"%(p_hang,p_lie))
            if colors[i].color_num > 0 and matrix[p_hang][p_lie].color==None:
                if p_hang != 0 :
                    if matrix[p_hang-1][p_lie].color != colors[i].color_name:
                        matrix[p_hang][p_lie].color = colors[i].color_name
                        colors[i].color_num = colors[i].color_num - 1
                        if p_lie+2 <= lie_num:
                            p_lie = p_lie+2
                        else:
                            p_lie = 0
                            if p_hang < hang_num:
                                p_hang +=1
                            elif p_hang == hang_num:
                                p_hang = 0
                    else:
                        p_lie +=1
                        
                elif p_hang == 0:
                    matrix[p_hang][p_lie].color = colors[i].color_name
                    colors[i].color_num = colors[i].color_num - 1
                    if p_lie+2 <= lie_num:
                        p_lie = p_lie+2
                    else:
                        p_lie = 0
                        p_hang +=1
            elif colors[i].color_num > 0 and matrix[p_hang][p_lie].color!=None:
                p_lie +=1
                
            elif colors[i].color_num == 0 and matrix[p_hang][p_lie].color==None:
                i +=1
                matrix[p_hang][p_lie].color = colors[i].color_name
                colors[i].color_num = colors[i].color_num - 1
                if p_lie+2 <= lie_num:
                    p_lie = p_lie+2
                else:
                    if p_hang < hang_num:
                        p_hang +=1
                    elif p_hang == hang_num:
                        p_lie = 0
                        p_hang = 0
            elif colors[i].color_num == 0 and matrix[p_hang][p_lie].color!=None:
                if i==len(colors)-1 :
                    break
                i +=1
                if p_lie < lie_num:
                    p_lie +=1
                elif p_lie == lie_num:
                    p_lie = 0
                    if p_hang < hang_num:
                        p_hang +=1
                    elif p_hang == hang_num:
                        p_hang = 0
        if colors[len(colors)-1].color_num == 0:
            break
        else:
            
            if p_hang < hang_num:
                p_hang +=1
            elif p_hang == hang_num:
                p_hang = 0
    return matrix
   
outf = open("output_question_5_1.txt","a")
matrix = set_matrix(5,5)
colors = get_colors(["B","R"],[13,12])
hang_num = len(matrix)
lie_num = len(matrix[0])
matrix = color_it(colors,matrix)
for i in matrix:
    for j in i:
        outf.write(j.color + "")
    outf.write("\n")
outf.close()
                
outf = open("output_question_5_2.txt","a")
matrix = set_matrix(64,64)
colors = get_colors(["B","W","G","Y","R"],[1451,1072,977,457,139])
hang_num = len(matrix)
lie_num = len(matrix[0])
matrix = color_it(colors,matrix)
for i in matrix:
    for j in i:
        outf.write(j.color + "")
    outf.write("\n")
outf.close()
