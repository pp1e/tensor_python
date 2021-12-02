def sumAll(*args):
    try:
        sum=None
        for arg in args:
            if sum==None:
                sum=arg
            else:
                sum+=arg
        if sum is None:
            sum=0        
        return sum
    except TypeError:
        print("Error! Invalid argumets types")
        return None    

sum=sumAll('ASFAS',1)
if sum is not None:
    print('Sum of arguments: '+str(sum))              