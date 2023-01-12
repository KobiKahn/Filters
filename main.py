import pandas
import numpy as np
X = [1 , 4 , 5 , 6, -2 , 9 , 3 , 4 , 0 , 2]
W = [1, 1, 1, 1]

X2 = [4 , 7, 8, 2 , 10 , 23 , 9 , 5]
W2 = [1 , 2 , 3 , 2 , 1]

X3 = [4 , 7, 8, 2 , 10 , 23 , 9 , 5]
W3 = [.5, .5]

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

w_mov_fil1 = weight_avg_fil(X, 4, W)
w_mov_fil2 = weight_avg_fil(X2, 5, W2)
# print(w_mov_fil1)
# print(w_mov_fil2)

def fade_avg_fil(f_list, w_list):
    output = []
    w1, w2 = w_list[0], w_list[1]
    if sum(w_list) == 1:
        for i in range(len(f_list)):
            if i == 0:
                output.append(f_list[i])
            else:
                output.append( (w1 * output[i-1]) + (w2 * f_list[i]) )

    return(output)

f_mov_fil = fade_avg_fil(X3, W3)
# print(f_mov_fil)







