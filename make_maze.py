#
#
#
# Katsigiannis Fotis
# 1st Assignment
#
#
#

import sys
import random

n = int(sys.argv[1])
x = int(sys.argv[2])
y = int(sys.argv[3])
random.seed(sys.argv[4])
outputfile = sys.argv[5]

def get_matrix(n):
   """Read in and return a matrix of ints with n rows and n columns"""
   mat = []
   for i in range(n):
      row_str = raw_input("")
      row_str_l = row_str.split()
      row = []
      for j in range(n):
         row.append(int(row_str_l[j]))
      mat.append(row)
   return mat
