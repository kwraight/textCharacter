import matplotlib.pyplot as plt
import numpy as np
import time
import argparse
import operator
import character


# commandline arguments
# specify input filename output filename
# flag show image

######################
### parsing
######################

def GetArgs():
    parser = argparse.ArgumentParser(description=__file__)

    # basic inputs
    parser.add_argument('--infiles', nargs='+', help='input filenames')
    parser.add_argument('--plot', help='show plots')

    args = parser.parse_args()

    print "args:",args

    argDict={'infile':[], 'plot':1 }

    for a in vars(args).iteritems():
        if not a[1]==None:
            print "got argument",a
            try:
                argDict[a[0]]=int(a[1])
            except:
                argDict[a[0]]=a[1]


    return argDict

######################################
### useful functions
######################################

def GetCharacteristics():


    return

def PlotComparison():


    return

######################
### main
######################

def main():

get chactgerisitics per file
plot PlotComparison
table comparison


    return

if __name__ == "__main__":
print "### in",__file__,"###"
start = time.time()
main()
end = time.time()
print "\n+++ Total scan time: ",(end-start),"seconds +++\n"
print "### out",__file__,"###"
