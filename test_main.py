from tools.numbers.simp import add, sub  
from tools.numbers.comp import sumofdigits, ispal
from icecream import ic

def simp_before():
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
    global num , num1 , num2 , pal_num
    simp_before()
        