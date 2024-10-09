import classifierclass, copy

def forwardSelection(numfeatures, filename): #numfeatures = len(file[0]), aka number of columns
    feat = list()
    feat.append(1)
    upperboundrand = 100  #should be max value the rand can take
    maxaccuracy = 0
    featwithmaxaccuracy = 1
    prevLevelfeatwithmaxaccuracy = []
    val = classifierclass.validator(filename)

    while True:  #should exit when you reach the end of feature columns in file
        calculatedaccuracy = val.leaveOneOut(feat) #returns value calculated by leave-one-out function

        print("Using feature(s) {", formatList(feat), "} accuracy is", calculatedaccuracy) #trace
        
        if maxaccuracy < calculatedaccuracy:  #update maxaccuracy
            maxaccuracy = calculatedaccuracy
            featwithmaxaccuracy = copy.deepcopy(feat) #int(formatList(feat))

        if feat[0] == numfeatures: #if you reached the end of features (columns) in file
            print("\nFeature set {", formatList(featwithmaxaccuracy), "} was best, with an accuracy of", maxaccuracy)  #trace

            prevLevelmaxaccuracy = maxaccuracy
            prevLevelfeatwithmaxaccuracy = featwithmaxaccuracy  #featwithmaxaccuracy is already a list

            print("prevLevelmaxaccuracy =", prevLevelmaxaccuracy, "  prevLevelfeatwithmaxaccuracy", prevLevelfeatwithmaxaccuracy, "\n")
            
            maxaccuracy = 0
            featwithmaxaccuracy = 1
            feat = 1                #0 because it gets incremented by 1 right after
            break
        feat[0] += 1
    
    
    #here, all single features' accuracy have been calculated
    feats = list()                 #we want feat to be a list so that val.leaveOneOut()'s argument has the right type, which is list
    feats = copy.deepcopy(prevLevelfeatwithmaxaccuracy)
    feats.append(1)
    while True:
        feats = copy.deepcopy(prevLevelfeatwithmaxaccuracy)
        feats.append(1)
        for i in range(1, numfeatures+1):   #each subsequent (after single features) combination is done in this loop
            if featIsInPrevLevelList(feats[-1], prevLevelfeatwithmaxaccuracy):  #make sure prevLevelfeatwithmaxaccuracy does not get combined with itself

                if feats[-1] == numfeatures:  #in case numfeatures is already in prevLevelfeatwithmaxaccuracy and feat has reached numfeatures
                    break

                feats[-1] += 1    #increment feat so that the feature we are combining prevLevelfeatwithmaxaccuracy with is not itself
                continue

            calculatedaccuracy = val.leaveOneOut(feats) #returns value calculated by leave-one-out function

            print("Using feature(s) {", formatList(prevLevelfeatwithmaxaccuracy), ",", (feats[-1]), "} accuracy is", calculatedaccuracy) #trace

            if maxaccuracy < calculatedaccuracy:
                maxaccuracy = calculatedaccuracy
                featwithmaxaccuracy = copy.deepcopy(feats[-1])

            if feats[-1] == numfeatures: #reset values when you reached the end of features
                break
            feats[-1] += 1

        #print("Done if prevLevelmaxaccuracy > maxaccuracy: prevLevelmaxaccuracy =", prevLevelmaxaccuracy, "  curr level maxaccuracy =", maxaccuracy)
        #check if current level prevLevelmaxaccuracy > maxaccuracy, then break
        if prevLevelmaxaccuracy > maxaccuracy:  #note to future self: combine this if-else outside the while loop (after the break)
            print("\n(Warning, accuracy has decreased!) Exiting... ") #trace

            break
        
        else:
            print("\nFeature set {", formatList(prevLevelfeatwithmaxaccuracy), ",", featwithmaxaccuracy, "} was best, with an accuracy of", maxaccuracy) #trace

            prevLevelmaxaccuracy = maxaccuracy
            prevLevelfeatwithmaxaccuracy.append(featwithmaxaccuracy)

        maxaccuracy = 0
        featwithmaxaccuracy = 1
        feat = 1
       
        if len(prevLevelfeatwithmaxaccuracy) == numfeatures:  #reached bottom of association graph
            #print("no more features to add to prevLevelfeatwithmaxaccuracy, reached bottom of association graph (where you start backwardElimination). exiting...")
            break

    print("\nFinished search!! The best feature is {", formatList(prevLevelfeatwithmaxaccuracy), "}, with an accuracy of", prevLevelmaxaccuracy) #trace
    return

def formatList(prevLevelList): #returns prevLevelfeatwithmaxaccuracy without the brackets
    return str(prevLevelList)[1:-1]

def featIsInPrevLevelList(feat, prevLevelList): #returns whether or not feat is already in prevLevelfeatwithmaxaccuracy
    return feat in prevLevelList
