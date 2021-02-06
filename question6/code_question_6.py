#REFERENCE:https://www.jianshu.com/p/ba03c600a557

import matplotlib.pyplot as plt

def draw (test_p,poly_p):
    start_p = poly_p[0]
    for i in range(1,len(poly_p)):
        end_p = poly_p[i]
        plt.plot([start_p[0],end_p[0]],[start_p[1],end_p[1]],color="r")
        plt.scatter([start_p[0],end_p[0]],[start_p[1],end_p[1]],color="b")
        start_p = end_p
    end_p = poly_p[0]
    plt.plot([start_p[0],end_p[0]],[start_p[1],end_p[1]],color="r")
    
    for i in range(0,len(test_p)):
        p = test_p[i]
        plt.scatter(p[0],p[1],color="b")
    plt.show()

def get_points(file):
    in_file = open(file,"r")
    lines = in_file.readlines()
    points = []
    #获取点列表[["x1","y1"],["x2","y2"],,,,["xn","yn"]]
    for line in lines:
        line = line.strip("\n")
        point = line.split(" ")
        if len(point)==2:
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
        print(p[0],p[1])
        if p[0] < lft_lim:
            lft_lim = p[0]
            print("l",lft_lim)
        if p[0] > rt_lim:
            rt_lim = p[0]
            print("r",rt_lim)
        if p[1] < btm_lim:
            btm_lim = p[1]
            print("b",btm_lim)
        if p[1] > top_lim:
            top_lim = p[1]
            print("t",top_lim)
    return ([top_lim,btm_lim,lft_lim,rt_lim])
    
def first_judge(p,lims):#p是点[x,y]，lims是边界[上，下，左，右]
    p_x = p[0]
    p_y = p[1]
    if lims[2]<=p_x<=lims[3] and lims[1]<=p_y<=lims[0]:#如果在边界内部，跳过
        return False
    else:#如果不在边界内直接输出，outside
        return True

def judge_intersect(p,start_p,end_p,poly_p,end_i):
    x = p[0]
    y = p[1]
    x1 = start_p[0]
    y1 = start_p[1]
    x2 = end_p[0]
    y2 = end_p[1]
    big_xp = start_p if x1>x2 else end_p
    small_xp = start_p if x1<x2 else end_p
    if end_i+1 <= len(poly_p)-1:
        next_y = poly_p[end_i+1][1]
    elif end_i == len(poly_p)-1:#最后一个点
        next_y = poly_p[0][1]
    elif end_i == 0:
        next_y = poly_p[1][1]
        pre_y = poly_p[len(poly_p)-2][1]
    if end_i-2 >= 0:
        pre_y = poly_p[end_i-2][1]
    elif end_i == 1:
        pre_y = poly_p[len(poly_p)-1][1]
    #平行且不重合。即，是一条平行于坐标轴的边
    if y1 == y2 and y != y1:
        print("1")
        return False
    #平行且重合
    if y1 == y2 and y == y1 and small_xp[0]>x:
        if (next_y-y)*(pre_y-y) < 0:
            print("2")
            return True
        elif (next_y-y)*(pre_y-y) > 0:
            print("3")
            return False
    #垂直
    if x1 == x2 and x1 != x:
        if (y1-y)*(y2-y)<0 :
            print("4")
            return True
        else:
            print("5")
            return False
    #前一个端点在射线上，记为不相交。
    if (x1>x and y1==y and y2!=y):
        print("6")
        return False
    #后一个端点在射线上，判断下一端点和前一段点y值与当前y值相比，大小关系是否相同。
    if x2>x and y2==y and y1!=y :
        if (next_y-y)*(y1-y)<0:
            print("7")
            return True
        elif (next_y-y)*(y1-y)>0:
            print("8")
            return False
    #起始点均在射线上方，不相交。即，y1，y2都大于y
    if y1>=y and y2>=y :
        print("9")
        return False
    #起始点均在下方，不相交。
    if y1<=y and y2<=y :
        print("10")
        return False
    #起始点均在左边，不相交。即，x1,x2都小于x
    if big_xp[0]<=x :
        print("11")
        return False
    
    #边的两个端点一个在点左边，一个在点的右边。
    big_xp = start_p if x1>x2 else end_p
    small_xp = start_p if x1<x2 else end_p
    if ((big_xp[0]>x and small_xp[0]<x) and ((y1-y)*(y2-y)<0)): 
        ex = (abs(big_xp[1]-y)*(big_xp[0]-small_xp[0]))/(abs(big_xp[1]-small_xp[1]))
        if (big_xp[0]-x)<ex:
            print("12")
            return False
        else:
            print("13")
            return True
    #(y1-y)*(y2-y)=0
    if big_xp[0]>x and small_xp[0]<x and (y1-y)*(y2-y)==0:
        print("14")
        return False
    return True
    
    
def judge_on(p,start_p,end_p):
    x = p[0]
    y = p[1]
    x1 = start_p[0]
    y1 = start_p[1]
    x2 = end_p[0]
    y2 = end_p[1]
    #边垂直于坐标轴
    if x1 == x2 :
        if x == x1 and ((y1-y)*(y2-y)<=0):
            return True
        else :
            return False
    #边平行于坐标轴
    if y1 == y2 :
        if y == y1 and ((x1-x)*(x2-x)<=0):
            return True
        else:
            return False
    #边是斜线
    k = (y2-y1)/(x2-x1)
    b = y1-((x1*(y2-y1))/(x2-x1))
    if y == k*x+b and ((x1-x)*(x2-x)<=0):
        return True
    return False


def judge_in(p,poly_p):
    start_p = poly_p[0]
    chuanguo_sum = 0
    for i in range(1,len(poly_p)):
        end_p = poly_p[i]
        #如果在这条边上，返回in
        if judge_on(p,start_p,end_p):
            return True
        #如果不在边上，就判断穿过关系
        if judge_intersect(p,start_p,end_p,poly_p,i):#如果穿过某条边，穿过计数器+1
            chuanguo_sum += 1
        start_p = end_p
    end_p = poly_p[0]
    if judge_intersect(p,start_p,end_p,poly_p,0):#如果穿过最后一条边，穿过计数器+1
        chuanguo_sum += 1
    if chuanguo_sum%2 == 0:
        return False
    else:
        return True


outf = open("output_question_6.txt","a")

#获取待判断点坐标列表test_p,多边形顶点坐标列表poly_p
test_p = get_points("input_question_6_points")
poly_p = get_points("input_question_6_polygon")

#draw(test_p,poly_p)

#获取多边形最大边界列表lims[上，下，左，右]
lims = get_lim(poly_p)
#print(lims)
#初步判断点是否不在多边形内部
lenth = len(test_p)
del_list = []
for p in range(0,lenth):
    point = test_p[p]
    if first_judge(point,lims):
        outf.write(str(point[0])+" "+str(point[1])+" outside\n")
        del_list.append(p)
print(del_list)
print(test_p)
for i in del_list:
    del test_p[i]
#精细判断剩余点是否位于多边形内部
lenth = len(test_p)
for p in range(0,lenth):
    print(test_p[p])
    point = test_p[p]
    k = judge_in(point,poly_p)
    if k == True:
        outf.write(str(point[0])+" "+str(point[1])+" inside\n")
    elif not judge_in(point,poly_p):
        outf.write(str(point[0])+" "+str(point[1])+" outside\n")

outf.close()
    
