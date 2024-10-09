import math

def euclidean(point1, point2): #given two points, return the distance between the two
    #find diff for all dimensions of point1 and point2
    #save square of each dimension in diff
    #sum across all dimensions of the list of squared values found above
    #final result is sqrt of the sum found above

    #print("in distance.py:")

    numfeat = len(point1)
    sumofsquares = 0
    #print("p1 =", point1, "\np2 =", point2)
    
    for i in range(numfeat):
        #print(i, type(point1), type(point2))

        sumofsquares += (point1[i] - point2[i])**2
    
    #print("sumofsquares =", sumofsquares)

    result = math.sqrt(sumofsquares)

    #if point1 == [1.2891084, 2.7268616, 4.6027145]:
    #    print("r =", result)
    #print("p1 =", point1, "\np2 =", point2, "\nresult =", result, "\n")
    return result


#testing this function
#p1 = [1.1,2.0,3.0,4.0,5.0]
#p2 = [2.0,3.0,4.0,5.0,6.0]
#euclidean(p1, p2)
