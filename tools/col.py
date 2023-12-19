from icecream import ic

# combine 2 lists to one

def myzip(it1, it2):
    it1 = iter(it1)
    it2 = iter(it2)
    
    while True:
        v1 = next(it1, None)
        v2 = next(it2, None)
        if v1 is None and v2 is None:
            return 
        yield (v1, v2)
