try:
    numbers = [33,59,72,118,117,12,21,20]
    numbers.sort()
    #Declare Variables area
    diff = []
    ValueClosest = 120
    CloseDupe = []
    duplicates = []
    counter = 0
    counter2 = 0

    for x in range(len(numbers)-1):
        diff.append(numbers[x + 1] - numbers[x])


    #CODE TO CHECK FOR DUPES***
    if diff.count(min(diff)) > 1:

        #Move duplicates into an array
        for x in diff:
            if diff[counter] == min(diff):
                duplicates.append(numbers[counter])
            counter += 1
            
        #Take each value in previous array and subtract them by wanted value
        #Then place into new array
        for x in duplicates:
            CloseDupe.append(abs(duplicates[counter2] - ValueClosest))
            counter2 += 1

        # find index of min for close dupes
        #take value find index in numbers and add 1
        num1 = duplicates[CloseDupe.index(min(CloseDupe))]
        num2 = numbers[numbers.index(num1)+1]
        
    #END CODE TO CHECK FOR DUPES***

    else:
        num1 = numbers[diff.index(min(diff))]
        num2 = numbers[diff.index(min(diff)) + 1]

    #Final outcome
    print str(num1) +" "+ str(num2)
except ValueError:
    pass




    
    


