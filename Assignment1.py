#Assignment1

number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))

operater = input("select operater to perform \t'+ for addition' \t'- for subtraction' \t'* for product' \t'/ for division'\n")

if operater == '+':
    print("sum = ",number1+number2)
elif operater == '-':
    print("subtraction =",number1-number2)
elif operater == '*':
    print("product = ",number1*number2)
elif operater == '/':
    print("division =",number1/number2)6
    