#Since the value of each member in a row of the matrix given in the example is
#equal to the number of that row, the matrix generated in this code is also of this form,
#but can be replaced with other matrices in other cases.
'''
README

input of the code is like the example below:

e.g.we want to find the operations of a mxn matrix with the sum=k

type"outf.write(main(m,n,k))"at the end of this program

'''

class Node :
    def __init__ (self,val_site,lft=None,rt=None,baba=None):
        self.val = val_site
        self.lftChd = lft
        self.rtChd = rt
        self.father = baba

class Null_Node:
    def __init__(self,val_site=[-1,-1],lft="null",rt="null",baba=None):
        self.val = val_site
        self.lftChd = lft
        self.rtChd = rt
        self.father = baba

class Root :
    def __init__ (self,val_site=[0,0],lft=None,rt=None,baba=None):
        self.val = val_site
        self.lftChd = lft
        self.rtChd = rt
        self.father = baba

class Tree :
    def __init__ (self,val_site=[0,0],lft=None,rt=None):
        self.root = Root(val_site) #建立根节点只需要输入根节点数字值
        self.left_subT = None
        self.right_subT = None
        #用来记录每一个节点是否已满
        self.list = []
        self.list.append(self.root)

    def add_node(self,tree,val_site,hang,lie):
        baba_node = self.list[0] #顺序取未满的节点的第一个
        new_node = Node (val_site)
        baba_x = baba_node.val[0]
        baba_y = baba_node.val[1]
        new_x = new_node.val[0]
        new_y = new_node.val[1]
        #添加新节点的顺序为先左后右,左=下，右=右
        if baba_node.lftChd == None and baba_x+1==new_x:#往下走没到最后一行
            baba_node.lftChd = new_node
            #print("new",new_node.val,"lft",baba_node.lftChd.val)
            #print("new",new_node.val,"list",self.list[len(self.list)-1].val)
            #print(baba_node.lftChd.val)
            new_node.father = baba_node
            self.list.append(new_node)#新添加的节点记录到列表中
        elif baba_node.lftChd==None and baba_x==hang-1 :#往下走到了最后一行
            null_node = Null_Node( )
            baba_node.lftChd = null_node
            null_node.father = baba_node
            baba_node.rtChd = new_node
            new_node.father = baba_node
            #print("lft",baba_node.lftChd.val,"rt",new_node.val)
            self.list.append(new_node)
            self.list.pop(0)
        elif baba_node.lftChd!=None and baba_node.lftChd!="null": #往右走
            if baba_y+1==new_y:
                if new_node.val == baba_node.lftChd.val:
                    null_node = Null_Node( )
                    baba_node.rtChd = null_node
                    null_node.father = baba_node
                    #print("Rnull:",baba_node.rtChd.val)
                    self.list.pop(0)
                    tree.add_node(tree,new_node.val,hang,lie)
                else:
                    baba_node.rtChd = new_node
                    #print("R:",baba_node.rtChd.val)
                    new_node.father = baba_node
                    self.list.append(new_node)
                    #此时爸爸节点已满，从列表中除去
                    self.list.pop(0)
            elif baba_y == lie-1:
                    null_node = Null_Node( )
                    baba_node.rtChd = null_node
                    null_node.father = baba_node
                    #print("Rnull:",baba_node.rtChd.val)
                    self.list.pop(0)
                    tree.add_node(tree,new_node.val,hang,lie)
        

    def leave(self,node):
        if node.lftChd == None and node.rtChd == None:
            return [node]
        elif node.lftChd == "null" and node.rtChd == "null":
            return [node]
        elif node.lftChd != None and node.rtChd != None :
            return (self.leave(node.lftChd)+self.leave(node.rtChd))
        elif node.lftChd != None and node.rtChd == None :
            return (self.leave(node.lftChd))
        elif node.lftChd == None and node.rtChd != None :
            return (self.leave(node.rtChd))

def set_matrix(hang,lie):
    m = hang
    n = lie
    matrix = []
    for i in range(1,m+1):
        matrix.append([i]*n)
    return matrix

def put_in_tree(hang,lie):
    hang = int(hang)
    lie = int(lie)
    #设list作为树节点队列[行，列]
    list1 = [[0,0]]
    #设tree_list作为最终记录树节点的列表
    tree_list = []
    #当list里没有元素时结束循环
    while (len(list1)!= 0):
        if list1[0][0]+1<hang and list1[0][1]+1<lie :
            D = [list1[0][0]+1,list1[0][1]]
            R = [list1[0][0],list1[0][1]+1]
            list1.append(D)
            list1.append(R)
            tree_list.append(list1.pop(0))
        elif list1[0][0]+1<hang and list1[0][1]+1==lie:#一行顶到头了,只能往下走
            D = [list1[0][0]+1,list1[0][1]]
            list1.append(D)
            tree_list.append(list1.pop(0))
        elif list1[0][0]+1==hang and list1[0][1]+1<lie:#一列顶到头了,只能往右走
            R = [list1[0][0],list1[0][1]+1]
            list1.append(R)
            tree_list.append(list1.pop(0))
        elif list1[0][0]+1==hang and list1[0][1]+1==lie:#到右下角了
            tree_list.append(list1.pop(0))
        #print("list:",list1)
        #print("tree_list: ",tree_list)
    #print(tree_list)
    #print("out")
    return tree_list


def main (hang,lie,k):    
    tree = Tree([0,0])
    tree_val_list = put_in_tree(hang,lie)
    tree_val_list.pop(0)
    for val in tree_val_list:
        tree.add_node(tree,val,hang,lie)

    matrix = set_matrix(hang,lie)

    leave_list = tree.leave(tree.root)
    
    for leave in leave_list:
        node = leave
        sum = hang
        node_list = []
        #print("start:",node.val)
        if node.val != [-1,-1] :
            while node.father != None:
                #print(node.father.val)
                x = node.father.val[0]
                y = node.father.val[1]
                #print("xy:",matrix[x][y])
                sum = sum + matrix[x][y]
                node_list.append(node)
                node = node.father
                #print("sum:",sum)
        if sum == k:
            node = node_list[0]
            break
        
    actions = ""
    while node.father != None:
        f_site = node.father.val
        n_site = node.val
        if n_site[0]-f_site[0]== 1:
            actions = actions + "D"
        elif n_site[1]-f_site[1]==1:
            actions = actions + "R"
        node = node.father
    actions = actions[::-1]
    return(str(k)+" "+actions)

print(main(5,5,27))

'''outf=open("output_question_1.txt","a")
#outf.write(main(3,3,8))
outf.write(main(9,9,65))
outf.write("\n")
outf.write(main(9,9,72))
outf.write("\n")
outf.write(main(9,9,90))
outf.write("\n")
outf.write(main(9,9,110))
outf.write("\n")
outf.write(main(90000,100000,87127231192))
outf.write("\n")
#outf.write(main(90000,100000,5994891682))
outf.close()'''
        
        
