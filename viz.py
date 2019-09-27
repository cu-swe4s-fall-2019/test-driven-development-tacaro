import sys
import os
import math
import argparse
import data_viz as dv
import get_data as gt
import numpy as np


def main():
    parser = argparse.ArgumentParser(
                description='Read a file from stdin, generate a plot',
                prog='bay')

    parser.add_argument('-o',  # input file, from user
                        '--out_file',
                        type=str,
                        help="File Name With Which to Save Plot",
                        required=True)

    parser.add_argument('-p',  # desired column, from user
                        '--plot_type',
                        type=str,
                        help="Types are: 'hist', 'box', 'combo'",
                        required=True)

    args = parser.parse_args()
    file_out = args.out_file
    type = args.plot_type

    x = gt.read_stdin_col(0)
    #print(x)
    y = gt.read_stdin_col(1)
    #print(y)
    combined = np.vstack((x,y)).T
    combined = combined.tolist()

    if type == "hist":
        dv.histogram(combined, file_out)
    if type == "box":
        dv.boxplot(combined, file_out)
    if type == "combo":
        dv.combo(combined, file_out)

if __name__ == '__main__':
    main()
