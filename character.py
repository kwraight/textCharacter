import matplotlib.pyplot as plt
import numpy as np
import time
import argparse
import operator


# commandline arguments
# specify input filename output filename
# flag show image

######################
### parsing
######################

def GetArgs():
    parser = argparse.ArgumentParser(description=__file__)

    # pass on
    parser.add_argument('--infile', help='input filename')
    parser.add_argument('--plot', help='show plots')

    args = parser.parse_args()

    print "args:",args

    argDict={'infile':"NYS", 'plot':1 }

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

def GetRawList(filename):
#read file and raw list of characters

    retArr= [ch for ch in open(filename).read() if ch != '\n' if ch != ' ']

    return retArr

def GetFreqList(arr):
# make list of dictionaries, each with character and frequency

    retDict = {i:arr.count(i) for i in arr}

    return retDict

def PlotFreq(dict):
# bar chart of character frquencies

    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

    print(sorted_dict)

    objects= [i[0] for i in sorted_dict]
    y_pos = np.arange(len(objects))
    frequencies= [i[1] for i in sorted_dict]

    print(objects)
    print(y_pos)
    print(frequencies)

    plt.bar(y_pos, frequencies, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('frequency')
    plt.title('Frequency of each (unique) character')
    plt.show()



######################
### main
######################

def main():

    argDict=GetArgs()
    print "argDict:",argDict

    if "NYS" in argDict['infile']:
        print("No input filename specificed. Exiting")
        return

    # read in all characters from file (remove whitespace and new lines)
    rawList= GetRawList(argDict['infile'])
    # make all characgters lower case
    lowList= [ch.lower() for ch in rawList]
    # count frequency for each unique character
    freqDict = {i:lowList.count(i) for i in lowList}

    print(freqDict)
    print("total # characters:", len(rawList))
    print("total unique characters:", len(freqDict))

    if argDict['plot']==1:
        PlotFreq(freqDict)

    return


if __name__ == "__main__":
    print "### in",__file__,"###"
    start = time.time()
    main()
    end = time.time()
    print "\n+++ Total scan time: ",(end-start),"seconds +++\n"
    print "### out",__file__,"###"

'''
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
'''
