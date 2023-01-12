import pandas
import numpy as np
X = [1 , 4 , 5 , 6, -2 , 9 , 3 , 4 , 0 , 2]
def mov_avg_fil(f_list, f_len):
    output = []
    for i in range(len(f_list)):
        if i <= len(f_list) - f_len:
            min_list = []
            for j in range(f_len):
                min_list.append(f_list[i + j])
            output.append(sum(min_list)/f_len)

    return(output)

a_mov_fil = mov_avg_fil(X, 4)
# print(a_mov_fil)

X2 = [4 , 7, 8, 2 , 10 , 23 , 9 , 5]
W = [1 , 2 , 3 , 2 , 1]

def weight_avg_fil(f_list, f_len, w_list):
    output = []
    for i in range(len(f_list)):
        if i <= len(f_list) - f_len:
            min_list = []
            min_list2 = []
            for j in range(f_len):
                min_list.append(f_list[i + j])

            for k in range(len(min_list)):
                min_list2.append(min_list[k] * w_list[k])

            output.append(sum(min_list2)/sum(w_list))

    return(output)

w_mov_fil = weight_avg_fil(X2, 5, W)
print(w_mov_fil)

