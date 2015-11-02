#def multipliers():
#    return [lambda x : i * x for i in range(4)]
# Output : [6,6,6,6]
# Due to late binding

def multipliers():
     for i in range(4): yield lambda x : i * x 
#Output : [0,2,4,6]
    
print([m(2) for m in multipliers()])
