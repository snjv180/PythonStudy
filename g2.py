#foobar:~/rabbit_test_subjects snjv180$ cat readme.txt 
#Rabbit test subjects
#====================
#
#The diabolical Professor Boolean has captured you and a group of your hapless rabbit kin as test subjects for his terrible experiments! You're not sure what his real plans are, but currently it seems he's trying to make everyone faster and smarter? He's exposing rabbit test subjects to novel chemicals, genetic manipulations, and pathogens; then measuring their completion time for various puzzles and exercises. Then again, there's a rumor he's developing a kind of zombie rabbit. You don't want to become a zombit!
#
#Unfortunately, due to insubordination and laziness, Professor Boolean just "eliminated" the lab assistant tracking all data from this research. Now, he's forcing you to sort through the notes and find something useful from the chaos. You have no choice but to abide by your captors evil rules. For now.
#
#Of the subjects that have survived, each has a distinct file, with anywhere from 1 to 100 measurements of completion time for the tests. The measurements from the before and after cases are listed separately, but the ordering has been mixed up. You have to figure out the degree of improvement (0% to 99%, rounded to the nearest whole number) based on the two lists of results.
#
#For example, if the first list of times is [22.2, 46, 100.8] and the second list is [23, 11.1, 50.4] you would return 50, because the times got 50% shorter: the 22.2 entry improved to 11.1, the 46 improved to 23, and the 100.8 improved to 50.4. Even though the data points are in different order, each improves by the same amount.
#
#Write a function answer(x, y) which takes two lists of floating point performance scores and returns the improvement percentage, rounded to the nearest integer.
#
#
#Languages
#=========
#
#To provide a Python solution, edit solution.py
#To provide a Java solution, edit solution.java
#
#Test cases
#==========
#
#Inputs:
#    (double list) y = [1.0]
#    (double list) x = [1.0]
#Output:
#    (int) 0
#
#Inputs:
#    (double list) y = [2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002]
#    (double list) x = [23.0, 150.0, 1024.0, 34868.0]
#Output:
#    (int) 90
#
#Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

def answer(y, x):
    # your code here
    y.sort()
    x.sort()
    if y[0] >= x[0]:
        maxList = y
        minList = x
    else:
        maxList = x
        minList = y
    result = []
    for i in range(0, len(y)):
        result.append(((maxList[i]-minList[i])/maxList[i])*100)
        
    sumVal = 0
    for i in range(0, len(y)):
        sumVal += result[i]
        
    avgVal = int(sumVal//len(y))
    
    return avgVal
