def main (m,n,get_s):
    min_sum = n-1 + ((1+m)*m)/2
    max_sum = (n-1)*m + ((1+m)*m)/2
    if get_s<min_sum or get_s>max_sum:
        return "out of range. can not find the way"
    #Move k column forward from the minimum sum method, increasing the sum
    k = int((get_s - min_sum) // (m-1))#从最小和方法向前移动k列，增大和
    #The number of digits that move an incomplete column after moving a complete column
    first_dw = int((get_s - min_sum) % (m-1))#移动完整列后再向前移动不完整的一列的数字个数
    first_rt = n-1 - k - 1
    second_dw = m-1 -first_dw
    way = "R"*first_rt + "D"*first_dw + "R" + "D"*second_dw + "R"*k
    return way


outf=open("output_question_1","a")
outf.write(main(90000,100000,87127231192))
outf.write("\n")
outf.write(main(90000,100000,5994891682))
outf.close()
