import itertools

def validPerm(l):
        x,y,z = l[0],l[1],l[2]
        monthValid = False
        dayValid = False
        yearValid = False
        if (x >0 and x <= 12):
                monthValid = True
        else:
                monthValid = False
                
        if (y > 0 and y <= 32):
                dayValid = True
        else:
                dayValid = False
        
        if (z > 0 and z <= 99):
                yearValid = True
        else:
                yearValid = False
                
        if monthValid and dayValid and yearValid:
                return True
        else:
                return False
        

def checkValidPermutation(lis):
        l = []
        for i in lis:
                if (validPerm(i)):
                        l.append(i)
        return l

def answer(x, y, z):
        # your code here
        l=[x,y,z]
        perm = set(itertools.permutations([x,y,z]))
        result = checkValidPermutation(perm)
        if len(result) == 1:
                #print(result[0][1])
                print("%02d/%02d/%02d" % (result[0][0],result[0][1],result[0][2]))
        else:
                print("Ambigious")
        
answer(2,30,3)
