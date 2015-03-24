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

graph = [[0 for i in range(n)] for j in range(n)]
