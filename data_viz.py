import math
import sys
import matplotlib
import math_lib as ml
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def boxplot(L, out_file_name):
    x = []
    y = []
    for l in L:
        A = l.rstrip().split()
        x.append(float(A[0]))
        y.append(float(A[1]))

    stat_mean = str(ml.list_mean(y))
    stat_stdev = str(ml.list_stdev(y))
    width = 3
    height = 3

    fig = plt.figure(figsize=(width, height), dpi = 300)
    ax = fig.add_subplot(1,1,1)
    ax.boxplot(x,y,'.')
    plt.title("Mean: " + stat_mean + " " + "stdev: " + stat_stdev)
    plt.ylabel('Frequency')
    plt.savefig(out_file_name, bbox_inches='tight')


def histogram(L, out_file_name):
    D = []
    for l in L:
        A = l.rstrip().split()
        D.append(float(A[0]))
        D.append(float(A[1]))

    width = 3
    height = 3
    stat_mean = str(ml.list_mean(y))
    stat_stdev = str(ml.list_stdev(y))
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1,1,1)
    ax.hist(D)
    plt.title("Mean: " + stat_mean + " " + "stdev: " + stat_stdev)
    plt.ylabel('Frequency')
    plt.savefig(out_file_name,bbox_inches='tight')

def combo(L, out_file_name):
    D = []
    x = []
    y = []

    for l in L:
        A = l.rstrip().split()
        D.append(float(A[0]))
        D.append(float(A[1]))
        x.append(float(A[0]))
        y.append(float(A[1]))

    stat_mean = str(ml.list_mean(y))
    stat_stdev = str(ml.list_stdev(y))
    width = 5
    height = 3

    fig = plt.figure(figsize=(width, height), dpi = 300)
    ax = fig.add_subplot(1,2,1)
    ax.boxplot(x,y,'.')
    ax = fig.add_subplot(1,2,2)
    ax.hist(D)
    plt.title("Mean: " + stat_mean + " " + "stdev: " + stat_stdev)
    plt.ylabel('Frequency')
    plt.savefig(out_file_name,bbox_inches='tight')
