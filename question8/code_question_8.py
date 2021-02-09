import numpy as np
import math as m
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

#the fuction that calculate the rate of change of P
def f(Mes):#计算P的rate的函数
    Mp_dt = 100*Mes
    return Mp_dt
    
#the fuction that calculate the rate of change of S
def g(Mes,Me,Ms):
    Ms_dt = 600*Mes - 100*Me*Ms
    return Ms_dt
    
#the fuction that calculate the rate of change of ES
def h(Mes,Me,Ms):
    Mes_dt = 100*Me*Ms - 750*Mes
    return Mes_dt
    
#the fuction that calculate the rate of change of E
def j(Mes,Me,Ms):
    Me_dt = 750*Mes - 100*Me*Ms
    return Me_dt
    
#use Runge-Kutta
def rk4(k,T):#设置步长和总时间 Set the step length k and total time T  
    m = 0 #ES 初始量original bulk
    n = 1 #E 初始量original bulk
    p = 10 #S 初始量original bulk
    Mp = 0 #P 初始量original bulk
    time = 0 #时间初始值Initial time value
    
    time_list =[]
    P_list = []
    E_list = []
    ES_list = []
    S_list = []
    vp_list = []
    
    while time<T:
        time_list.append(time)
        P_list.append(Mp)
        E_list.append(n)
        S_list.append(p)
        ES_list.append(m)
        
        time += k
        
        f1 = f(m)
        g1 = g(m,n,p)
        h1 = h(m,n,p)
        j1 = j(m,n,p)
        m1 = m + h1*k/2
        n1 = n + j1*k/2
        p1 = p + g1*k/2
        
        f2 = f(m1)
        g2 = g(m1,n1,p1)
        h2 = h(m1,n1,p1)
        j2 = j(m1,n1,p1)
        m2 = m + h2*k/2
        n2 = n + j2*k/2
        p2 = p + g2*k/2
        
        f3 = f(m2)
        g3 = g(m2,n2,p2)
        h3 = h(m2,n2,p2)
        j3 = j(m2,n2,p2)
        m3 = m + h3*k
        n3 = n + j3*k 
        p3 = p + g3*k 
        
        f4 = f(m3)
        g4 = g(m3,n3,p3)
        h4 = h(m3,n3,p3)
        j4 = j(m3,n3,p3)
        
        m = m + (h1 + 2*h2 + 2*h3 + h4)*k/6
        n = n + (j1 + 2*j2 + 2*j3 + j4)*k/6
        p = p + (g1 + 2*g2 + 2*g3 + g4)*k/6
        Mp = Mp + (f1 + 2*f2 + 2*f3 + f4)*k/6
        vp = (f1 + 2*f2 + 2*f3 + f4)/6
        vp_list.append(vp)
    time_list.append(time)
    P_list.append(Mp)
    E_list.append(n)
    S_list.append(p)
    ES_list.append(m)
        
    return (time_list,P_list,ES_list,E_list,S_list,vp_list)
    
rk4_result = rk4(0.001,0.15)
time_list = rk4_result[0]
P_list = rk4_result[1]
ES_list = rk4_result[2]
E_list = rk4_result[3]
S_list = rk4_result[4]
vp_list = rk4_result[5]

plt.plot(time_list,P_list,color="r",label="P")
plt.plot(time_list,E_list,color="b",label="E")
plt.plot(time_list,ES_list,color="y",label="ES")
plt.plot(time_list,S_list,color="g",label="S")
plt.legend()
plt.show()

outf = open("output_question_8_2.txt","a")
outf.write("time\tP\tES\tE\tS\n")
for i in range(len(time_list)):
    time = str( time_list[i] )
    P = str( P_list[i] )
    ES = str( ES_list[i] )
    E = str(E_list[i])
    S = str(S_list[i])
    outf.write(time+"\t"+P+"\t"+ES+"\t"+E+"\t"+S+"\n")
outf.close()

S_list.pop(0)
sns.set()
plt.plot(S_list,vp_list)
plt.scatter(S_list,vp_list,marker = ".",linewidths = 0.05,c="r" )
plt.xlabel("C[S]")
plt.ylabel("V")
max_vp = 0
for i in range(len(vp_list)):
    if vp_list[i] > max_vp:
        max_vp = vp_list[i]
        max_vp_index = i
print(max_vp)


plt.text(S_list[max_vp_index],vp_list[max_vp_index],"%.4f"%vp_list[max_vp_index])

plt.show()

    
    
    
