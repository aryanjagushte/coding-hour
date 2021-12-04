import math
while True:  
    print('CHOOOSE CALCULATION FROM THE FOLLOWING'
        "1. Add\n2. 2. Subtract\n3. 3. Multiply\n4. 4. Divide\n5.  5. Exit\n")  
    choose_calculation = input("1. Add\n2. 2. Subtract\n3. 3. Multiply\n4. 4. Divide\n5. 5. Square\n. 6. Squareroot\n. 7. Exit\n")

    if choose_calculation == '1':
        lst = []
        num = int(input('How many numbers to add: '))
        for n in range(num):
           numbers = int(input('Enter number '))
           lst.append(numbers)
           print("Sum of elements in given list is:",sum(lst))

    elif choose_calculation == '2':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        diff = n1 - n2
        print("The difference is:",diff)
           

        
    elif choose_calculation == '3':
         lst1 = []
         num1 = int(input('How many numbers to multiply: '))
         for i in range(num1):
           numbers1 = int(input('Enter number '))
           lst1.append(numbers1)
           print("multiplication of elements in given list is:", math.prod(lst1))

        
    
    elif choose_calculation == '4':
         n3 = float(input("Enter first number: "))
         n4 = float(input("Enter second number: "))
         div = n3 / n4
         print("The quotient is:",div)

    
    elif choose_calculation == '5':
        break
    
    else:
        print("Enter correct choice!!")
