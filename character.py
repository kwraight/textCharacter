import matplotlib.pyplot as plt
import numpy as np
import time
import argparse
import operator
import pandas as pd
import radarPlot as rp


# commandline arguments
# specify input filename output filename
# flag show plots

######################
### parsing
######################

def GetArgs():
    parser = argparse.ArgumentParser(description=__file__)

    # basic inputs
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
# read file and raw list of characters
    retArr= [ch for ch in open(filename).read() if ch != '\n']

    return retArr

def GetCleanList(arr, bads):
#get list with elements containing bad characters removed
    retArr=arr
    for b in bads:
        retArr= [ elem for elem in retArr if b not in elem]
    return retArr

def GetFreqList(arr):
# make list of dictionaries, each with character and frequency

    retDict = {i:arr.count(i) for i in arr}

    return retDict


def GetAveFreq(dict, coi=[]):
# get average frequency of characters of interest
    sumVal=0
    if len(coi)==0:
        sumVal=sum(dict.values())
        return sumVal

    for c in coi:
        try:
            sumVal+=dict[c]
        except KeyError:
            continue

    if sumVal==0:
        print("GetAveFreq >>> No frequencies found. returning 0")
        return 0

    return sumVal/len(coi)


def GetMostPopular(dict, coi=[]):
# get average frequency of characters of interest
    stat=0
    mpc=[]

    for c in coi:
        try:
            freq=dict[c]
        except KeyError:
            continue
        if freq==stat:
            mpc.append(c)
        if freq> stat:
            stat=freq
            mpc=[c]

    return stat, mpc

def GetAveWordLength(filename):
# get average word length

    sentence = open(filename).read()
    filtered = ''.join(filter(lambda x: x not in '".,;!-', sentence))
    words = [word for word in filtered.split() if word]
    avg = sum(map(len, words))/len(words)
    return avg


def PlotFreq(dict):
# bar chart of character frquencies
    print("### Plotting...")

    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

    objects= [i[0] for i in sorted_dict]
    for o in range(0,len(objects),1):
        try: # messy fudge to deal with accented characters
            deco=objects[o].decode("utf-8")
        except UnicodeDecodeError:
            deco=objects[o].encode('hex')
            print("replace:",objects[o],"-->",deco)
            objects[o]="*"+deco
    y_pos = np.arange(len(objects))
    frequencies= [i[1] for i in sorted_dict]

    print("objects:",objects)
    print("y_pos:",y_pos)
    print("frequencies:",frequencies)

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
    print("argDict:",argDict)

    if "NYS" in argDict['infile']:
        print("No input filename specificed. Exiting")
        return

    # read in all characters from file (remove whitespace and new lines)
    rawList= GetRawList(argDict['infile'])
    # clean list of bad characters (e.g. whitespaces)
    cleanList= GetCleanList(rawList, [" ", "\\"])
    # make all characgters lower case
    lowList= [ch.lower() for ch in cleanList]
    # count frequency for each unique character
    freqDict = {i:lowList.count(i) for i in lowList}

    print(freqDict)
    # all character output
    print("total # characters:", len(cleanList))
    print("total unique characters:", len(freqDict))

    # average frequencies
    aveVowels=GetAveFreq(freqDict, "aeiou")
    aveConsonants=GetAveFreq(freqDict, "bcdfghjklmnpqrstvwxyz")
    print("average vowel frequency:", aveVowels)
    print("average consonants frequency:", aveConsonants)

    # most popular characters
    mpv, popVowels=GetMostPopular(freqDict, "aeiou")
    mpc, popConsonants=GetMostPopular(freqDict, "bcdfghjklmnpqrstvwxyz")
    print("most popular vowels ("+str(mpv)+"):", popVowels)
    print("most popular consonants ("+str(mpc)+"):", popConsonants)

    # average word length
    awl = GetAveWordLength(argDict['infile'])
    print("average word length:", awl)

    # Plotting
    if argDict['plot']==1:
        PlotFreq(freqDict)

        df = pd.DataFrame({
        'group': [argDict['infile']],
        'uniques': [len(freqDict)],
        'AWL': [awl],
        'aveVows': [aveVowels],
        'MPV': [mpv],
        'aveCons': [aveConsonants],
        'MPC': [mpc]
        })

        rp.MakeRadar(df)

    return


if __name__ == "__main__":
    print "### in",__file__,"###"
    start = time.time()
    main()
    end = time.time()
    print "\n+++ Total scan time: ",(end-start),"seconds +++\n"
    print "### out",__file__,"###"
