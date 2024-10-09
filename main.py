import classifierclass, re, forward, backward

#given a string, convert to x list
def stringToXList(strpt):
    tempdata = []
    clines = strpt.split("\n")
    testx = list()

    l = re.sub('^\s+', '', strpt)
    l = re.sub('\s+$', '', strpt)
    tempdata = re.split('\s+', l)

    numdimensions = len(tempdata)

    #make all strings in tempdata into floats
    for d in range(numdimensions):
        #print(d, "testx =", testx, "t =", tempdata[d], "\n")
        testx.append(float(tempdata[d]))      #skip b[l][0] since that is the 

    #print("testx =", testx,"\n")
    return testx

def main():
    print("Welcome to Shruti's Evaluation Function and NN-classifier.\nType in the name of the file to test:")
    filename = input() #string
    
    cl = classifierclass.classifier(filename)
    #print("in main: cl =", cl.data)
    numfeatures = cl.getnumfeat()

    #print("Please enter feature subset you want to check accuracy of:")
    #featsubsetstr = input() #string
    #featsubset = list(map(int, featsubsetstr.split()))

    #val = classifierclass.validator(filename)
    #acc = val.leaveOneOut(featsubset)

    print("Type the number of the algorithm you want to run.\n1 Forward Selection\n2 Backward Elimination")
    algotype = input()

    if algotype == '1':
        print("\nUsing forward selection...\nBeginning search...")
        f = forward.forwardSelection(numfeatures, filename) #should be number of columns in file
        print("reached main from forwardSelection", f)
    elif algotype == '2':
        print("\nUsing backward elimination...\nBeginning search...")
        b = backward.backwardElimination(numfeatures, filename)
        print("reached main from backwardElimination", b)
    else:
        print("\nInvalid number. Please type either '1' or '2'.")


    return


if __name__ == "__main__":
    main()

