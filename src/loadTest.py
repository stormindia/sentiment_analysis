import sys
# to suppress warning - https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
def loadTest(filename): # function to load test file in the csv format : sentiment,tweet
    f=open(filename,'r')
    k=0

    line=f.readline()
    labels=[]
    vectors=[]
    while line and k<4:
        k=k+1
        l=line[:-1].split(r'","')
        s=float(l[0][1:])
        tweet=l[5][:-1]
        print str(s)
        print tweet
        print tweet.split()
        line=f.readline()
        #print str(kneg)+"negative lines loaded"
    f.close()
    return

loadTest('../data/test_dataset.csv')
