from matplolib.pyplot as plt

def get_points(file):
    in_file = open(file,"r")
    lines = in_file.readlines()
    points = []
    #获取点列表[["x1","y1"],["x2","y2"],,,,["xn","yn"]]
    for line in lines:
        line = line.strip("\n")
        point = line.split(" ")
        points.append(point)
    #把点坐标都转换为int
    for p in points:
        p[0] = int(p[0])
        p[1] = int(p[1])
    return points

def get_lim(poly_p):
    lft_lim = 100000
    top_lim = 0
    rt_lim = 0
    btm_lim = 100000
    for p in poly_p:
        if p[0] < lft_lim:
            lft_lim = p[0]
        if p[0] > rt_lim:
            rt_lim = p[0]
        if p[1] < btm_lim:
            btm_lim = p[0]
        if p[1] > top_lim:
            top_lim = p[1]
    return (top_lim,btm_lim,lft_lim,rt_lim)
    
def first_judge(p,lims):#p是点[x,y]，lims是边界[上，下，左，右]
    p_x = p[0]
    p_y = p[1]
    if lims[2]<=p_x<=lims[3] and lims[1]<=p_y<=lims[0]:#如果在边界内部，跳过
        return False
    else:#如果不在边界内直接输出，outside
        return True

def judge(p,poly_p):
    



outf = open("output_question_6.txt","a")

#获取待判断点坐标列表test_p,多边形顶点坐标列表poly_p
test_p = get_points("input_question_6_points")
poly_p = get_points("input_question_6_polygon")
#获取多边形最大边界列表lims[上，下，左，右]
lims = get_lim(poly_p)
#初步判断点是否不在多边形内部
lenth = len(test_p)
for p in range(0,lenth)):
    point = test_p[p]
    if first_judge(point,lims)：
        outf.write(str(point[0])+" "+str(point[1])+" outside\n")
        del test_p[p]
#精细判断剩余点是否位于多边形内部

    
#画两顶点连线
for point in range(0,len(poly_points)):
    x = []
    if point <= len(poly_points)-1
    x.append()
