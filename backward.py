import classifierclass, copy

def backwardElimination(numfeatures, filename): #numfeatures = len(file[0]), aka number of columns
    allfeats = list(range(1, numfeatures+1))      #fill allfeats with all the numbers of each feature
    upperboundrand = 100     #should be max value the rand can take
    maxaccuracy = 0
    featwithmaxaccuracy = allfeats
    prevLevelfeatwithmaxaccuracy = []
    val = classifierclass.validator(filename)

    #start of finding the accuracy of the feature set containing all features:
    calculatedaccuracy = val.leaveOneOut(allfeats) #returns value calculated by leave-one-out function

    print("Using feature(s) {", formatList(allfeats), "} accuracy is", calculatedaccuracy) #trace
    
    if maxaccuracy < calculatedaccuracy:  #update maxaccuracy
        maxaccuracy = calculatedaccuracy
        featwithmaxaccuracy = allfeats

    #found accuracy of allfeats
    print("\nFeature set {", formatList(allfeats), "} was best (of one), with an accuracy of", maxaccuracy)  #trace

    prevLevelmaxaccuracy = maxaccuracy
    prevLevelfeatwithmaxaccuracy = featwithmaxaccuracy.copy()
    
    maxaccuracy = 0
    featwithmaxaccuracy = allfeats
    feattoremove = 1

    currfeats = allfeats
    
    #here, the accuracy of the feature set containing all features has been calculated
    while True:
        for feattoremove in range(1, numfeatures+1):   #first combination
            if featToRemoveNotInPrevLevelList(feattoremove, prevLevelfeatwithmaxaccuracy):
                if feattoremove == numfeatures:  
                    print("Reached end of features for current level. exiting...")
                    break
                continue

            tempLevelList = copy.deepcopy(prevLevelfeatwithmaxaccuracy)
            tempLevelList.remove(feattoremove)  #removes value from the list object is is called on and returns None (pass by reference and changes the list itself)

            calculatedaccuracy = val.leaveOneOut(tempLevelList) #returns value calculated by leave-one-out function

            print("Using feature(s) {", formatList(tempLevelList), "} accuracy is", calculatedaccuracy) #trace
            if maxaccuracy < calculatedaccuracy:
                maxaccuracy = calculatedaccuracy
                featwithmaxaccuracy = tempLevelList  #update featwithmaxaccuracy with feature set with maxaccuracy

            if feattoremove == numfeatures: #reset values when you reached the end of features
                break
        
        if prevLevelmaxaccuracy > maxaccuracy:
            print("\n(Warning, accuracy has decreased!) Exiting... ") #trace
            break
        
        else:  #else accuracy increased from previousLevel, then update prevLevelmaxaccuracy with current maxaccuracy and prevLevelfeatwithmaxaccuracy with featwithmaxaccuracy
            print("\nFeature set {", formatList(featwithmaxaccuracy), "} was best, with an accuracy of", maxaccuracy) #trace  #this is different from forwards because there we are appending to prevLevelList and here we are removing from prevLevelList

            prevLevelmaxaccuracy = maxaccuracy
            prevLevelfeatwithmaxaccuracy = featwithmaxaccuracy.copy() 
        
        maxaccuracy = 0
        featwithmaxaccuracy = 1
        feat = 1
       
        if len(prevLevelfeatwithmaxaccuracy) == 1:
            break
    
    print("\nFinished search!! The best feature is {", formatList(prevLevelfeatwithmaxaccuracy), "}, with an accuracy of", prevLevelmaxaccuracy)

    return


def formatList(prevLevelList): #returns prevLevelfeatwithmaxaccuracy without the brackets
    return str(prevLevelList)[1:-1]

def featIsInPrevLevelList(feat, prevLevelList): #returns whether or not feat is already in prevLevelfeatwithmaxaccuracy
    return feat in prevLevelList

def featToRemoveNotInPrevLevelList(featSet, prevLevelList): #returns whether or not feattoremove is not already in prevLevelfeatwithmaxaccuracy
    return not featSet in prevLevelList
