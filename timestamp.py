#coding=utf-8
import csv
import numpy as np
import matplotlib.pyplot as plt

col_type =[int, int]
f = open('./20220107/Board2/0930/cam8_B.csv')
f_csv = csv.reader(f)
last_row = 0
counter = 0
list_x = list()
for row in f_csv:
    row = tuple(convert(value) for convert, value in zip(col_type, row))
    if(counter > 0):
        list_x.append(int((row[1]- last_row)/1000))
    counter = counter + 1
    last_row = row[1]

max_len = len(list_x)
x = np.linspace(1, max_len, max_len)
y = list_x
# plt.plot(x, list_x, ls='-', lw=2, label='cosine', color='purple')
plt.plot(x, y)

xlabel  = 'total %d' %max_len

plt.legend()
plt.xlabel(xlabel)
plt.ylabel('diff')
plt.show()

