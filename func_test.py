from tools.col import myzip
from tools.numbers.simp import add, sub
from tools.numbers.comp import sumofdigits, ispal
from icecream import ic


if __name__ == '__main__':
    list1 = [1,2,3] 
    list2 = ['a','b','c']
    ic(add(12,13))
    ic(sub(15,23))
    ic(sumofdigits(23454))
    ic(ispal(122321))
    ic(ispal(666311))
    ic(myzip(list1,list2))