# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import time

######################################
### useful functions
######################################

def MakeRadar(df):
    # ------- PART 1: Create background

    # number of variable
    categories=list(df)
    categories.remove('group')

    print(categories)
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
    plt.ylim(0,40)

    # ------- PART 2: Add plots

    # Plot each individual = each line of the data
    print("in radarPlot")
    for i in range(0,len(df['group']),1):
        # Ind1
        values=df.loc[i].drop('group').values.flatten().tolist()
        print(values)
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=df['group'][i])
        ax.fill(angles, values, 'b', alpha=0.1)

    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.show()

    return

######################
### main
######################

def main():

    # Set data
    df = pd.DataFrame({
    'group': ['A','B','C','D'],
    'var1': [38, 1.5, 30, 4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
    })

    MakeRadar(df)


    return


if __name__ == "__main__":
    print "### in",__file__,"###"
    start = time.time()
    main()
    end = time.time()
    print "\n+++ Total scan time: ",(end-start),"seconds +++\n"
    print "### out",__file__,"###"
