from tools.col import myzip
from tools.numbers.simp import add, sub
from tools.numbers.comp import sumofdigits, ispal
from icecream import ic

def simp_before():
    global num , num1 , num2 , pal_num
    simp_called = False
    
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            
            add(num1, num2)
            sub(num1,num2)
            simp_called = True
            break
        
        except ValueError:
            print("Invalid input, please enter two integers")
            continue

    if simp_called:
        num = int(input("Enter a number: "))
        pal_num = int(input("Enter a number to check palindrome: "))




if __name__ == "__main__":
    ic(simp_before())
    list1 = [1,2,3]
    list2 = ['a','b','c']
    ic(list(myzip(list1, list2)))
    ic(add(num1,num2))
    ic(sub(num1,num2))
    ic(sumofdigits(num))
    ic(ispal(pal_num))