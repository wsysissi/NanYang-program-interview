def coo_index (coo,lie,hang):
    x1=coo[0]
    x2=coo[1]
    i=x2*lie+x1
    return i
    
def index_coo(i,lie,hang):
    x1 = i%lie
    x2 = i//lie
    return ([str(x1),str(x2)])

def write_coo_index(inf,outf,lie,hang):
    inf = open(inf,"r")
    outf = open(outf,"a")
    outf.write("index\n")
    lines = inf.readlines()
    for i in range(1,len(lines)):
        line = lines[i]
        line = line.strip("\n")
        coo = line.split("\t")
        if len(coo) > 0:
            for i in coo:
                i=int(coo.pop(0))
                coo.append(i)
            index = coo_index(coo,lie,hang)
            outf.write(str(index)+"\n")

def write_index_coo(inf,outf,lie,hang):
    inf = open(inf,"r")
    outf = open(outf,"a")
    outf.write("x1\tx2\n")
    lines = inf.readlines()
    for i in range(1,len(lines)):
        line = lines[i]
        line = line.strip("\n")
        if len(line) > 0:
            line = int(line)
            coo = index_coo(line,lie,hang)
            outf.write(coo[0]+"\t"+coo[1]+"\n")
    
write_coo_index("input_coordinates_7_1.txt","output_index_7_1.txt",50,57)
#write_coo_index("intest.txt","outtest.txt",4,3)
write_index_coo("input_index_7_1.txt","output_coordinates_7_1.txt",50,57)
#write_index_coo("outtest.txt","2outtest.txt",4,3)



