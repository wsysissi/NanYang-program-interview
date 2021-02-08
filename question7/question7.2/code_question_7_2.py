def get_i (index,D,L,d):#D为维数,L是list（L1，L2,,,,LD）,d最开始的输入值=1
    if d == D-1:#iD=index
        pi_L =1
        for i in range(0,d):#L的前D-1个
            pi_L = pi_L * L[i]
            #print("0:",pi_L)
        i_d = index%pi_L
        i_d_list = [i_d]
        #print("1:",i_d,i_d_list)
        return ([i_d,i_d_list])
        
    pi_L=1
    for i in range(0,d):
        pi_L = pi_L * L[i]
    if d == 1 :
        pi_L = L[0]
    k = get_i(index,D,L,d+1)
    #print("id_1:%d, piL:%d"%(k[0],pi_L))
    i_d = k[0]%pi_L
    i_d_list = k[1]+[i_d]
    #print("2:",i_d,i_d_list)
    return ([i_d,i_d_list])
#i_d_list在用之前要先反向，再append index。


def index_coo (index,D,L):#D为维数,L是list（L1，L2,,,,LD）
    x_list =[]
    k = get_i(index,D,L,1)
    k[1].reverse()
    k[1].append(index)
    i_list = k[1]
    x0 = i_list[0]
    x_list.append(x0)
    for d in range(1,D):
        pi_L = 1
        for i in range(0,d):
            pi_L = pi_L*L[i]
        x_d = (i_list[d]-i_list[d-1])/pi_L
        x_list.append(int(x_d))
    return x_list
    
def coo_index (x_list,D,L):
    index = x_list[0]
    for d in range(1,D):
        pi_L = 1
        for i in range(0,d):
            pi_L = pi_L*L[i]
        index = x_list[d] * pi_L + index
    return index
    
def write_coo_index(inf,outf,L):
    inf = open(inf,"r")
    outf = open (outf,"a")
    lines = inf.readlines()
    D = len(lines[0].strip("\n").split("\t"))
    outf.write("index\n")
    for i in range(1,len(lines)):
        line = lines[i].strip("\n")
        coo = line.split("\t")
        coo_out = []
        if len(coo)==D:
            #print(len(coo))
            for xi in coo:
                k = int(xi)
                coo_out.append(k)
            index = coo_index(coo_out,D,L)
            outf.write(str(index)+"\n")
    inf.close()
    outf.close()
            
            
def write_index_coo(inf,outf,D,L):
    inf = open(inf,"r")
    outf = open (outf,"a")
    lines = inf.readlines()
    out_line0 =""
    for i in range(D):
        out_line0 = out_line0 + "x" + str(i+1) +"\t"
    outf.write(out_line0+"\n")
    for i in range(1,len(lines)):
        #print("第%d个"%i)
        line = lines[i]
        index = line.strip("\n")
        if index != "":
            out_index = int(index)
            coo = index_coo(out_index,D,L)
            for xi in coo:
                outf.write(str(xi)+"\t")
        outf.write("\n")
    inf.close()
    outf.close()
    
write_coo_index("input_coordinates_7_2.txt","output_index_7_2.txt",[4,8,5,9,6,7])
#write_coo_index("intest.txt","outtest.txt",[4,3])
write_index_coo("input_index_7_2.txt","output_coordinates_7_2.txt",6,[4,8,5,9,6,7])
#write_index_coo("outtest.txt","2outtest.txt",3,[4,3,2])
