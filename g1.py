import itertools
import datetime

def validPerm(l):
        x,y,z = l[0],l[1],l[2]
        
        try:
            datetime.datetime(year=z,month=x,day=y)
            correctDate = True
        except ValueError:
            correctDate = False
                
        if correctDate:
                return True
        else:
                return False
        

def checkValidPermutation(lis):
        l = ()
        for i in lis:
                if (validPerm(i)):
                        l.append(i)
        return l

def answer(x, y, z):
        # your code here
        perm = set(itertools.permutations([x,y,z]))
        result = checkValidPermutation(perm)
        if len(result) == 1:
                #print(result[0][1])
                
                return "%02d/%02d/%02d" % (result[0][0],result[0][1],result[0][2])
        else:
                return "Ambigious"


print(answer(31,21,99))
