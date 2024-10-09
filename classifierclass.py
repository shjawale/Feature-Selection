#used GeeksforGeeks to make the contents a file into a string and then split it into a list of data

import distance, copy, re, math

##got the outline for this from datagy.io/python-z-score/
def znorm(allxvalues):   #znormAllFeats calls znorm as many times as there are feature columns in the data
    # Calculate  the Standard Deviation in Python
    zscores = copy.deepcopy(allxvalues)
    for c in range(len(allxvalues[0])):
        mean = 0
        for i in range(len(allxvalues)):
            mean += allxvalues[i][c]
        mean = mean / len(allxvalues)

        sumofsquares = 0
        for i in range(len(allxvalues)): 
            sumofsquares += (allxvalues[i][c] - mean)**2

        standard_deviation = math.sqrt(sumofsquares / (len(allxvalues)))
        #print(mean, standard_deviation, "for", singlefeatcol[0], "\n")

        # Calculate the z-score from scratch
        for i in range(len(allxvalues)): 
            zscores[i][c] = ((allxvalues[i][c] - mean) / standard_deviation)
        #print("singlefeatcol =", singlefeatcol, "\nmean =", mean, "\ndifferences =", differences, "\nstandard_deviation =", standard_deviation, "\nzscores =", zscores, "\n\n")

    return zscores   #return list of znormed singlefeatcol

class classifier(): #file must be a .txt file
    #numfeatures = len(file[0]), aka number of columns
    #print('in classifier class')

    def __init__(self, filename):
        #x,y = fillXandY()
        #self.data = x             #list of lists with the features values for each point
        #self.classlabels = y      #list with a size same as number of lines in file
        
        #print("inside initializer for classifier:")
        
        #x, y, numlines, numdimensions = fillXandY(filename)
        '''
        if filename == "small-test-dataset.txt":
            file = open("data/small-test-dataset.txt","r")
        elif filename == "large-test-dataset.txt":
            file = open("data/large-test-dataset.txt","r")
        elif filename == "my-small-dataset_35.txt":
            file = open("data/my-small-dataset_35.txt","r")
        elif filename == "my-large-dataset_35.txt":
            file = open("data/my-large-dataset_35.txt","r")
        ''' 
        file = open("data/" + filename,"r")

        tempdata = []
        numlines = 0
        numdimensions = 0

        contents = file.read()
        clines = contents.split("\n")

        #print("X:")
        for l in clines:
            if l:       #makes sure that tempdata does not end with a [''] by only incrementing numlines when the line is not empty
                l = re.sub('^\s+', '', l)
                l = re.sub('\s+$', '', l)
                tempdata.append(re.split('\s+', l))
        numlines = len(tempdata)

        numdimensions = len(tempdata[0]) - 1

        x = list()
        y = list() 

        #make all strings in b into floats
        for l in range(numlines):
            y.append(float(tempdata[l][0]))
            x.append(list())
            for d in range(1, len(tempdata[l])):
                #print("x[", l, "] =", x[l])
                x[l].append(float(tempdata[l][d]))      #skip b[l][0] since that is the corresponding y

            #print("x =", x[l])
       
        zx = znorm(x)
        ''' 
        ind = 0
        #zfeatset = copy.deepcopy(x[:][:4])
        zfeatset = list()
        feats = [2, 6, 7, 8, 9, 10]
        for c in feats:
            for r in range(len(x)):
                zfeatset.append(list())
                print(r,c-1,ind, len(x))
                #print("zfeatset =", zfeatset[r], "  ", x[r][c-1])
                zfeatset[r].append(x[r][c-1])
            ind += 1
        print("zfeatset =", zfeatset)
        '''

        self.data = zx             #list of lists with the features values for each point
        self.classlabels = y      #list with a size same as number of lines in file
        self.numinstances = numlines
        self.numfeat = numdimensions

    def trainNearestNeighbor(self, data):
        #input to the Train method is the set of training instances (or their IDs)
        #no output for this method.
        #Note that the class label for each instance is provided along with the feature vector.
        
        #remember nearest neighbor has nothing to train, all work/calculations are done when testing a given point
        return

    def testNearestNeighbor(self, testpoint, datasubset): 
        #input to the Test method is a test instance (or its ID) 
        #output is the predicted class label.
        
        #mainly going to use distance.euclidean(p1, p2) on a bunch of pairs of points.
        #print("inside testNearestNeighbor")

        predictedClassLabel = 0
        numpoints = len(datasubset)   #self.numinstances only if datasubset is empty
        mindist = 1e9
        nearestpoint = list()  #length is len(datasubset)
        idnum = numpoints + 2  #invalid index in self.classLabels
       
        #print("testpt =", testpoint, " numpoints =", numpoints)
        #print(self.data[0])
        for k,v in sorted(datasubset.items()): #go down the points in data and check distance to testpoint
            #print("  testpoint =", testpoint, "  datasubset[", i, "] =", datasubset[k])
            #print("  datasubset[", i, "] =", datasubset[k])
            currdist = distance.euclidean(testpoint, datasubset[k])
            #print("  currdist =", currdist, "  mindist =", mindist)
            if currdist < mindist: #save distance and the datapoint (row) of nearest neighbor
                mindist = currdist
                nearestpoint = datasubset[k]
                idnum = k
            #print("\n")

        #print("NN is:", nearestpoint, "which is point", idnum, "at distance of", mindist)
        predictedClassLabel = self.classlabels[idnum] #testpoint's classLabel is the same as the classLabel of nearest neighbor
        #print("NN to", testpoint, "is point", idnum, "at distance of", mindist, "and the predicted class is", predictedClassLabel)
        #print("NN is point", idnum, "at distance of", mindist, "and the predicted class is", predictedClassLabel)                      #good print
        return predictedClassLabel


    def ifSameClassLabel(self, predclass, instnum):
        #print("in ifSameClassLabel: instnum =", instnum, "  predclass =", predclass, "  actualclass", self.classlabels[instnum])    #good print
        return abs(predclass - self.classlabels[instnum]) < 0.01
    
    def getnumfeat(self):
        return self.numfeat

#test the initializer
#cl = classifier()
#print(cl.data)
#testpt = [4.3049096, 1.8931881, 0.0810018, 2.4838479, 4.1251075, 2.3844308, 3.4647919, 1.0, 1.0, 2.0]
#test = cl.testNearestNeighbor(testpt, list())
#print("predictedClassLabel =", test)

class validator(classifier): 
#class validator(): 
    #print('in validator class')

    def __init__(self, filename):
        classifier.__init__(self,filename)  #actually do need this because validator needs to be able to access classifier.data, which is z-normalized
        self.filename = filename
    
    def leaveOneOut(self, featsubset): 
        #Given a feature subset as input, it returns a score (classifier’s accuracy) as output. It needs to use the training data and the classifier to do its job.

        #featsubset is a list of lists, each of which refers to an instance in the dataset

        #print("inside leaveOneOut")
        #featsubset = list()
        c = classifier(self.filename)

        #print("featsubset =", featsubset)

        i = 0
        subset = list()
        #print("c =", c.data)
        for line in c.data:
            subset.append(list())
            for featnum in featsubset:
                #print("in leaveOneOut: featnum =", featnum)
                subset[i].append(line[featnum-1])  #index is actually the feature number -1
            i += 1
            #print("subset =", subset)
        
        currsum = 0
        instnum = 0
        for line in subset:
            #print("instnum =", instnum, "  currsum =", currsum)  #good print
            tempsubset = dict()
            for i in range(len(subset)):
                if subset[i] != line:
                    tempsubset[i] = subset[i]
            #print("ts =", tempsubset)
            #print("line =",line, "  ", float(self.classlabels[instnum]))    #good print
            predclass = c.testNearestNeighbor(line, tempsubset)  #compare line with all other instances, only looking at the subset specified features
            if c.ifSameClassLabel(predclass, instnum):            #int(predclass == self.classlabels[instnum])  #sum gets incremented by 1 when the predicted class Label is the same as the actual label
                currsum += 1
            instnum += 1   #corresponds to the instance number in self.data
            #print("\n")

        accuracy = currsum #/ len(c.data) #* len(self.numinstances)  #make sure it's not a float, cuz they are annoying 
        return accuracy
