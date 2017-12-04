

### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results):
    if results == None:			### If none will be given as input it will return none.
        return None
    results = (list(tuples) for tuples in results)			###tuples are converted into list   
    list1 = []
	###This loop is to get information of every dtudent one by one###
    for i in results:
        
        x = (i[2:])			###In x the scores of students are saved
        
        y = []
		###This loop is to seprate None from integers and floats###
        for n in x:			
            if n == None:
                continue
            else:
                y.append(n)
    
        sum1 = sum(y)### All the numbers are sumed up
        list2 = i[0:2]
        list2.append(sum1)
        list1.append(tuple((list2)))
        
        
    return list1   



#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(results):

    
    sumedup = find_cumulative_marks(results)
    numlist = []
    counter = 0
    list2 = []
    for i in sumedup:
        numlist.append(i[2])   ### It will append the total number of all the students in the numlist
    maximum = max(numlist)   ### It will compute the maximum marks from the numlist
    ### This loop will generate the output for us
    for i in sumedup:
        if maximum == i[2]:
            list2.append(i[0:2])
            counter += 1
    if counter == 1:
        for p in list2:
            return p
    return list2
#### End OF MARKER

