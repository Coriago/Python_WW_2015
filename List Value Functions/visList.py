	

    visList = [12, 20, 37, 38, 33, 45, 46, 59, 72, 105, 119, 118]
    visList.sort()
    diffList = []
    diffCurIndex = 0
    sameDiffVis = []
    SDVdiffs = []
    finalvals = []
    try:
        for n in visList:
            try:
                cur = visList.index(n)      #makes cur the index value of the current item in the original list.
                nex = cur + 1      #makes nex the index value of the next item in the original list.
                diffList.append(visList[nex] - visList[cur])        #places the difference between the two items in the list in diffList.
            except IndexError:
                pass       #does that for each item in the list, passes to the next code section when the above code returns an error for trying to access index numbers that don't exist in the list.
        for z in diffList:
            if diffList[diffCurIndex] == min(diffList):     #if the item at index value diffCurIndex (the current index value we're utilizing) has the smallest difference in the diffList...
                sameDiffVis.append(visList[diffCurIndex])       #add the item in the original list that has the index value of diffCurIndex.
            diffCurIndex += 1      #whether we added any values to the list of items with the minimum difference or not, step the index value we're working with up one.
        for g in sameDiffVis:
                SDVdiffs.append(abs(120 - g))       #makes a list that contains how far away from 120 each item that had a minimum difference was.
        finalvals.append(sameDiffVis[SDVdiffs.index(min(SDVdiffs))])        #puts the number that begins the pair that has both the smallest difference between eachother and that are the closest to 120
        finalvals.append(sameDiffVis[SDVdiffs.index(min(SDVdiffs))] + min(diffList))        #does almost the same thing but adds the number that ends the pair
        print finalvals
    except ValueError:
        #this SHOULD only occur if visList is equal to []
        pass


