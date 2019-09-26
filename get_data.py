import sys
import os
import math



def read_stdin_col(col_num):
    A = []
    V = []
    for l in sys.stdin:
        A = [x for x in l.split()]
        V.append(int(A[col_num]))
    return V

#def main():
    #print(read_stdin_col(0))

#if __name__ == '__main__':
    #main()
