import matplotlib.pyplot as plt
import numpy as np
import time
import argparse
import operator
import pandas as pd
import character as chr
import radarPlot as rp


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

    argDict={'infiles':[], 'plot':1 }

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

def GetCharacteristics(filename):
# get characterisitic parameters from file

    rawList= chr.GetRawList(filename) # read in all characters from file (remove new lines)
    cleanList= chr.GetCleanList(rawList, [" ", "\\"]) # clean list of bad characters (e.g. whitespaces)
    lowList= [ch.lower() for ch in cleanList] # make all characters lower case
    freqDict = {i:lowList.count(i) for i in lowList} # count frequency for each unique character
    mpv, popVowels= chr.GetMostPopular(freqDict, "aeiou")
    mpc, popConsonants= chr.GetMostPopular(freqDict, "bcdfghjklmnpqrstvwxyz")
    retDict= {
            'group': filename,
            'total': len(cleanList),
            'uniques': len(freqDict),
            'aveVows': chr.GetAveFreq(freqDict, "aeiou"),
            'MPV': mpv,
            'aveCons': chr.GetAveFreq(freqDict, "bcdfghjklmnpqrstvwxyz"),
            'MPC': mpc,
            'AWL': chr.GetAveWordLength(filename)
            }
    # all character output
    print(freqDict)
    print("total # characters:", retDict['total'])
    print("total unique characters:", retDict['uniques'])
    # average frequencies
    print("average vowel frequency:", retDict['aveVows'])
    print("average consonants frequency:", retDict['aveCons'])
    # most popular characters
    print("most popular vowels ("+str(mpv)+"):", popVowels)
    print("most popular consonants ("+str(mpc)+"):", popConsonants)
    # average word length
    print("average word length:", retDict['AWL'])

    return retDict


def PlotComparison(df):

    rp.MakeRadar(df)

    return

######################
### main
######################

def main():

    argDict=GetArgs()
    print("argDict:",argDict)

    '''
    get chactgerisitics per file
    plot PlotComparison
    table comparison
    '''

    if len(argDict['infiles'])==0:
        print("No input filenames specificed. Exiting")
        return

    dataDict = {
    'group': [],
    'uniques': [],
    'AWL': [],
    'aveVows': [],
    'MPV': [],
    'aveCons': [],
    'MPC': []
    }

    for f in argDict['infiles']:
        tempDict=GetCharacteristics(f)
        print("### the second")
        print(tempDict)
        dataDict['group'].append(tempDict['group'])
        dataDict['uniques'].append(tempDict['uniques'])
        dataDict['AWL'].append(tempDict['AWL'])
        dataDict['aveVows'].append(tempDict['aveVows'])
        dataDict['MPV'].append(tempDict['MPV'])
        dataDict['aveCons'].append(tempDict['aveCons'])
        dataDict['MPC'].append(tempDict['MPC'])

    df= pd.DataFrame.from_dict(dataDict)

    # Plotting
    if argDict['plot']==1:
        PlotComparison(df)


    print("### Comparison Table")
    print(df[['group','uniques','AWL','aveVows','MPV','aveCons','MPC']].to_string(index=False))

    return

if __name__ == "__main__":
    print "### in",__file__,"###"
    start = time.time()
    main()
    end = time.time()
    print "\n+++ Total scan time: ",(end-start),"seconds +++\n"
    print "### out",__file__,"###"
