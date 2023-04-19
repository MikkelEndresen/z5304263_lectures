lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]

new_list = [x**2 for x in lst if x**2 > 150]
#print(new_list)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]

newt = [x for x in numbers if x % 2 ==0]
print(list(set(newt)))

import yf_example1

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    '''
    Method to download qantas share price into csv
    '''
    start = str(year) + "-01-01"
    end = str(year) + "-12-31"
    pth = "data/"
    tic = "QAN.AX"
    name = "an_prc_" + str(year) + ".csv"
    yf_example2.yf_prc_to_csv(tic, pth+name, start=start, end=end)

qan_prc_to_csv(2020)